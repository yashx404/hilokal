import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMDU4OTc0IiwiaWF0IjoxNzU2MDQzMDMxfQ.NWq0CPoUluesjTPkmlUM6fKqcoXhR8HB_ww1d5MaXYIsUyEUr2uuHq6jVkGfTJT9OrvuwBh8pb9TdcdnQ9Kmt-NMjWN4aSidZi6wGCeQZA2WnKDiTxEr8k2dYBjpVHCbKMX8FKgE1NgMlXTwttVMK9bEy0kKQfurneZc7bwoLYIAJLomJM3VK9n8poLli6ckLTjq2M2jx_DGzyinzOgbXPGUInU0OoNQQsiuDTPv3rS3N1yrqdUXPA4d3rLYEaVB9hufRXc9OYHZz21qe-IekA0keXzweumWARxJyIaAwGlRcKBnxkrw9Jq0qI_-W5LsClWB2rxbClJtiXCykDjwlA',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1MDc1NjUiLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzI3NjUyNDUzfQ.l3FFUqItMfkks7vg2b1PPv7q0mEaBIVvmQ5W04L8knO_22p9WF8-Ixe0WszJtPbpcqnpV26q0lrJDiCreGaz-_PkeAS9xLYpCUThTVYUpQXPvMvSJr9IPxdM9E5LhWLEvLlLazJ0RyQCsuZLq9hJdOH5xzOjiIyvI7USzs6zht2o_csE8hl2zg_aKUgSKNo_wShy1S5bA0LiuiKNFcxd2MNHtwWDz-Ft_zT3lSwG-F4z2COqHOUcIquSdNa0Sci8eEOAwID2drjgLjDtG-oQVF8M5wpwcadgVl9pO9kEmus58txj2JcLYsPP6AuOONeUvNTaVZLtGHjE5bZSDotlPw',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}
json_data = {
    'invitedUserIds': [
        1754516,
    ],
}
# while True:
response = requests.post('https://elb.hilokal.com/group-call/4386204/invitation', cookies=cookies, headers=headers, json=json_data)
# time.sleep(1)