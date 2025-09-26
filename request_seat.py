import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMDU4OTc0IiwiaWF0IjoxNzU2MDQzMDMxfQ.NWq0CPoUluesjTPkmlUM6fKqcoXhR8HB_ww1d5MaXYIsUyEUr2uuHq6jVkGfTJT9OrvuwBh8pb9TdcdnQ9Kmt-NMjWN4aSidZi6wGCeQZA2WnKDiTxEr8k2dYBjpVHCbKMX8FKgE1NgMlXTwttVMK9bEy0kKQfurneZc7bwoLYIAJLomJM3VK9n8poLli6ckLTjq2M2jx_DGzyinzOgbXPGUInU0OoNQQsiuDTPv3rS3N1yrqdUXPA4d3rLYEaVB9hufRXc9OYHZz21qe-IekA0keXzweumWARxJyIaAwGlRcKBnxkrw9Jq0qI_-W5LsClWB2rxbClJtiXCykDjwlA'
,
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.hilokal.com',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
json_data = {}
response = requests.put(
    'https://elb.hilokal.com/group-calls/5332137/seat-request', cookies=cookies, headers=headers, json=json_data,
)