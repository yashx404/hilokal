import requests
cookies = {
    '_gcl_au': '1.1.1281012474.1787123063',
    '_hjSessionUser_2705208': 'eyJpZCI6IjRjY2FkOTcyLWIxNGEtNTdkMC1iNzkwLTJiZmM2MzVhZDY4YiIsImNyZWF0ZWQiOjE3ODcxMjMwNjM1OTAsImV4aXN0aW5nIjp0cnVlfQ==',
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTQxNDUyIiwiaWF0IjoxNzg5MDE2NjE1fQ.iVEhY2NnfpmcKjemTxfkhseOV65mS4ZuXH5JQVIxDNTYhHAIE_38ruG30oKddJzN2Rs0L61AeAJuL4NFwngHKPMj7hQoAGO1VrNo-wAEE-ZrsgXudBOqOOcmskfTfYLePtTyXvma8QmWqByOnHIJgNaH-rgUPTbGptre46u8IHLmvXXqQ5ahAtTIGzTKSh3qceCpV-s3bF8QMmEnD-g-owar0Idtg6RX_BiAsRyYdvRkco5GyzagViEasq7XGqmgAJb_SlWa0azVYSdGgzlDXvdWIP54HApTg5sAlT1cztkOpr2k9AAmPAg0zZJbvoYH6FBURDGgpVzdJ1SASq09ow',
    '_gid': 'GA1.2.416255240.1789533746',
    '_hjSession_2705208': 'eyJpZCI6IjhkODVmYTNkLTAyMzEtNDFlOS04ZTE3LTNiMGEwNzFiNjBkMiIsImMiOjE3ODk2MjA3Mjk3ODQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_ga': 'GA1.1.118388267.1787123063',
    '_ga_S97T9P1W73': 'GS2.1.s1789620729$o58$g1$t1789621810$j52$l0$h0',
    '_ga_6HCL2GMXBV': 'GS2.1.s1789620729$o57$g1$t1789621810$j52$l0$h0',
}
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
    }
json_data = {
    'topic': 'Working',
    #'description': '',
    'transcriptionLang': 'en',
    'targetLevel': 4,
    #'visibility': 'public',
    'allowReview': False,
    #'allowPaid': False,
    #'participantLimit': 8,
    #'price': 2,
    "shareCount": 69,
    "acceptSpeakerRequests": True,
    "groupChatAccess": "speaker",
}
response = requests.put('https://elb.hilokal.com/group-call/5996784',cookies=cookies,headers=headers,json=json_data,verify=False,)