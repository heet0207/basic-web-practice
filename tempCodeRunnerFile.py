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