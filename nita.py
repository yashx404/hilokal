import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjAyOTciLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzI4ODE5OTM5fQ.VfBO1eRtq4OCJMLIpmosvOpAJ3lc1kUOxJ6pcNjwzajQOO8jhGyqIzxTJqpLt8E2fhpzqMQa62tDTxIuzAHLa8SYrpOWNlvZ5VMuq8n2DaVCalS0IQNi2bxdUCXMrR3CmzbFOW3fNacNTrKsu1eT1qWi8lJWw5JThAycSHGz7ISmItvAuB7Ac1eT0UYO4dYjNA5LfPdeMma-LR4yGO2xJ0-lwroJHevy6USqZaGsscxGjRYLBCa-vyh3TdkHpmBxFIpnYBHdrBgbT8wMB5PYEtknNL2uguLuQp8AAjQBH1AcqAtU2-syT4A3R-HgEAP0Y2UK7gGaZjXt8GadS_APeA',
}
headers = {
    'authority': 'elb.hilokal.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
json_data = {
    #'nativeLang': 'en',
    #'nativeChangingCount': 1,
    #'targetLang': ' ',
    'name': 'fox',
    #'nativeChangingCount': 1,
    #'profileImageUrl': 'https://media.giphy.com/media/F85cGwDfqrBPKQc7SN/giphy.gif',
}
response = requests.put('https://elb.hilokal.com/users/me', cookies=cookies, headers=headers, json=json_data)