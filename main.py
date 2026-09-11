import requests
from bs4 import BeautifulSoup

# --練習用--

# jraの公式サイト
#url = "https://www.jra.go.jp/"

# 練習用レース
url = "https://www.jra.go.jp/JRADB/accessD.html?CNAME=pw01dde0106202604031120260912/9D"

# 接続確認
response = requests.get(url, timeout=10)
#print(response.status_code)

# getしたresponseをhtmlとして解釈
soup = BeautifulSoup(response.content, "html.parser")

# 文字コード確認
#print(response.encoding)
# タイトル出力
#print(soup.title.text)

#馬の名前を抽出（最初の1匹分）
#horse = soup.find("td", class_="horse")
#print(horse)
#name = horse.find("div", class_="name")
#print(name.text)

#馬の名前を抽出（全馬分）
race_table = soup.find(id="syutsuba")
horses = race_table.find_all("td", class_="horse")

for horse in horses:
    name = horse.find("div", class_="name")

    if name is None:
        print("nameが見つからない要素:")
        print(horse)
    else:
        print(name.text)
print(len(horses))











# --練習用ここまで--