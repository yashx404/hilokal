import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMDU4OTc0IiwiaWF0IjoxNzU2MDQzMDMxfQ.NWq0CPoUluesjTPkmlUM6fKqcoXhR8HB_ww1d5MaXYIsUyEUr2uuHq6jVkGfTJT9OrvuwBh8pb9TdcdnQ9Kmt-NMjWN4aSidZi6wGCeQZA2WnKDiTxEr8k2dYBjpVHCbKMX8FKgE1NgMlXTwttVMK9bEy0kKQfurneZc7bwoLYIAJLomJM3VK9n8poLli6ckLTjq2M2jx_DGzyinzOgbXPGUInU0OoNQQsiuDTPv3rS3N1yrqdUXPA4d3rLYEaVB9hufRXc9OYHZz21qe-IekA0keXzweumWARxJyIaAwGlRcKBnxkrw9Jq0qI_-W5LsClWB2rxbClJtiXCykDjwlA',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1MDc1NjUiLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzI5Mjk0NjI5fQ.jOxRX1o6SHbra7-wvnoHyEqyp9Fs_MnTmpFPY7tzIBWCMyIJxwkNTd90b_uv0XwYUwmtic7_1tHmfISE2u7S6FtI5PlJJzYKic5iVMv-zwRJmrqi05Nt7vxXzVzrDVLaVveWiCidhX16jCbqm_brUQ8jVEUfluMinhajuJBgH6_LlvwaAplFsmojmiZqjkbnhWIH8GyQe8YtK5nE6dQO91wYx7di_86kUSxVfIwuKrMIPraC2PGZpnUo__h7bGvijMeqyLTvv2fIzbmXJhy6JalzrSE8e12-Y434rn9NAm8j1gPFQkoQIEnK3-DnwwkAvfsBO1yQS_EDGuDImesutg',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}
json_data = {
    'body': '',
    'type': 'image',
    'parentId': None,
    'image': 'https://media.discordapp.net/attachments/1014472071457288222/1411356058559184956/image.png',
    'imageWidth': 564,
    'imageHeight': 753,
}
response = requests.post('https://elb.hilokal.com/group-call/5262194/messages', cookies=cookies, headers=headers, json=json_data)