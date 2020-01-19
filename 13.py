# coding:utf-8

from bs4 import BeautifulSoup
import requests
import urllib

import pymongo
import re
import time

url = "http://tieba.baidu.com/p/2166231880"
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36"}
print("正在爬"+url)
r = requests.get(url,headers=headers)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
img_info = soup.find_all('img', class_='BDE_Image')
index =0
for index, img in enumerate(img_info, index + 1):
    print("正在下载第{}张图片".format(index))
    urllib.request.urlretrieve(img.get("src"),'D:/Program Files/pythonStudy/everyday/lianxi/picture/%s.jpg' % index)



