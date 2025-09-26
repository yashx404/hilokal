import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1NzEzMzciLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzMzMDU3ODEzfQ.vFgVsO6uwB6Q5xv4zToRKuOJuVi4KaT1MDBtaXC8iszR72hRC9NV1TbQBJugUaJRBK10haGSZo3Sxp0xY_DUp_j7DSjWiElyScAh4cw6QK8uY8mTspJpGYopttYhZ59pW5sHBcc8AGrrvnsE7u_nG1DUHrPDLbtiPy3eIEmjlCbuJ4tnQrwo255c6E-pVFtHZYC-6RDw0g9z7sMrss-wyfXD6tT1Vsxo7YYphaBacXSt9_Ibg0I5Elclki4jXS9pdWtKAZe9LLhKVKhLdnFWG1TxScI90Oz02xTaelR8d4_0CYKKGi3v26mjA0_CqsbM8c__puYzk9jongWWC6De2g',
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
    #'nativeLang': 'ru',
    #'nativeChangingCount': 1,
    #'targetLang': '',
    #'nativeChangingCount': 1,
    #'countryCode': '',
    #'profileImageUrl': 'https://media.giphy.com/media/F85cGwDfqrBPKQc7SN/giphy.gif',
}
response = requests.put('https://elb.hilokal.com/users/me', cookies=cookies, headers=headers, json=json_data)