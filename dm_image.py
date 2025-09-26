import requests
cookies = {
    '_hjSessionUser_2705208': 'eyJpZCI6IjljMTExYWUwLTlkNDYtNTAzZC04OTM3LWU1YTc1MjJjNzY1ZiIsImNyZWF0ZWQiOjE3Mzc2Mzg1MTg0NjMsImV4aXN0aW5nIjp0cnVlfQ==',
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1MDc1NjUiLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzQ5OTgzOTM1fQ.odghEblq_0MpT9-ZOOCDk35kHopO3MyyoM96XxdC_oPYz-wdsLaym-UXT38B8X6GglQHYJ-b1EJHx0mGawWCQEdKbbR6LvKRCtmrMUyDYmGIH1N7kA74pEm09tesF0sNtLm4vFj1RDWirHXz2IXer4z6FHYRfCUbcp_0uBE5Z3s8xwdNWmGRSANmHciju_8j2VZ0-D0rZFERDYM8SvinvCskcLm4zARzvTgCnOuviVSWy-jXHyhaErICaqI5EZ-8uKr8Rq4DJ5BjVN4eamYLZIlJICAhIRwcju5S0cWIfHl1Bk6-YZvMTvWCTbY-Z4Pbpt12-nOtxhWDA9lW33Py8A',
    '_gid': 'GA1.2.750465270.1751731503',
    '__gads': 'ID=f8073d284904e32d:T=1737638519:RT=1751731510:S=ALNI_MZ5YmmIfwtKMBgK1mNP7LtgSEeDQg',
    '__gpi': 'UID=000010091f423ad7:T=1737638519:RT=1751731510:S=ALNI_MaKnAQfDdq9YIthu9-n0vQyAXG9EQ',
    '_hjSession_2705208': 'eyJpZCI6ImNmNjdmNWUyLWQ5ZTItNGE3Ni05N2I5LTlhYWE4OTAyOGE0YiIsImMiOjE3NTQxMzgwOTg3MzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_ga': 'GA1.1.381345667.1737638518',
    '_ga_6HCL2GMXBV': 'GS2.1.s1754138098$o177$g1$t1754144749$j45$l0$h0',
    '_ga_S97T9P1W73': 'GS2.1.s1754138099$o177$g1$t1754144751$j43$l0$h0',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_hjSessionUser_2705208=eyJpZCI6IjljMTExYWUwLTlkNDYtNTAzZC04OTM3LWU1YTc1MjJjNzY1ZiIsImNyZWF0ZWQiOjE3Mzc2Mzg1MTg0NjMsImV4aXN0aW5nIjp0cnVlfQ==; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1MDc1NjUiLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzQ5OTgzOTM1fQ.odghEblq_0MpT9-ZOOCDk35kHopO3MyyoM96XxdC_oPYz-wdsLaym-UXT38B8X6GglQHYJ-b1EJHx0mGawWCQEdKbbR6LvKRCtmrMUyDYmGIH1N7kA74pEm09tesF0sNtLm4vFj1RDWirHXz2IXer4z6FHYRfCUbcp_0uBE5Z3s8xwdNWmGRSANmHciju_8j2VZ0-D0rZFERDYM8SvinvCskcLm4zARzvTgCnOuviVSWy-jXHyhaErICaqI5EZ-8uKr8Rq4DJ5BjVN4eamYLZIlJICAhIRwcju5S0cWIfHl1Bk6-YZvMTvWCTbY-Z4Pbpt12-nOtxhWDA9lW33Py8A; _gid=GA1.2.750465270.1751731503; __gads=ID=f8073d284904e32d:T=1737638519:RT=1751731510:S=ALNI_MZ5YmmIfwtKMBgK1mNP7LtgSEeDQg; __gpi=UID=000010091f423ad7:T=1737638519:RT=1751731510:S=ALNI_MaKnAQfDdq9YIthu9-n0vQyAXG9EQ; _hjSession_2705208=eyJpZCI6ImNmNjdmNWUyLWQ5ZTItNGE3Ni05N2I5LTlhYWE4OTAyOGE0YiIsImMiOjE3NTQxMzgwOTg3MzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ga=GA1.1.381345667.1737638518; _ga_6HCL2GMXBV=GS2.1.s1754138098$o177$g1$t1754144749$j45$l0$h0; _ga_S97T9P1W73=GS2.1.s1754138099$o177$g1$t1754144751$j43$l0$h0',
}
json_data = {
    'roomId': '2b5772ae-c244-4264-9633-cc3eb3e2fdf7',
    'body': '',
    'type': None,
    'parentId': None,
    'messageType': 'image',
    'voiceMessageUrl': None,
    'imageUrl': 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2dpbGZrZGt5eDh2MmIxNzBsNDVidGVnaHIxdWpjOWF5NDF4d2Q4ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dmUUlUUMd3y8UlwrMR/giphy.gif',
    'imageWidth': 1920,
    'imageHeight': 1080,
}
response = requests.post(
    'https://elb.hilokal.com/direct-messages/room/2b5772ae-c244-4264-9633-cc3eb3e2fdf7/messages',
    cookies=cookies,
    headers=headers,
    json=json_data,
)