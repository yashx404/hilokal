// world:"MAIN" — runs synchronously at document_start in the page's JS context.

// ── parse socket.io frame (handles ack-id prefix) ────────────────────────────
// "42["ev",data]"    → plain event
// "4217["ev",data]"  → event with ack id 17 (the requestId you see in logs)
function _parseSio(raw) {
    if (typeof raw !== 'string' || !raw.startsWith('42')) return null;
    const s = raw.slice(2), i = s.indexOf('[');
    if (i < 0) return null;
    try { return JSON.parse(s.slice(i)); } catch (_) { return null; }
}

// ── Room + message detection (ported from the supplied userscript) ──────────
// Hilokal exposes message records through API responses and React props. We
// collect both paths because the page does not always issue a fresh messages
// fetch after the extension is opened.
const HL_ROOM_RE = /group-call\/(\d+)\/(participants|messages|stay-time)/;
let hlCurrentRoom = null;
const hlMessageStore = Object.create(null); // roomId -> { messageId: {id,userId,body,type} }
let hlLastPublish = 0;

function hlBucket() {
    if (!hlCurrentRoom) return null;
    return hlMessageStore[hlCurrentRoom] || (hlMessageStore[hlCurrentRoom] = Object.create(null));
}
function hlPublish(force = false) {
    const now = Date.now();
    if (!force && now - hlLastPublish < 500) return;
    hlLastPublish = now;
    const bucket = hlBucket();
    if (!bucket) return;
    window.postMessage({
        type: '__HILOKAL_MESSAGES__',
        roomId: hlCurrentRoom,
        data: Object.values(bucket)
    }, '*');
}
function hlSetRoom(url) {
    const match = String(url || '').match(HL_ROOM_RE);
    if (!match) return;
    if (match[1] !== hlCurrentRoom) {
        hlCurrentRoom = match[1];
        console.log('[HL] room detected:', hlCurrentRoom, 'from', String(url));
        window.postMessage({ type: '__HILOKAL_ROOM__', roomId: hlCurrentRoom }, '*');
        hlScrapeReact();
        hlPublish(true);
    }
}
function hlAddRecord(x) {
    const bucket = hlBucket();
    if (!bucket || !x || typeof x !== 'object' || x.id == null || x.userId == null) return;
    if (!('body' in x) && !('type' in x)) return;
    const id = String(x.id);
    bucket[id] = {
        id,
        userId: Number(x.userId),
        body: String(x.body || x.message || x.text || ''),
        type: String(x.type || '')
    };
}
function hlScanData(data) {
    (function walk(x) {
        if (Array.isArray(x)) { x.forEach(walk); return; }
        if (!x || typeof x !== 'object') return;
        hlAddRecord(x);
        Object.values(x).forEach(walk);
    })(data);
    hlPublish();
}

// Fetch: preserve the page's normal request/response behavior and inspect a
// clone of message responses, just like the userscript.
const OriginalFetch = window.fetch.bind(window);
window.fetch = function (...args) {
    const input = args[0];
    const url = typeof input === 'string' ? input
        : (input && typeof input.url === 'string') ? input.url : '';
    try {
        const callMatch = String(url).match(/\/group-calls?\/(\d+)\/(?:emoji|seat-request|card|messages|pin)/);
        if (callMatch) window.postMessage({ type: '__HILOKAL_CALL_ID__', callId: callMatch[1] }, '*');
        hlSetRoom(url);
    } catch (_) {}

    const result = OriginalFetch(...args);
    try {
        if (/messages/i.test(String(url))) {
            result.then(res => res.clone().json().then(hlScanData).catch(() => {})).catch(() => {});
        }
    } catch (_) {}
    return result;
};

// XHR: the supplied userscript uses open() to detect room changes. Also inspect
// JSON response bodies when available, which catches XHR-backed message APIs.
const OriginalXHROpen = XMLHttpRequest.prototype.open;
const OriginalXHRSend = XMLHttpRequest.prototype.send;
XMLHttpRequest.prototype.open = function (method, url) {
    this.__hlUrl = String(url || '');
    try { hlSetRoom(this.__hlUrl); } catch (_) {}
    return OriginalXHROpen.apply(this, arguments);
};
XMLHttpRequest.prototype.send = function () {
    if (/messages/i.test(this.__hlUrl || '')) {
        this.addEventListener('load', () => {
            try {
                const parsed = this.responseType === 'json' ? this.response : JSON.parse(this.responseText);
                if (parsed) hlScanData(parsed);
            } catch (_) {}
        }, { once: true });
    }
    return OriginalXHRSend.apply(this, arguments);
};

