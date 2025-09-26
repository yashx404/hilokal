import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMTIzMTE5IiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTcyODkyMjkxN30.pa64v0v9FnIre807xu6TXfXFjZ-CmFwohofrR5QNpOlLWWqXFj0Q0WRfhGAQ407xpG68paAU7OYZZlXe1_fNxlQDXjXKhY2BzjFNUZvQoGNgqEuGhrCTP0Rt6QGUDwBp-FzI80aiB50ydYQ99VMArDBnsnPR-8d8_ycOxiWkD3BWsqY1orudbxB2Z9dQigvcMidAge56S79R0PqEahJnz_Y18ym5U29OmK84XcZtUcSB3bOu93_jjMFYkVl-74PKBtfd4GwVw6egiai5roh2oF0coibwrVmKRPGttxkBs7NVcUBSkLf0YaW67vvg4HpRZ3mngIj5iqpcOHkDxztGQg',
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
    'roomId': '4033f2c3-e8d5-4541-becc-0a12832086f6',
    'body': '.',
    'parentId': None,
    'type': None,
    'messageType': 'text',
    'voiceMessageUrl': None,
}
response = requests.post(
    'https://elb.hilokal.com/direct-messages/room/4033f2c3-e8d5-4541-becc-0a12832086f6/messages',
    cookies=cookies,
    headers=headers,
    json=json_data,
)