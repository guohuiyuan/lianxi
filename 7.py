#
import os
import re
f = open("code/Client.java")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
zhushi = 0
daima = 0
kongge = 0
while line:
    matchObj = re.search(r'\w|}|{', line, re.M | re.I)
    matchObj1 = re.match(r'[\s| ]*\n',line,re.M|re.I)
    matchObj2 = re.search(r'/{2}|/\*|\*/',line,re.M|re.I)
    if matchObj1:
        kongge+=1
        print(1)
    if matchObj2:
        zhushi+=1
        print(2)
    if matchObj:
        daima+=1
        print(3)
    print(line, end = '')       # 在 Python 3中使用
    line = f.readline()
f.close()
print("注释有%s行,代码有%s行,空格有%s行"%(zhushi,daima,kongge))