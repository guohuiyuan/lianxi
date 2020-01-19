import os
import re
from collections import Counter
with open("text/1.txt",'r') as f:
    text = f.read()
    text = text.lower()
    datalist = re.split(r'[\s\n]+', text)
    dic = Counter(datalist).most_common()
    for i in range(len(dic)):
        print('%15s  ---->   %3s' % (dic[i][0], dic[i][1]))
