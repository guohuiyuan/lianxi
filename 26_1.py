import requests
import re
from bs4 import BeautifulSoup
import urllib
import time
import os
list1 = []
with open("listTemp.txt","r") as f:
    text = f.readlines()
    for i in text:
        list1.append(re.sub("\n","",i).split(','))
print(list1[0][0])
def search(a):
    urlTemp = "http://www.zerobyw4.com/" + re.sub("\./", "", a)
    print(urlTemp)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36"
    }

    print("正在爬取" + urlTemp + "的信息")
    r = requests.get(urlTemp, headers=headers)
    demo = r.text  # 服务器返回响应
    print(demo)
    list2 = []
    soup = BeautifulSoup(demo, "html.parser")
    for i in soup.find_all('img'):
        print(i.get("src"))
        searchObj = re.search(r"(/[a-zA-Z]+/\d+)/\d+\.jpg$", i.get("src"), re.I | re.M)
        if searchObj:
            if not os.path.exists('D:/Program Files/pythonStudy/lianxi/picture' + searchObj.group(1)):
                os.makedirs('D:/Program Files/pythonStudy/lianxi/picture' + searchObj.group(1))
            print(searchObj.group(1))
            list2.append([i.get("src"), searchObj.group()])
        else:
            print("无匹配")
    print(list2)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36')]

    urllib.request.install_opener(opener)
    for x, y in list2:
        print("正在查看"+'D:/Program Files/pythonStudy/lianxi/picture' + y+"是否存在")
        if not os.path.exists('D:/Program Files/pythonStudy/lianxi/picture' + y):
            urllib.request.urlretrieve(x, 'D:/Program Files/pythonStudy/lianxi/picture' + y)
            print("正在下载" + x)
            time.sleep(0.2)

search(list1[0][0])