#抓小说
import requests
import re
import sys
from bs4 import BeautifulSoup
url = "https://www.x23qb.com/book/30298/"
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36"
}
print("正在爬取" + url+"的信息")
r = requests.get(url, headers=headers)
demo = r.text.encode("utf8").decode("utf8") # 服务器返回响应
print(demo)

soup = BeautifulSoup(demo, "html.parser")