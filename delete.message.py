import requests
import time
cookies = {
    '_gcl_au': '1.1.1281012474.1787123063',
    '_hjSessionUser_2705208': 'eyJpZCI6IjRjY2FkOTcyLWIxNGEtNTdkMC1iNzkwLTJiZmM2MzVhZDY4YiIsImNyZWF0ZWQiOjE3ODcxMjMwNjM1OTAsImV4aXN0aW5nIjp0cnVlfQ==',
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzg5MDE2NjE1fQ.iVEhY2NnfpmcKjemTxfkhseOV65mS4ZuXH5JQVIxDNTYhHAIE_38ruG30oKddJzN2Rs0L61AeAJuL4NFwngHKPMj7hQoAGO1VrNo-wAEE-ZrsgXudBOqOOcmskfTfYLePtTyXvma8QmWqByOnHIJgNaH-rgUPTbGptre46u8IHLmvXXqQ5ahAtTIGzTKSh3qceCpV-s3bF8QMmEnD-g-owar0Idtg6RX_BiAsRyYdvRkco5GyzagViEasq7XGqmgAJb_SlWa0azVYSdGgzlDXvdWIP54HApTg5sAlT1cztkOpr2k9AAmPAg0zZJbvoYH6FBURDGgpVzdJ1SASq09ow',
    '_gid': 'GA1.2.1175261942.1789972552',
    '_hjSession_2705208': 'eyJpZCI6IjA3MTUzZjRkLTQzZjItNDNmMy05OGQxLTUyZmU1OThiZTI5MiIsImMiOjE3ODk5ODI5ODc0MjMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_ga': 'GA1.2.118388267.1787123063',
    '_ga_6HCL2GMXBV': 'GS2.1.s1789982988$o67$g1$t1789984344$j60$l0$h0',
    '_ga_S97T9P1W73': 'GS2.1.s1789982986$o68$g1$t1789984344$j60$l0$h0',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
}
json_data = {}
GROUP_CALL_ID = 4021503 
message_ids = [
      156792425

]

session = requests.Session()
session.cookies.update(cookies)
session.headers.update(headers)

for msg_id in message_ids:
    url = f'https://elb.hilokal.com/group-call/{GROUP_CALL_ID}/messages/{msg_id}'
    try:
        response = session.delete(url, json={}, timeout=10)
        print(msg_id, response.status_code)
        if not response.ok:
            print("  Failed:", response.text)
    except requests.RequestException as e:
        print(msg_id, "error:", e)
    time.sleep(0.5)