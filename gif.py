import requests
headers = {
    'authority': 'elb.hilokal.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ODI0MjciLCJ0cmFuc2NyaXB0aW9ucyI6dHJ1ZSwiaWF0IjoxNjk3Mzc1NDM4fQ.xngJ8KnEidkyaht3_dfVacrdPTUqKrYDP_GoW7IM2fseCMKnu6D2x7dlMYSoGzS-Vq_id5Sk7dt4JVcTJOGaXYTADrGYL6qEdZledbcROcA_whpCoY2TucnKOkuM3pQizsM9qM0CjOuU4ptcz_un7mFD_dF82b4o1z0FugV0c0eDqXZo8_xM79eJzGK73f-hioe9ja9_ijVXOgx-HXwvdg-_IVD69AbybzCqnxwSJ4aQCmFuWOGKsQOGbRv4wvopdUkU0UqCpK2KA_u5ce9CWoE3aSjdUpj6cD4GYxTe9CGxdsRi1j1mf2UzASKKOeC7hy0FJ7o9GEqca9MX3GxEFw',
    'content-type': 'application/json',
    'origin': 'https://www.hilokal.com',
    'referer': 'https://www.hilokal.com/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
json_data = {
    'body': 'https://media.tenor.com/Qy2ftrUMX2AAAAAd/gmod-garry.gif',
    'type': 'gif',
    'parentId': None,
    'imageWidth': 422,
    'imageHeight': 400,
}
response = requests.post('https://elb.hilokal.com/group-call/2773673/messages', headers=headers, json=json_data)