// React-fiber scan from the userscript. This is important when the chat list
// is already rendered and no messages API request happens after page startup.
function hlScrapeReact() {
    if (!hlCurrentRoom) return;
    const bucket = hlBucket();
    if (!bucket) return;
    document.querySelectorAll('div').forEach(el => {
        const fiberKey = Object.keys(el).find(key => key.startsWith('__reactFiber$'));
        if (!fiberKey) return;
        let fiber = el[fiberKey], depth = 0;
        while (fiber && depth++ < 8) {
            const props = fiber.memoizedProps;
            if (props && typeof props === 'object') {
                for (const value of [props, ...Object.values(props)]) {
                    if (value && typeof value === 'object' && value.id != null && value.userId != null && 'body' in value) {
                        hlAddRecord(value);
                    }
                }
            }
            fiber = fiber.return;
        }
    });
    hlPublish();
}
setInterval(hlScrapeReact, 3000);

// ── Ghost Speak: intercept WebRTC APIs ───────────────────────────────────────
// When window.__ghost is true, these block the browser from stopping your mic.

// 1. RTCPeerConnection.close() — blocks whole transport teardown
const _OrigRTC = window.RTCPeerConnection;
window.RTCPeerConnection = new Proxy(_OrigRTC, {
    construct(T, args) {
        const pc = new T(...args);
        const orig = pc.close.bind(pc);
        pc.close = function () {
            if (window.__ghost) { console.warn('[Ghost] ✋ pc.close() blocked'); return; }
            return orig();
        };
        return pc;
    },
});
window.RTCPeerConnection.prototype = _OrigRTC.prototype;

// 2. track.stop()
const _origStop = MediaStreamTrack.prototype.stop;
MediaStreamTrack.prototype.stop = function () {
    if (window.__ghost) { console.warn('[Ghost] ✋ track.stop() blocked'); return; }
    return _origStop.call(this);
};

// 3. track.enabled = false
const _td = Object.getOwnPropertyDescriptor(MediaStreamTrack.prototype, 'enabled');
if (_td && _td.set) {
    Object.defineProperty(MediaStreamTrack.prototype, 'enabled', {
        get() { return _td.get.call(this); },
        set(v) {
            if (window.__ghost && !v) { console.warn('[Ghost] ✋ track.enabled=false blocked'); return; }
            _td.set.call(this, v);
        },
        configurable: true,
    });
}

// 4. replaceTrack(null)
const _origRep = RTCRtpSender.prototype.replaceTrack;
RTCRtpSender.prototype.replaceTrack = function (t) {
    if (window.__ghost && t === null) { console.warn('[Ghost] ✋ replaceTrack(null) blocked'); return Promise.resolve(); }
    return _origRep.call(this, t);
};

// 5. removeTrack()
const _origRem = RTCPeerConnection.prototype.removeTrack;
RTCPeerConnection.prototype.removeTrack = function (s) {
    if (window.__ghost) { console.warn('[Ghost] ✋ removeTrack() blocked'); return; }
    return _origRem.call(this, s);
};

// ── WebSocket proxy ───────────────────────────────────────────────────────────
const GHOST_BLOCK = new Set([
    'leave-table',                                          // ← KEY: stops server telling others to close your audio
    'close-transport', 'closeTransport', 'closeWebRtcTransport',
    'closeProducer',   'pauseProducer',
]);

const OriginalWebSocket = window.WebSocket;

function PatchedWebSocket(url, protocols) {
    const ws = protocols
        ? new OriginalWebSocket(url, protocols)
        : new OriginalWebSocket(url);

    const isMed = url.includes('hilokal-media') || url.includes('mediasoup');

    // Intercept outgoing sends — log EVERYTHING when ghost is on, block known events
    const origSend = ws.send.bind(ws);
    ws.send = function (raw) {
        const p = _parseSio(raw);
        if (p) {
            const [ev, pl] = p;
            // Log ALL sends on BOTH sockets when ghost is on so we miss nothing
            if (window.__ghost) {
                console.log('[' + (isMed ? 'media→' : 'main→ ') + ']', JSON.stringify(ev), pl !== undefined ? JSON.stringify(pl).slice(0, 120) : '');
            }
            if (isMed && window.__ghost && GHOST_BLOCK.has(ev)) {
                console.warn('[Ghost] ✋ BLOCKED media emit "' + ev + '"');
                return;
            }
        }
        return origSend(raw);
    };

    // Intercept incoming messages — participant cards + chat
    ws.addEventListener('message', (event) => {
        if (typeof event.data !== 'string') return;
        if (!event.data.startsWith('42')) return;
        const p = _parseSio(event.data);
        if (!p) return;
        const [eventName, payload] = p;
        if (!eventName) return;

        if (isMed && window.__ghost) {
            // Log ALL incoming media events when ghost is on
            console.log('[media←]', JSON.stringify(eventName), payload !== undefined ? JSON.stringify(payload).slice(0, 120) : '');
        }

        if (eventName === 'group-call-card') {
            extractParticipant(payload);
        } else if (payload && payload.userId && (payload.body || payload.message || payload.text)) {
            // Chat message — relay to extension
            window.postMessage({
                type:    '__HILOKAL_CHAT__',
                who:     payload.senderName || ('user#' + payload.userId),
                text:    payload.body || payload.message || payload.text,
                eventName,
            }, '*');
        }
    });

    return ws;
}

