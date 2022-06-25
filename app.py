"""
郵便番号(0287111)を入力したら
岩手県八幡平市大更が出力される

python app.py
郵便番号<ハイフンなし>は？0287111
岩手県八幡平市大更
"""
from search_address import search_address


def main():
    # num = input("郵便番号<ハイフンなし>")
    num = "0287111"

    address = search_address(num)

    print(address)


# print(dic)

if __name__ == "__main__":
    main()
