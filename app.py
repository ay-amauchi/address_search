import requests

responce = requests.get("http://zipcloud.ibsnet.co.jp/doc/api")

print(responce)
print(responce.text)
