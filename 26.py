#使用python将网站的图片爬下来
from bs4 import BeautifulSoup
import requests
import re
import html


url = "http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=811"
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36"
}
print("正在爬取" + url+"的信息")
r = requests.get(url, headers=headers)
demo = r.text  # 服务器返回响应
print(demo)
zhengze = ""
with open("zhengzebiaodashi.txt","r") as f:
    zhengze = f.read()
print(zhengze)
searchObj = re.search(zhengze,demo, re.M|re.I)
findallObj = re.findall(zhengze,demo,re.M|re.I)
print(findallObj)

with open("listTemp.txt","w") as f1:
    for x, y in findallObj:
        f1.write(html.unescape(x)+","+y+"\n")
# for x,y in findallObj:
#     urlTemp = "http://www.zerobyw4.com/"+html.unescape(x)
#     demoTemp = requests.get(url, headers=headers).text
#     if y is '3':
#         print(demoTemp)

