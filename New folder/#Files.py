f=open('friend_copy1.txt','r',encoding='utf-8')
data=f.readlines()
for i in data:
    if "#" not in data:
        print(i.strip())
f.close()



f=open('friend_copy1.txt','r',encoding='utf-8')
d=open('friend_no_hash.txt','w',encoding='utf-8')
while True:
    b=f.readline()
    if len(b)!=0:
        if b[0]=="#":
            continue
        else:
            if '#' in b:
                for i in range(1,len(b)):
                    if b[i]=='#':
                        d.write(b[0:i]+'\n')
            else:
                d.write(b)
    else:
        break
f.close()
d.close()



f = open("friend_copy1.txt", "r", encoding='utf-8')
s = f.readlines()
f.close()
d = open('friend_no_hash.txt', 'w', encoding='utf-8')

for i in s:
    i = i.rstrip()

    if i[0] == "#":
        continue

    if "#" in i:
        i = i.split("#")[0].rstrip()
    d.write(i + "\n")
d.close()



f = open("friend_copy1.txt", "r", encoding='utf-8')
d = open('friend.txt', 'r', encoding='utf-8')
s=f.readlines()
q=d.readlines()

for i in s:
    for j in q:
        if j!=i:
            print()
f.close()
d.close()


def sa():
    f = open("friend_copy1.txt", "r", encoding='utf-8')
    d = open('friend.txt', 'r', encoding='utf-8')
    s=f.readlines()
    q=d.readlines()
    min1=min(len(s),len(q))
    for i in range(min1):
        l1=s[i]
        l2=q[i]
        min_len=min(len(l1),len(l2))
        for j in range(min_len):
            if l1[j]!=l2[j]:
                print('Line :',i +1,'index :',j + 1)
                return
    if len(s)!=len(q):
        print('different number of lines')
    else:
        print('files are identical')
    d.close()
    f.close()
sa()


f=open('s.txt','w',encoding='utf-8')
while True:
    a=input('Enter text (type "End" to quit): ')
    if a=='End':
        break
    f.write(a+'\n')
f.close()

f=open('s.txt','r',encoding='utf-8')
data=f.readlines()
for i in data:
    if i[0].isupper():
        print(i)
f.close()