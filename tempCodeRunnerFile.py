f=open('s.txt','r',encoding='utf-8')
data=f.readlines()
for i in data:
    if i[0].isupper():
        print(i)
f.close()