import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDc5NTYzIiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTc1MzQ1NTY3M30.OfS2tJUyxIwiHaDEoEc9kQFUaaLgYInMz6n8KNcNxpDlvFH_yojVgwSCn-0oNlwQAeiGErg5q4gx-pv7Cin15RiAqD5TOrlR659qrJnZV2_IJpH_PgcK8feMh-OUXZfphUxsRjfOvYUTpXIU3TShJJSAVyiMmTYktR8dDlg9V4bI1QChJ70Y6kwNsv0D4wYCzkyDNm_CQurJtApZjdukulJ_PPLX7TnKfGh8lzOyzVPzZxEwDRGmDSj1tBYYD5-AVvW_XTS8-G6AzpZav5hrNrK6FTDPOGwJv4ZvPiKE05E0YDTPFI50V1QPTROaoAZYGm4WqC9fsmqHMDz842KOww',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
}

json_data = {
    'invitedUserIds': [
        2396476,
    ],
}
while True:
    response = requests.post('https://elb.hilokal.com/group-call/5732388/invitation', cookies=cookies, headers=headers, json=json_data)
time.sleep(1)