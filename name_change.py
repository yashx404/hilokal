import requests
cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzczMDUzNDEyfQ.Zo7sV5s1-tFn1T_S5N-Sg4TOB0HcDW4-l_m9k0US-AKvEaPhUFeI7m72ibpxDIM3yX_toMX545tcksvHS_SH2uywVEeN7BDrEW4ud-ii6LEq5dzP1LfVWJ8kudhxSpF7owmKARvDsvI-6dKRN2rah5bBraS-hK2_kOyiTJwapcOPNjlFaLgf23f72Au30xN8xHqG4ROOd38L2Qc4NXJDozxxC8yfij5jdVa6VoWd-5Hm-SdatcUVmlAXjz_hC1wmCGOexgwfib2QDsb0rjhEzt5Z692efd3yQ38FR9-dLAVH1iVghpwZkiN_BY2VcYeLAWQqChFQsoqYdZdf8PsEzg',
}
headers = {
    'authority': 'elb.hilokal.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www..com/',
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
    #'targetLang': '',
    #'targetLangLevel': '1',
    #'languageLevel': '2',
    'countryCode': '',
    #'profileImageUrl': 'https://s3.ap-northeast-2.amazonaws.com/hilokal-user-uploads/image-upload-507565-8bfzsdx2tkj.jpeg',
    #'profileImageUrl': 'https://s3.ap-northeast-2.amazonaws.com/hilokal-user-uploads/image-upload-2141452-iuhp13gv68.png',
    #'bio': '',
}
response = requests.put('https://elb.hilokal.com/users/me', cookies=cookies, headers=headers, json=json_data)