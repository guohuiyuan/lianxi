# -*- coding:utf-8 -*-
from xml.dom import minidom
import pandas as pd
import re
df=pd.read_excel('student.xls')
doc = minidom.Document()
comment_text = doc.createComment(u"""学生信息表 "id" : [名字, 数学, 语文, 英文]""")
root_node = doc.createElement('root')
doc.appendChild(root_node)
student_node = doc.createElement('students')
root_node.appendChild(student_node)
dict1 = {'1':str(df['1'].values),'2':str(df['2'].values),'3':str(df['3'].values)}
k = re.sub(r'"','',str(dict1))
print(k)
name_text=doc.createTextNode(k)
student_node.appendChild(comment_text)
student_node.appendChild(name_text)
try:
    with open('student.xml','w',encoding='UTF-8') as fh:
        # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        doc.writexml(fh,indent='',addindent='\t',newl='\n',encoding='UTF-8')
        print('写入xml OK!')
except Exception as err:
    print('错误信息：{0}'.format(err))