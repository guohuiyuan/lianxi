import re

f = open("city.txt",encoding='utf8')             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法

dict1 =[]
while line:
    matchObj1 = re.search(r'}|{', line, re.M | re.I)
    if matchObj1:
        print(line , end="")

    else:
        print(line, end="")
        k = re.search((r'\S(.*)\S'), line, re.I | re.M)
        # print(k)
        print(k.group())
        j = re.search(r'\"\d\"',k.group(),re.M|re.I)
        print(j.group()[1])
        l = re.search(r'[\u4e00-\u9fa5]+',k.group(),re.I|re.M)
        print(l.group())
        dict1.append([j.group()[1],l.group()])
    line = f.readline()
print(dict1)
f.close()
dict2 = {dict1[0][0]:dict1[0][1],dict1[1][0]:dict1[1][1],dict1[2][0]:dict1[2][1]}
print(dict2)
import pandas as pd
d = pd.Series(dict2)
df=pd.DataFrame({'0':d})
print(df)
# df.to_excel('city.xls')