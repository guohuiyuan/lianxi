
with open("filtered_words.txt",'r',encoding='UTF-8') as f:
    list = f.read().split('\n')
    print(list)
str = input("Enter your input: ")

print ("Received input is : ", str)
import re
k='|'.join(list)
print(k)
matchObj = re.search(k,str,re.I|re.M)
if matchObj:
    print("Human Rights")
else:
    print("Freedom")
matchObj1 = re.sub(k,'***',str)
print(matchObj1)

