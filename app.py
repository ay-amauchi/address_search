"""
郵便番号(0287111)を入力したら
岩手県八幡平市大更が出力される

python app.py
郵便番号<ハイフンなし>は？0287111
岩手県八幡平市大更
"""


import requests

# num = input("郵便番号<ハイフンなし>")
num = "0287111"

url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={num}"
responce = requests.get(url)

print(responce)

dic = responce.json()
print(dic)
