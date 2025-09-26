import requests

cookies = {
    '_hjSessionUser_2705208': 'eyJpZCI6IjdlZTUyNDRiLWMwMTktNTdhZC1hZTgxLTBmNDEyMTcwMjMzNSIsImNyZWF0ZWQiOjE3NTYwNDM3NTAyNzAsImV4aXN0aW5nIjp0cnVlfQ==',
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDc5NTYzIiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTc1MzQ1NTY3M30.OfS2tJUyxIwiHaDEoEc9kQFUaaLgYInMz6n8KNcNxpDlvFH_yojVgwSCn-0oNlwQAeiGErg5q4gx-pv7Cin15RiAqD5TOrlR659qrJnZV2_IJpH_PgcK8feMh-OUXZfphUxsRjfOvYUTpXIU3TShJJSAVyiMmTYktR8dDlg9V4bI1QChJ70Y6kwNsv0D4wYCzkyDNm_CQurJtApZjdukulJ_PPLX7TnKfGh8lzOyzVPzZxEwDRGmDSj1tBYYD5-AVvW_XTS8-G6AzpZav5hrNrK6FTDPOGwJv4ZvPiKE05E0YDTPFI50V1QPTROaoAZYGm4WqC9fsmqHMDz842KOww',
    '_ga': 'GA1.1.1367245081.1756042971',
    '__gads': 'ID=eded4002ba3dc0c8:T=1756043799:RT=1756044632:S=ALNI_MYDCOW1q2hwU0wV2dzaj8IaEJbJIQ',
    '__gpi': 'UID=0000118571550dd1:T=1756043799:RT=1756044632:S=ALNI_MayaYzVKlXD_wdDH6Y8qtGjIvQfAw',
    '__eoi': 'ID=b4e687cbf17c5c29:T=1756043799:RT=1756044632:S=AA-AfjaKydIwmCI0r1FtabbiTp-Q',
    '_ga_S97T9P1W73': 'GS2.1.s1756042970$o1$g1$t1756044798$j11$l0$h0',
    '_ga_6HCL2GMXBV': 'GS2.1.s1756042971$o1$g1$t1756044798$j11$l0$h0',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': '_hjSessionUser_2705208=eyJpZCI6IjdlZTUyNDRiLWMwMTktNTdhZC1hZTgxLTBmNDEyMTcwMjMzNSIsImNyZWF0ZWQiOjE3NTYwNDM3NTAyNzAsImV4aXN0aW5nIjp0cnVlfQ==; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMDU4OTc0IiwiaWF0IjoxNzU2MDQzODMxfQ.bVcXNfnf8q1PKNXmnqSs3PrAZ2h8JpGahx2YSzOHEozL79Z_04OZKFjXHwhXhwm0yfWCpg7H6Js-t8EBGUoQj9SCCR-G8g4uiAU25QPccf2VoQ5cl5kIw0egGoA2jkx6AkWdi79kaRRG-pZHFcEV6ICrh_VszwROQcxC0izrFk0zjfvPldr6gjiQXk5V8TiMn0m7mOmCEXLvkoU8FPFOr9QoLaqrsfK-Z984H6VJJvdei6Pv4I1YsLPT9qS7B8pe1v3xb5XrLUffTNMJQHHUgJ2LJ8-RZCItIBxY6jd74IGy9U3sykz_8QCr0cycMZE6qqMAvHbs9rdgrBfLytTCpQ; _ga=GA1.1.1367245081.1756042971; __gads=ID=eded4002ba3dc0c8:T=1756043799:RT=1756044632:S=ALNI_MYDCOW1q2hwU0wV2dzaj8IaEJbJIQ; __gpi=UID=0000118571550dd1:T=1756043799:RT=1756044632:S=ALNI_MayaYzVKlXD_wdDH6Y8qtGjIvQfAw; __eoi=ID=b4e687cbf17c5c29:T=1756043799:RT=1756044632:S=AA-AfjaKydIwmCI0r1FtabbiTp-Q; _ga_S97T9P1W73=GS2.1.s1756042970$o1$g1$t1756044798$j11$l0$h0; _ga_6HCL2GMXBV=GS2.1.s1756042971$o1$g1$t1756044798$j11$l0$h0',
}

json_data = {
    'type': 'image',
    'body': None,
    'imageUrl': 'https://s3.ap-northeast-2.amazonaws.com/hilokal-user-uploads/image-upload-1413322-p66xcr5gc6d.png',
    'imageWidth': 663,
    'imageHeight': 379,
    'userId': 1079563,
    'sourceType': 'group-chat',
    'sourceId': 142616891,
    'libraryId': None,
}

while True:
    response = requests.post('https://elb.hilokal.com/group-calls/4323408/pins', cookies=cookies, headers=headers, json=json_data)
time.sleep(1)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"type":"text","body":"Bb zella","imageUrl":null,"imageWidth":null,"imageHeight":null,"userId":453695,"sourceType":"group-chat","sourceId":141254298,"libraryId":null}'
#response = requests.post('https://elb.hilokal.com/group-calls/5138970/pins', cookies=cookies, headers=headers, data=data)