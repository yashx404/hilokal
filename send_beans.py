import requests
headers = {
    'authority': 'elb.hilokal.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzkxNDQzNzM1fQ.P4DlVAYPHnUPwmAUzeV3VO7dBDO1BdEaCP4zS1hkDWx16-uE8HsyQhgYPQbRe0-5HKZaETOaBURMGdmFwu2UqBLKi7xQRLKgWnyAjUfQ_D3gm0Ah_o9ECNRw9fVTcAMNkUEepYYhlHlIONTYl7bRKWORXIMes8jK4oTibOBEzX1pSZIBbTdwxAxkITckB7hwxPSIrPzOxynMNaIcM29jzIlP60vq9jQX8qiObUSulK4vobe-jWfcVUbsmZGwzDPmhJ37suauOmsG1ZBEG8gW8aqoJjyIMhs8rGEg008XEk84JXL9K8gM3kBh6186Z_BUuRPAmf99b2j9-ChVKU_0pg',
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
balance_response = requests.get('https://elb.hilokal.com/users/me', headers=headers)
balance = balance_response.json().get('beans', 0)  # Adjust key name as needed

json_data = {
    'receiverId': 2537325,
    'type': 'send',
    'groupCallId': 4021503,
    'anonymous': False,
    'message': 'richie rich',
    'amount': '69',
}

response = requests.post('https://elb.hilokal.com/users/beans', headers=headers, json=json_data)
print("Status:", response.status_code)
print("Response:", response.text)