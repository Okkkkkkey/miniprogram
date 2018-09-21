import re
import execjs
import urllib.request
import urllib.parse
import requests

with open("corespider.js") as f:
    data = f.read()

headers = {"Referer": "http://music.163.com/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
           }
url = "https://music.163.com/weapi/v1/resource/comments/A_PL_0_2349998506?csrf_token="

rid = "A_PL_0_2349998506"
offset = 0


params_first = '{"rid":"%s","offset":"%d","total":"false","limit":"20","csrf_token":""}'%(rid,offset)
params_second = "010001"
params_third = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
params_forth = "0CoJUm6Qyw8W8jud"

getParams = execjs.compile(data).call("d",params_first,params_second,params_third,params_forth)

fromData = {
    "params":getParams["encText"],
    "encSecKey":getParams["encSecKey"]
}
rsp = requests.post(url=url,data=fromData,headers=headers)
print(rsp.text)
#print(urllib.request.urlopen(urllib.request.Request(url=url,data=urllib.parse.urlencode(fromData).encode("utf-8"),headers=headers)).read().decode("utf-8"))