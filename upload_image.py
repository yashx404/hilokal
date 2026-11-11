import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzczMDUzNDEyfQ.Zo7sV5s1-tFn1T_S5N-Sg4TOB0HcDW4-l_m9k0US-AKvEaPhUFeI7m72ibpxDIM3yX_toMX545tcksvHS_SH2uywVEeN7BDrEW4ud-ii6LEq5dzP1LfVWJ8kudhxSpF7owmKARvDsvI-6dKRN2rah5bBraS-hK2_kOyiTJwapcOPNjlFaLgf23f72Au30xN8xHqG4ROOd38L2Qc4NXJDozxxC8yfij5jdVa6VoWd-5Hm-SdatcUVmlAXjz_hC1wmCGOexgwfib2QDsb0rjhEzt5Z692efd3yQ38FR9-dLAVH1iVghpwZkiN_BY2VcYeLAWQqChFQsoqYdZdf8PsEzg',
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
    'image': 'https://s3.ap-northeast-2.amazonaws.com/hilokal-user-uploads/image-upload-2141452-edu82yhmvpo.png',
    'imageWidth': 564,
    'imageHeight': 753,
}
response = requests.post('https://elb.hilokal.com/group-call/4021503/messages', cookies=cookies, headers=headers, json=json_data)