import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzc4NjQ5OTM5fQ.rVz6fvxpVLVHbqRcuO4PR3oOxsKz56IaFkZjNpH3jpBe9rxS42sX4iOTRF0VhYrtq60WnjnMmrkVw2OXfU0iMkcNYA47fW50v5s-RTdabfL9TSjpFcEAYdk2RXsFB9SFo-ByJuFD-KYApzpnhA5vBpU-7EDn_fJLSGpxi1E6I-yHKtXQGUgJxKkTdUkXF2v1k1x6Hb1mHqjEzOVWhF8H0cHQ3Kf21GHAydf5Vncsp6ctdhLyxPvqCnch7-0EnvHfVFdiI-41zNck2rMc8_0CMl8dfBvGb1CCW1GXwhITmqniGlFd35uyExU9dvdBoflwHUmTCDpKBrflj5OMuSCnEQ',
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
    'targetUserId': 1919159,
}
while True:
    response = requests.post('https://elb.hilokal.com/group-call/4021503/kicks', cookies=cookies, headers=headers, json=json_data)
time.sleep(1)