import pandas as pd
df = pd.DataFrame(pd.read_excel('numbers.xls'))
a = 0
for i in df['1']:
    a += int(i)
print(a)