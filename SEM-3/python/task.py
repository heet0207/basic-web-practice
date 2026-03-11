def cust_data():
    f=open('customer.txt','w+')
    n=input("Enter customer Name: ")
    a=input("Enter customer Age: ")
    f.write('Customer Name : '+ n + "\n"+'Age :'+ a + "\n")
    f.seek(0)
    print(f.read())
    f.close()
cust_data()



def city_data():
    f=open('City.txt','r')
    print(f.read())
    f.close()
city_data()


def count_lines():
    f=open('friend.txt','r')
    lines=f.readlines()
    print("Number of lines in the file:", len(lines))
    f.close()
count_lines()



def count_oddLines():
    f=open('friend.txt', 'r')
    for i, line in enumerate(f, start=1):
        if i% 2 != 0:
            print(line)
    f.close()
count_oddLines()

def count_odd():
    f=open('friend.txt','r')
    lines=1
    for i in f:
        if lines % 2 != 0:
            print("odd line:", i.strip())
        lines += 1
    f.close()
count_odd()

def upp():
    f=open('friend.txt','r')
    c=f.read()
    print(c.upper())
    f.close()
upp()

def print_noofword():
    f=open('friend.txt','r')
    c=f.read()
    words=c.split()
    print("Number of words in the file:", len(words))
    f.close()
print_noofword()

def print_noofstatment():
    f=open('friend.txt','r')
    c=f.read()
    statements=c.split('.')
    print("Number of statements in the file:", len(statements) - 1)
    f.close()
print_noofstatment()

def file_transfer():
    f1=open('friend.txt','r')
    f2=open('friend_copy.txt','w')
    content=f1.read()
    f2.write(content)
    f1.close()
    f2.close()
file_transfer()

def file_transfer1():
    f=open('friend.txt','r')
    f1=open('friend_copy.txt','r')
    f2=open('friend_copy1.txt','w')
    c=f.read()
    c1=f1.read()
    f2.write(c+'\n'+'\n'+c1)
    f.close()
    f1.close()
    f2.close()
file_transfer1()



def search_word(word):
    f=open('friend.txt','r')
    content=f.read()
    if word in content:
        print(f'The word "{word}" is found in the file.')
    else:
        print(f'The word "{word}" is not found in the file.')
    f.close()
search_word('are')