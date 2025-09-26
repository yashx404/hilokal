import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMDU4OTc0IiwiaWF0IjoxNzU2MDQzMDMxfQ.NWq0CPoUluesjTPkmlUM6fKqcoXhR8HB_ww1d5MaXYIsUyEUr2uuHq6jVkGfTJT9OrvuwBh8pb9TdcdnQ9Kmt-NMjWN4aSidZi6wGCeQZA2WnKDiTxEr8k2dYBjpVHCbKMX8FKgE1NgMlXTwttVMK9bEy0kKQfurneZc7bwoLYIAJLomJM3VK9n8poLli6ckLTjq2M2jx_DGzyinzOgbXPGUInU0OoNQQsiuDTPv3rS3N1yrqdUXPA4d3rLYEaVB9hufRXc9OYHZz21qe-IekA0keXzweumWARxJyIaAwGlRcKBnxkrw9Jq0qI_-W5LsClWB2rxbClJtiXCykDjwlA',
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
    #'name': 'ㅤㅤㅤㅤ',
    #'nativeLang': 'en',
    #'birthdayChangingCount': 1,
    'targetLang': '',
    #'targetLangLevel': '1',
    #'languageLevel': '2',
    #'countryCode': '',
    #'profileImageUrl': 'https://s3.ap-northeast-2.amazonaws.com/hilokal-user-uploads/image-upload-507565-8bfzsdx2tkj.jpeg',
    #'bio': 'I got everything I wanted\nthen I think of you',
}
response = requests.put('https://elb.hilokal.com/users/me', cookies=cookies, headers=headers, json=json_data)