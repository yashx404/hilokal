import requests
headers = {
    'authority': 'elb.hilokal.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDc5NTYzIiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTc1MzQ1NTY3M30.OfS2tJUyxIwiHaDEoEc9kQFUaaLgYInMz6n8KNcNxpDlvFH_yojVgwSCn-0oNlwQAeiGErg5q4gx-pv7Cin15RiAqD5TOrlR659qrJnZV2_IJpH_PgcK8feMh-OUXZfphUxsRjfOvYUTpXIU3TShJJSAVyiMmTYktR8dDlg9V4bI1QChJ70Y6kwNsv0D4wYCzkyDNm_CQurJtApZjdukulJ_PPLX7TnKfGh8lzOyzVPzZxEwDRGmDSj1tBYYD5-AVvW_XTS8-G6AzpZav5hrNrK6FTDPOGwJv4ZvPiKE05E0YDTPFI50V1QPTROaoAZYGm4WqC9fsmqHMDz842KOww',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
json_data = {
    #"countryCode": '',
    #"nativeChangingCount": 1,
    #"birthdayChangingCount": 1,
    #"targetLang": '',
    #"email": 'ibrahimovicanesa7@gmail.com',
    #"bio": 'Empty',
    #"name": 'Juliana',
    #'profileImageUrl': 'https://s3.ap-northeast-2.amazonaws.com/hilokal-user-uploads/image-upload-2058974-b4ynmkwhuhs.jpeg',
}
response = requests.put('https://elb.hilokal.com/users/me', headers=headers, json=json_data)
#juli: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5MzcyMzEiLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNzUyMDgzMjYzfQ.Yc4sVhwsgBw_scRBS92uozkIPyeUWP81gZiJNoMTtb-Tr8c6fWKheznsuBAN8-TPGSxLiCZVh7N3kPhuauDw-FbNbILChKclioF1jzMIPAQPd0ZDdOBUpCJ3v8knxH9KAAFI47JFNUU1kwWHByIfsGY95ZUFvAZgyh8bMwExID4jJRW8eN0EcXbeuG-0T_58QtosQC53i26fTpgjmrR2QFEdu0o7WEdIjmj9YPf6OFFLJfNXclx22pdPJ2l3dATHWsmoQ1TROmXaCD3F7O-2Daz5eiH8xQihmVU8Pv0SB1epIbGis0u2qYov967T0UL2-f5kA2osew_hnul2SFgiAg
#anesa: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDc5NTYzIiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTc1MzQ1NTY3M30.OfS2tJUyxIwiHaDEoEc9kQFUaaLgYInMz6n8KNcNxpDlvFH_yojVgwSCn-0oNlwQAeiGErg5q4gx-pv7Cin15RiAqD5TOrlR659qrJnZV2_IJpH_PgcK8feMh-OUXZfphUxsRjfOvYUTpXIU3TShJJSAVyiMmTYktR8dDlg9V4bI1QChJ70Y6kwNsv0D4wYCzkyDNm_CQurJtApZjdukulJ_PPLX7TnKfGh8lzOyzVPzZxEwDRGmDSj1tBYYD5-AVvW_XTS8-G6AzpZav5hrNrK6FTDPOGwJv4ZvPiKE05E0YDTPFI50V1QPTROaoAZYGm4WqC9fsmqHMDz842KOww
#protons: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMTIzMTE5IiwidHJhbnNjcmlwdGlvbnMiOnRydWUsImlhdCI6MTc1MzQ1Njk3NH0.j3ehNZB0JKQVAXxfoY4WkqAkjMoqJdJVsIO_oFJBqPtRBlqLWJzjLP5InZz9h0ER0gbiHl-igRlohFXJR6ekflS0WJau3YxfaEuiWHWUoZo6kYcpr9g5z1OJZG8Gd5Ru4PWyyJWK3mbF1nN3z_OTnVs7UQBbAvksVy0BfLys4mAMVYrJn8dpsNIvnFOF0SGKmNYJJkHatEymHvkE37VYh3wxy75pMMfCM1mRpNfgmxBt8R7nLww3XYlX2sUZHrtV4nFWzVpL6ftWolWlhUHs7yAUzBULS6y4ZjHsOLfsih_YOATN4z4-umurALglL1FA9w2pOc9B65Yq1Q1iuBW_GQ
#mitchy: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxODgwMTQyIiwiaWF0IjoxNzU2MzIxOTEwfQ.bqwCGHaz14ZUzT9aSHNWOGfZQx1m8csUhRyPY4jzmk-UCz1chhERTDFi0wfKUlbxaCWSz8qJExiRdYq5QhB4N3460DRbgcuGLqQU-2Q1pd_GdTZ2LbZoxPxLue2OK7tgtkufS-m4fk0a9ppYGJtsKx-bN1QlpolxyPgOWysa99eCSTqjzHoWwMGDvNAn4k4dCTL_P4BsPRaao5YGU56AeAakkyvLGywdtI0R3MKbAzu_HTTS1re2zsJB0pyyThYHHG3Xio7WzoBGxBmLnKhApMJo6D9V7kh_BPMZqlsjeiE2TgLro3964dDKJPy7UVinL-EoCdNXWGXR_Je42-vGRQ