PatchedWebSocket.prototype = OriginalWebSocket.prototype;
Object.setPrototypeOf(PatchedWebSocket, OriginalWebSocket);
window.WebSocket = PatchedWebSocket;

function extractParticipant(obj) {
    if (!obj || typeof obj !== 'object') return;
    if (obj.name && obj.accessCityName) {
        window.postMessage({
            type:    '__HILOKAL_GCC__',
            uid:     (obj.id != null) ? obj.id : null,
            name:    obj.name,
            city:    obj.accessCityName,
            country: obj.accessCountryCode || obj.countryCode || '',
            gender:  obj.gender || '',                                   // 'M' | 'F' | ''
            level:   (typeof obj.languageLevel === 'number') ? obj.languageLevel : null,
            native:  obj.nativeLang || '',
            target:  obj.targetLang || '',
            role:    obj.role || '',                                     // 'host' | ''
            badge:   obj.badge || '',                                    // 'birthday' | 'newuser-incomplete' | ''
            newUser: obj.isNewUser ? 1 : 0,
            serious: obj.isSeriousUser ? 1 : 0,
            premium: obj.premium ? 1 : 0,
            teacher: (obj.trainer || (obj.verifiedTeacher && obj.verifiedTeacher !== '')) ? 1 : 0,
            color:   obj.textColor || '',                                // 'BLUE' | 'PURPLE' | 'YELLOW' | 'DEFAULT' | ''
            avatar:  obj.profileImageUrl || '',
            bio:     obj.bio || '',
            ts:      Date.now(),
        }, '*');
    }
    for (const k in obj) {
        if (typeof obj[k] === 'object') extractParticipant(obj[k]);
    }
}

// ── Ghost toggle (popup communicates via postMessage) ─────────────────────────
window.__ghost = false;
window.ghostOn  = () => { window.__ghost = true;  console.warn('[Ghost] 🟢 ON');  updateGhostBtn(); };
window.ghostOff = () => { window.__ghost = false; console.warn('[Ghost] 🔴 OFF'); updateGhostBtn(); };

window.addEventListener('message', (e) => {
    if (!e.data) return;
    if (e.data.type === '__GHOST_ON')  window.ghostOn();
    if (e.data.type === '__GHOST_OFF') window.ghostOff();
});

// Keyboard shortcut: Ctrl+Shift+G
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.shiftKey && e.key === 'G') {
        window.__ghost = !window.__ghost;
        updateGhostBtn();
        console.warn('[Ghost]', window.__ghost ? '🟢 ON (Ctrl+Shift+G)' : '🔴 OFF (Ctrl+Shift+G)');
    }
}, true);

// No floating on-page button — the Ghost feature is still reachable via the
// Ctrl+Shift+G keyboard shortcut above; it just no longer draws UI on the page.
function updateGhostBtn() { /* button removed — kept as a no-op for the callers above */ }

console.warn('[Hilokal] inject.js loaded — Ghost toggle: Ctrl+Shift+G');


// Bulk message deletion bridge. The server remains the authority on whether
// the signed-in account may delete each message (e.g. moderator permissions).
let hlDeleteRunning = false;
let hlStopDelete = false;
window.addEventListener('message', async (event) => {
    if (event.source !== window || event.data?.type !== '__HILOKAL_DELETE_MESSAGES__') return;
    if (hlDeleteRunning) return;

    const { roomId, messageIds, requestId } = event.data;
    if (!/^\d+$/.test(String(roomId)) || !Array.isArray(messageIds) || !requestId) return;

    const ids = [...new Set(messageIds.map(value => String(value)))];
    if (!ids.length || ids.length > 10000) return;

    hlDeleteRunning = true;
    hlStopDelete = false;
    let deleted = 0, failed = 0, processed = 0, stopped = false;

    try {
        for (const rawId of ids) {
            if (hlStopDelete) { stopped = true; break; }
            const id = Number(rawId);
            if (!/^\d+$/.test(rawId) || !Number.isSafeInteger(id) || id <= 0) {
                failed++;
                processed++;
            } else {
                try {
                    const res = await OriginalFetch(`https://elb.hilokal.com/group-call/${roomId}/messages/${id}`, {
                        method: 'DELETE', credentials: 'include',
                        headers: { 'content-type': 'application/json', accept: 'application/json' },
                        body: '{}'
                    });
                    if (res.ok) deleted++; else failed++;
                } catch (_) { failed++; }
                processed++;
                await new Promise(resolve => setTimeout(resolve, 400));
            }
            window.postMessage({
                type: '__HILOKAL_DELETE_PROGRESS__', requestId,
                processed, total: ids.length, deleted, failed
            }, '*');
        }
    } finally {
        hlDeleteRunning = false;
        hlStopDelete = false;
        window.postMessage({
            type: '__HILOKAL_DELETE_RESULT__', requestId,
            deleted, failed, stopped
        }, '*');
    }
});
window.addEventListener('message', event => {
    if (event.source === window && event.data?.type === '__HILOKAL_STOP_DELETE__') {
        hlStopDelete = true;
    }
});
