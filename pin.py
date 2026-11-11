import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzc1NjM5NTI0fQ.qKEQBpANHz7r3u0OhSBLtBDco2WYAgBY3tc2Ley-BA05Q9bVlfrssv-EPSECSB5HNsE4_JttalZPMVkTuwDAfQcoD1G0Su8CSvj1t_K8n9MDb6E_tz8BsTC2cnK8YZ_npq65kND_6OdhwxJuTk7NrgsnhgTl7qPg0GFzVoKYlv1AcaDgVCJEq6-lrf6-5NSPhrVjJlEZa_A4po0ZerAXV7ltmNWNFBFQA7dSBsKVF4DuPJWR47kv05lJXXwy2Fe0F7t9aDGFnkPhs9G3N3ZSrr83z5KJceayUggh8K1bMg7xQGDsCNFVT3Z6eb-rFy1bJq0k5xRGVAfPKhdmBVYhrg',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
}
json_data = {
    'type': 'text',
    'body': '💀',
    'imageUrl': None,
    'imageWidth': None,
    'imageHeight': None,
    'userId': 808418,
    'sourceType': 'group-chat',
    'sourceId': 156686690,
    'libraryId': None,
}
while True:
    response = requests.post('https://elb.hilokal.com/group-calls/4021503/pins', cookies=cookies, headers=headers, json=json_data)
time.sleep(1)