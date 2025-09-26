import requests
headers = {
    'authority': 'elb.hilokal.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1MDc1NjUiLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNjk3OTU1MzYyfQ.ryzcyEiEHHlYGYtWzvhqV3JKe025k5CodjMy0dbiY0uNYHCRud7WuQs5ljBM1C208E1w0mI_k1JiSO__8b2kb34uUjyunAs9hVK6d7NZxDUE7wpMBdLjsvAkyjEXAJW4dXTm8rAEno7FCs7UYV8spG8HG_pWh8i3n7psUnZEmljjYHs3WUpTD5OjDr5TeziejWB_Icx7aA5T-0s1y1aV2CkfUW8O-kNTltAwWTtjepn3fUlKSnf0q2iDB6LsaVvhYqdxhbFry1RjbERpXhKt62OCWr9i_ppnfllhQciMglpEK7Kpoh8JsxWUCe2tHMOQ30zjAcl_FMuO5XNIuqeEOQ',
    'if-none-match': 'W/"25-sy2QoFZV6s5dxnt7crxe0Ai1XgQ"',
    'origin': 'https://www.hilokal.com',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
json_data = {
    'available': True,
    'remainingDays': '0',
}
response = requests.post('https://elb.hilokal.com/users/name-availability', headers=headers, json=json_data)