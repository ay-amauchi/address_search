import requests


def search_address(num):
    response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={num}")

    dic = response.json()  # パース

    pref_name = dic["results"][0]["address1"]
    city_name = dic["results"][0]["address2"]
    town_name = dic["results"][0]["address3"]

    address = f"{pref_name}{city_name}{town_name}"
    return address
