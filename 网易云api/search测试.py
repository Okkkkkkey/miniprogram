import requests
import json
url = "http://127.0.0.1:8000/search/"
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
data = {"kw":"周杰伦",
        "offset":5,
         "limit":10,
         "type":1}
rep = requests.post(url=url,headers=headers,data=data)
print(rep.text)