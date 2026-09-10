# サイトアクセスのため
import requests
# htmlを読み込ませるため
from bs4 import BeautifulSoup

# jraの公式サイト
url = "https://www.jra.go.jp/"

# 接続確認
response = requests.get(url, timeout=10)
#print(response.status_code)

# getしたresponseをhtmlとして解釈
soup = BeautifulSoup(response.content, "html.parser")
# 文字コード確認
#print(response.encoding)
#print(soup.title.text)

