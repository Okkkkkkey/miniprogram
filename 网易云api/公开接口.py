import requests

data = {'kw':'李志',
       'offset':'5',
        'limit':'10',
       'type':'1'}

search_api = "http://127.0.0.1:8000/search/"
rsp = requests.post(url=search_api,data=data)
print(rsp.text)