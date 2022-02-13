import requests

url = "https://zipcloud.ibsnet.co.jp/api/search"
payload = {"zipcode":"2440003"}

res = requests.get(url,params=payload)
print(res.text)

res2 = requests.get(url+"?zipcode=2440003")
print(res2.text)
