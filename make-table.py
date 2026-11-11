import requests
chief = "lovely"
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzgwMDMyOTQ0fQ.gRDP6RbuLRZx5wVv81uOQ-s8O_Oe5LFLKBCHMavrOs2ybBL71z4Bkk9FNxHdnY8F2xLHD28IZF8sJ6b2At1wJx7uwwuVoOE_GYv60vu5TTouU2Nv24RLYZ-aEhWn9O7fofTN8i4u4p7f52--mcszAEC3OTmSKfafgA3n9jDwMpeoa-IOVxGJLfiRnTkB3jXlNjnF6AxA5e3z9E5rtVZfqA7fbwcb5dWEb0cSTq460Ide_T0ntXoDgwiXsQOU1XrIDRovX2F3YePnafWTjxOgUIdBP9Y1lmKK6UkzBSHvxSTIYt6Nb3ukCux9VAeirScHtGoD9GsT2eR-yjHkOj8BBA',
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
    'transcriptionLang': chief,
    'topic': 'testttt',
    'targetLevel': 1,
    'invitedUserIds': [],
    'subscriberIds': [],
    'description': '',
    'visibility': 'private',
    'allowReview': False,
}
response = requests.post('https://elb.hilokal.com/group-calls', cookies=cookies, headers=headers, json=json_data)