import requests
cookies = {
    '_gcl_au': '1.1.1281012474.1787123063',
    '_hjSessionUser_2705208': 'eyJpZCI6IjRjY2FkOTcyLWIxNGEtNTdkMC1iNzkwLTJiZmM2MzVhZDY4YiIsImNyZWF0ZWQiOjE3ODcxMjMwNjM1OTAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.2.1472681391.1791176496',
    '_hjSession_2705208': 'eyJpZCI6IjFiNWEzMDVhLTAxNWQtNGVhMS05MmJkLTFmYjdiNjk4ZWVlNiIsImMiOjE3OTE0NDA1ODc4MzMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5MzcyMzEiLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzUyMDgzMjYzfQ.Yc4sVhwsgBw_scRBS92uozkIPyeUWP81gZiJNoMTtb-Tr8c6fWKheznsuBAN8-TPGSxLiCZVh7N3kPhuauDw-FbNbILChKclioF1jzMIPAQPd0ZDdOBUpCJ3v8knxH9KAAFI47JFNUU1kwWHByIfsGY95ZUFvAZgyh8bMwExID4jJRW8eN0EcXbeuG-0T_58QtosQC53i26fTpgjmrR2QFEdu0o7WEdIjmj9YPf6OFFLJfNXclx22pdPJ2l3dATHWsmoQ1TROmXaCD3F7O-2Daz5eiH8xQihmVU8Pv0SB1epIbGis0u2qYov967T0UL2-f5kA2osew_hnul2SFgiAg',
    '_ga': 'GA1.1.118388267.1787123063',
    '_ga_S97T9P1W73': 'GS2.1.s1791440587$o113$g1$t1791443220$j37$l0$h0',
    '_ga_6HCL2GMXBV': 'GS2.1.s1791440588$o112$g1$t1791443220$j37$l0$h0',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Chromium";v="154", "Google Chrome";v="154", "Not A(Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36',
}
json_data = {
    'body': '.',
    'type': 'text',
    'parentId': None,
    'image': None,
}
response = requests.post('https://elb.hilokal.com/group-call/4369277/messages', cookies=cookies, headers=headers, json=json_data)