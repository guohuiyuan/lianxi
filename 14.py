import re

f = open("student.txt",encoding='utf8')             # 返回一个文件对象
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
        l = re.search(r'\[(.*)\]',k.group(),re.I|re.M)
        print(l.group())
        list1 = re.sub('\"','',l.group()[1:len(l.group())-1]).split(',')
        print(list1)
        dict1.append([j.group()[1],re.sub('\"','',l.group()[1:len(l.group())-1]).split(',')])
    line = f.readline()
print(dict1)
f.close()
dict2 = {dict1[0][0]:dict1[0][1],dict1[1][0]:dict1[1][1],dict1[2][0]:dict1[2][1]}
print(dict2)
import pandas as pd
df = pd.DataFrame(dict2)

# df.to_excel("student.xls")
print(df.head(1)['1'])
