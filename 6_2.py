import os
import re
from collections import Counter
path = "text"
alltext = os.listdir(path)
count=1
for text in alltext:

    with open("text/"+text, 'r') as f:
        text = f.read()
        text = text.lower()
        datalist = re.split(r'[\s\n]+', text)
        dic = Counter(datalist).most_common()
        print("第%s个文本最重要的单词有%s,%s,%s,%s,%s"%(count,dic[0][0],dic[1][0],dic[2][0],dic[3][0],dic[4][0]))
    count+=1
