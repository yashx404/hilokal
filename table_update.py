import requests

cookies = {
    'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDc5NTYzIiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTc1MzQ1NTY3M30.OfS2tJUyxIwiHaDEoEc9kQFUaaLgYInMz6n8KNcNxpDlvFH_yojVgwSCn-0oNlwQAeiGErg5q4gx-pv7Cin15RiAqD5TOrlR659qrJnZV2_IJpH_PgcK8feMh-OUXZfphUxsRjfOvYUTpXIU3TShJJSAVyiMmTYktR8dDlg9V4bI1QChJ70Y6kwNsv0D4wYCzkyDNm_CQurJtApZjdukulJ_PPLX7TnKfGh8lzOyzVPzZxEwDRGmDSj1tBYYD5-AVvW_XTS8-G6AzpZav5hrNrK6FTDPOGwJv4ZvPiKE05E0YDTPFI50V1QPTROaoAZYGm4WqC9fsmqHMDz842KOww',
}

headers = {
    'Host': 'elb.hilokal.com',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjAyOTciLCJpYXQiOjE3NTg1NTc2Mzh9.qpIQ8Adet5POwEf_wNN_wwPHgrFk-0MPKnf3B-xzEnWbBi5OyqARZm55Ltt8Ul-VXNd2FiEBelq5vQkt4hz_Qawb6CU67-f6_3bbrmp8ArSIQ-xYJ4lW-wOv_oFZj9b2Q0WhhQwHXlywxQMTCB3KRsNudSXL2Y9tcEqFP04DQjZHuRc9AnBOgaAduTFhxieJw8RR59Y-hjWycmRWWbD-zbbTBM-awGu6k7j-RmvSMJmY2k7L62Tbj7JcubTghrf14mpQ8rOFKsgi3K2yX_pH3yzTkE0t5lpfPkrhaQUUKdjdmCYeXK7niCVzY7uswzcirwGAFZGwyFQmdsnZgxPs8A',
    'User-Agent': 'hilokal-consumer',
    'Sentry-Trace': '5ee63914428948ca8d218cc6d374978c-90235ade9fa09ad3',
    'Baggage': 'sentry-environment=production,sentry-public_key=af8f1acc78914590800392f7ab678595,sentry-trace_id=5ee63914428948ca8d218cc6d374978c',
    'Content-Type': 'application/json',
    # 'Content-Length': '181',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Cookie': 'jwt=undefined',
}

json_data = {
    #'topic': 'for a while',
    #'description': '',
    'transcriptionLang': 'ru',
    #'targetLevel': 0,
    #'visibility': 'public',
    #'allowReview': True,
    #'allowPaid': False,
    'participantLimit': 2,
    'price': 2,
    #"shareCount": 69,
    #"acceptSpeakerRequests": False,
    "groupChatAccess": "speaker",
}
while True:
    response = requests.put(
    'https://elb.hilokal.com/group-call/5360544',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
    )
time.sleep(1)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"topic":"heeeeeeeeeeeeeeeeeee","description":"","transcriptionLang":"ru","targetLevel":0,"visibility":"private","allowReview":true,"allowPaid":false,"participantLimit":7,"price":0}'
#response = requests.put('https://elb.hilokal.com/group-call/5352079', cookies=cookies, headers=headers, data=data, verify=False)