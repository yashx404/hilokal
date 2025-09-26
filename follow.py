import requests

cookies = {
    '_gcl_au': '1.1.375516535.1755955110',
    '_gid': 'GA1.2.1540647109.1755955110',
    '_hjSessionUser_2705208': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDc5NTYzIiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTc1MzQ1NTY3M30.OfS2tJUyxIwiHaDEoEc9kQFUaaLgYInMz6n8KNcNxpDlvFH_yojVgwSCn-0oNlwQAeiGErg5q4gx-pv7Cin15RiAqD5TOrlR659qrJnZV2_IJpH_PgcK8feMh-OUXZfphUxsRjfOvYUTpXIU3TShJJSAVyiMmTYktR8dDlg9V4bI1QChJ70Y6kwNsv0D4wYCzkyDNm_CQurJtApZjdukulJ_PPLX7TnKfGh8lzOyzVPzZxEwDRGmDSj1tBYYD5-AVvW_XTS8-G6AzpZav5hrNrK6FTDPOGwJv4ZvPiKE05E0YDTPFI50V1QPTROaoAZYGm4WqC9fsmqHMDz842KOww',
    '_hjSession_2705208': 'eyJpZCI6ImY2YmM4MzlhLTNhODMtNDYzYi04MjdjLThmZmM2OWY5YTUxNCIsImMiOjE3NTYwMTE4ODQxNDUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_gat_UA-184236194-1': '1',
    '_ga': 'GA1.1.1939536911.1755955110',
    '_ga_6HCL2GMXBV': 'GS2.1.s1756011884$o291$g1$t1756011907$j37$l0$h0',
    '_ga_S97T9P1W73': 'GS2.1.s1756011884$o7$g1$t1756011914$j30$l0$h0',
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
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.375516535.1755955110; _gid=GA1.2.1540647109.1755955110; _hjSessionUser_2705208=eyJpZCI6ImU5ODA1ZGU4LTVkMmQtNTQ1ZS04NTI4LWJiNDhlMDhmZWM0OCIsImNyZWF0ZWQiOjE3NTU5NTUxMDk2MjYsImV4aXN0aW5nIjp0cnVlfQ==; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMzk3MjMiLCJpYXQiOjE3NTU5NTUxODV9.CjXwuve1tWq6mVe_MDZ8sFZSPtzb0vOLW6QRIz0gyrNxLXeNZUUPlZmRS1JyLGgXVPm1U0CsfhQJwnSKkOtDAFM8bhU7xf8sFRaA8IsSurJEo-dJcmZtJOq3S0MKHzd_FSRDkxm59osWsvrwlr5BPEwX7DbBlYX7p1y1GE21gcIJAz1y-4rZjoKycRcG7YDqs4GeeOioxN1R4vU0bKCa6IiU1cI3uDKz9BU5gYiM5SMlW_UgLvWEL5HAU3ZCcTJ5piCcu3NdfUcX9_YfWz-EtWlrSeTshXZhqsq3hL4QgMk7HNC43iPsjtg4cFgf2XMqLlqG4z3oPGhm94Z20p1IcA; _hjSession_2705208=eyJpZCI6ImY2YmM4MzlhLTNhODMtNDYzYi04MjdjLThmZmM2OWY5YTUxNCIsImMiOjE3NTYwMTE4ODQxNDUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gat_UA-184236194-1=1; _ga=GA1.1.1939536911.1755955110; _ga_6HCL2GMXBV=GS2.1.s1756011884$o291$g1$t1756011907$j37$l0$h0; _ga_S97T9P1W73=GS2.1.s1756011884$o7$g1$t1756011914$j30$l0$h0',
}

json_data = {
    'userId': 239723,
}

response = requests.post('https://elb.hilokal.com/user-relationships/add-friend', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"userId":549568}'
#response = requests.post('https://elb.hilokal.com/user-relationships/add-friend', cookies=cookies, headers=headers, data=data)