import requests
import json
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_516392300?csrf_token="
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
data = {'encSecKey':'9a4ae3c30b4fe5d8a8892221b6eb676342ce2c2204093449e86c45b025d8bff59e3fcb76c91add60a51719fcd5d26192f91e8811c0f5352aa67493c9bbdf2ec1ef99976ddbea7acbc3f72333d5fbf26f4588f39647c6fb887d163d31c8fc40b631c9720af82de1fd9dd197e96c542371f40b3f56bf654029f6e8d11fa2e02834',
   'params':'kRMjFYvFlBlJunFVCcQ1ET7vpQWWjLa%2BZvgmBcFwGOvTJS1lbbOgMlLo53r1YEDSz%2FPqdxm6yICuf0V0Fr92emqDCLmc8rH%2BvVqlQtZG6q0x%2FGiK%2BQdHgi%2BQXhZLJt9XGSmf%2FjEtYERLQfnDNqsXCEhW%2Bnu73L7whKJLdrw0yBpddf5hdbqTlquQ6ID8gAGt'}
rep = requests.post(url=url,headers=headers,data=data)
rep.raise_for_status()
print(type(rep.text))
rep_dict = json.loads(rep.text)
print(rep_dict)