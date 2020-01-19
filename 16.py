import re

f = open("numbers.txt",encoding='utf8')             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法

dict1 =[]

while line:
    matchObj1 = re.match(r'\[|\]', line, re.M | re.I)
    if matchObj1:
        print(line , end="")
    else:
        print(line, end="")
        k = re.finditer((r'\d+'), line, re.I | re.M)
        # print(k)
        list1 = []
        for match in k:
            list1.append(match.group())
            print(match.group())
        dict1.append(list1)
    line = f.readline()
print(dict1)
f.close()
import pandas as pd
dict2 = {'1':dict1[0],'2':dict1[1],'3':dict1[2]}
print(dict2)


df=pd.DataFrame(dict2)
print(df)
df.to_excel('numbers.xls')