import requests
import json

url = "https://zipcloud.ibsnet.co.jp/api/search"
payload = {"zipcode":"2440003"}

res = requests.get(url,params=payload)
print(res.text)
# JSON形式のres.textをpython形式に変換する.
data = json.loads(res.text)
print(data)
