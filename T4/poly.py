# Polymorphism

n1=1
n2=2
print(n1+n2)

n1='Python'
n2='Programming'
print(n1+n2)

#function Polymorphism
print(len('Programmiz'))
print(len(['Python','Java','C']))
print(len({'Name':'As','Age':23}))

#class Polymorphism
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        print(f'I am Cat.My Name id {self.name}')
    
    def make_sound(self):
        print('Meow')
    
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        print(f'I am Dog.My Name id {self.name}')
    
    def make_sound(self):
        print('Bark')

cat1 =cat('Kitty',2.5)
dog1=Dog('Fluffy',4)

for a in(cat1,dog1):
    a.make_sound()
    a.info()
    a.make_sound()

# Inheritance
# Single Level Inheritance

class p:
    def house(self):
        print('Owns a House')
    def bike(self):
        print('p Owns A Bike')
class ch(p):
    def bike(self):
        print('Owns A Bike')

c=ch()
c.house()
c.bike()
p=p()
p.house()
p.bike()

class father:
    def height(self):
        print('Height Is 6.0 ft')
class Mother:
    def color(self):
        print('color is gray')
class child(father,Mother):
    pass
c=child()
c.height()
c.color()


class base:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
class child(base):
    def __init__(self, name,age):
        base.__init__(self,name)
        self.age=age
    def getage(self):
        return self.age

class grandchild(child):
    def __init__(self, name, age,address):
        child.__init__(self,name,age)
        self.address=address
    def getaddress(self):
        return self.address
g=grandchild('As',23,'Noida')
print(g.getname(),g.getage(),g.getaddress())

# Method Of Resolution On Order (MRO) C3 Linearization

class p1:
    pass
class p2:
    pass
class c1(p1,p2):
    pass
class c2(p1,p2):
    pass
class GC(c1,c2):
    pass

print(GC.__mro__)
print(GC.mro())


# Abstract Class Abstract Method & Property

from abc import ABC,abstractmethod,abstractproperty
class shape(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def draw(self):
        pass
    @abstractproperty
    def n(self):
        pass

class Circle(shape):
    def __init__(self):
        super().__init__('Circle')
    def draw(self):
        print('Draw a Circle')
    @property
    def n(self):
        return self.name

c=Circle()
c.draw()
print(c.n)
print(isinstance(c,Circle))
print(issubclass(Circle,shape))

from math import pi
class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def fact(self):
        return "I Am a 2 dimension"
    def __str__(self):
        return self.name

class square(shape):
    def __init__(self, length):
        super().__init__('Square')
        #shape.__init__(self,'Square')
        self.length=length
    def area(self):
        return self.length**2
    def fact(self):
        return 'Square Have equal Angles'

class Circle(shape):
    def __init__(self, radius):
        super().__init__('Circle')
        #shape.__init__(self,'Circle')
        self.radius=radius
    def area(self):
        return pi*self.radius**2

a=square(4)
b=Circle(7)
print(a)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
print(a.area())


# Method Overloading ❌
# def p(a,b):
#     return a*b
# def p(a,b,c):
#     return a*b*c
# p(1,2,3)
# p(4,5)


class Time:
    def __init__(self,h,m):
        self.h=h
        self.m=m
    def __add__(self,other):
        total_minutes = self.m + other.m
        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60

        total_hours = self.h + other.h + extra_hours

        return Time(total_hours, remaining_minutes)
        #return Time(self.h+other.h,self.h+other.h)
    def display(self):
        print('Hrs : ',self.h, ' min : ',self.m)

t1=Time(2,30)
t2=Time(3,35)
t3=t1+t2
t1.display()
t2.display()
t3.display()



class D:
    def __init__(self,name,author,publisher,isbn,year):
        self.name=name
        self.author=author
        self.n=len(author)
        self.publisher=publisher
        self.isbn=isbn
        self.year=year
    def display(self):
        print('Book Details : ')
        print('Name :',self.name)
        print('Authors : ')
        for author in self.author:
            print("  -", author)
        print('publisher : ',self.publisher)
        print('ISBN  :',self.isbn)
        print('Year : ',self.year)

class TB(D):
    def __init__(self, name, author, publisher, isbn, year,course):
        super().__init__(name, author, publisher, isbn, year)
        self.course=course
    def display(self):
        super().display()
        print('Course :',self.course)

authors=['John Smith','Alice Brown']
tb=TB('Data Structure',authors,'Pearson','978-81-203-XXXX',2023,'Computer Engineering')
tb.display()
    


class Staff:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Name : ',self.name)
        print('Salary :',self.salary)
    
class teach(Staff):
    def __init__(self, name, salary,Subject):
        super().__init__(name, salary)
        self.Subject=Subject
    
    def display(self):
        super().display()
        print('Subject :',self.Subject)

class non_teach(Staff):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        super().display()
        print('Department :',self.department)

t=teach('Abhi Shah',45000,'Python')

nt=non_teach('Dhruv Patel',40000,'Java')

print('Teaching Staff : ')
t.display()
print('Non-Teaching Staff : ')
nt.display()


#NumPy
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5])
arr=np.concatenate((arr1,arr2))
print(arr)

#2D
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])

arr=np.concatenate((arr1,arr2),axis=0)
arr1=np.concatenate((arr1,arr2),axis=1)
print(arr)
print(arr1)

#3D
import numpy as np
arr1=np.array([[[1,2,3]],[[4,5,6]]])
arr2=np.array([[[7,8,9]],[[10,11,12]]])
arr=np.concatenate((arr1,arr2))
arr11=np.concatenate((arr1,arr2),axis=1)
arr12=np.concatenate((arr1,arr2),axis=2)
print(arr)
print(arr11)
print(arr12)

import numpy as np
arr1=np.array([[[1,2,3],[4,5,6]]])
arr2=np.array([[[7,8,9],[10,11,12]]])
arr=np.concatenate((arr1,arr2))
arr11=np.concatenate((arr1,arr2),axis=1)
arr12=np.concatenate((arr1,arr2),axis=2)
print(arr)
print(arr11)
print(arr12)

#Searching Where
import numpy as np
arr=np.array([1,2,3,4,4,3,4])
x=np.where(arr==4)
print(x)
y=np.where(arr%2==0)
print(y)
arr=np.array([[1,2,3],[4,5,3]])
q=np.where(arr==3)
print(q)
arr1=np.array([[[5,6]],[[6,8]],[[9,6]]])
a=np.where(arr1==6)
print(a)

#random
import numpy as np
x=np.random.randint(100)
print(x)
y=np.random.rand()
print(y)
z=np.random.randint(100,size=(5))
print(z)
a=np.random.rand(5)
print(a)
b=np.random.randint(100,size=(35))
print(b)
c=np.random.rand(3,5)
print(c)
d=np.random.choice([3,5,7,9])
print(d)
e=np.random.choice([3,5,7,9],size=(3,5))
print(e)

#plot
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[9,7,4,5]
plt.plot(x,y,'D:r',linewidth=2,markersize=10)
# plt.plot(x,y,marker='D',color='b',linestyle=':',linewidth=2,markersize=10)
# plt.xlabel('Calories (KCAL)',fontsize=34,fontname='Comic Sans MS',color='brown',fontstyle='italic',fontweight='bold')
# plt.ylabel('Duration (s)',fontsize=34,fontname='Comic Sans MS',color='brown',fontweight='bold',fontstyle='italic')
f1={'fontsize':34,'fontname':'Comic Sans MS','color':'brown','fontstyle':'italic','fontweight':'bold'}
plt.xlabel('Calories (KCAL)', fontdict=f1)
plt.ylabel('Duration (s)', fontdict=f1)
plt.title('Calories vs Duration',fontdict=f1)
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Matplotlib Graph")
plt.show()

import matplotlib.pyplot as plt
y=[9,7,4,5]
plt.plot(y,'D:r',linewidth=2,markersize=10)
plt.show()

import matplotlib.pyplot as plt
help(plt.plot)

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[7,5,4,3]
plt.scatter(x,y,marker='d',color='y',s=100,alpha=0.3)
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[7,5,4,3]
y1=[4,5,6,7]
plt.scatter(x,y,marker='d',color='y',s=100,alpha=0.3)
plt.scatter(x,y1,marker='o',color='b',s=100,alpha=0.5)
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[7,5,4,3]
y1=[4,5,6,7]
x1=[3,4,5,6]
plt.scatter(x,y,marker='d',color='y',s=100,alpha=0.3)
plt.scatter(x1,y1,marker='o',color='b',s=100,alpha=0.5)
plt.show()

import matplotlib.pyplot as plt
help(plt.scatter)

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[7,5,4,3]
y1=[4,5,6,7]
x1=[3,4,5,6]
s=[50,100,200,250]
plt.scatter(x,y,marker='d',color='y',s=s,alpha=0.3)
plt.scatter(x1,y1,marker='o',color=['r','g','b','k'],s=s,alpha=0.5)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(100,size=(20))
print(x)
y=np.random.randint(100,size=(20))
color=np.random.randint(100,size=(20))
size=10*np.random.randint(100,size=(20))
plt.scatter(x,y,c=color,s=size,cmap='nipy_spectral')
plt.scatter(x,y,c=color,s=size,cmap='winter')
plt.xlabel('X axis',loc='left')
plt.ylabel('Y axis',loc='top')
plt.title('Scatter Plot')
plt.colorbar()
plt.show()


import matplotlib.pyplot as plt
x=['A','B','C']
y=[1,2,3]
plt.bar(x,y,color=['r','g','b'],width=0.2)
plt.show()

import matplotlib.pyplot as plt
x=['A','B','C']
y=[1,2,3]
plt.barh(x,y,color=['r','g','b'],height=0.2)
plt.show()

import matplotlib.pyplot as plt
x=['A','B','C']
y=[3,4,8]
plt.grid(linewidth=0.5)
plt.barh(x,y,color='burlywood',height=0.4)
plt.show()

import matplotlib.pyplot as plt
x={'A':1,'B':2,'C':3,'D':4}
a=x.keys()
b=x.values()
plt.grid()
plt.bar(a,b,color='orchid',width=0.4)
plt.show()

import matplotlib.pyplot as plt
x=[90,35,15,5]
plt.pie(x)
plt.show()

import matplotlib.pyplot as plt
x=[35,25,15,5]
plt.pie(x,labels=['A','B','C','D'],explode=[0,0.1,0.2,0.3],colors=['r','k','y','g'],autopct='%1.1f%%',shadow=True,startangle=90)
plt.legend(title='Categories',loc='best')
plt.show()


import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[9,7,4,5]
plt.plot(x,y,'D:r',linewidth=2,markersize=10)
# plt.plot(x,y,marker='D',color='b',linestyle=':',linewidth=2,markersize=10)
# plt.xlabel('Calories (KCAL)',fontsize=34,fontname='Comic Sans MS',color='brown',fontstyle='italic',fontweight='bold')
# plt.ylabel('Duration (s)',fontsize=34,fontname='Comic Sans MS',color='brown',fontweight='bold',fontstyle='italic')
f1={'fontsize':34,'fontname':'Comic Sans MS','color':'brown','fontstyle':'italic','fontweight':'bold'}
plt.xlabel('Calories (KCAL)',horizontalalignment='right')
plt.ylabel('Duration (s)', verticalalignment='top')
plt.title('Calories vs Duration',fontdict=f1)
plt.show()

import matplotlib.pyplot as plt
x = [1,2,2,2,3,3,9,5,4,4,8,8,6,7]
plt.hist(x,bins=4,color='burlywood',edgecolor='black',orientation='horizontal')
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[4,5,6,7]
plt.subplot(2,3,1)
plt.scatter(x,y)
x=[1,2,3,4]
y=[4,5,6,7]
plt.subplot(2,3,2)
plt.scatter(x,y)
x=[1,2,3,4]
y=[4,5,6,7]
plt.subplot(2,3,3)
plt.scatter(x,y)
x=[1,2,3,4]
y=[4,5,6,7]
plt.subplot(2,3,4)
plt.scatter(x,y)
x=[1,2,3,4]
y=[4,5,6,7]
plt.subplot(2,3,5)
plt.scatter(x,y)
x=[1,2,3,4]
y=[4,5,6,7]
plt.subplot(2,3,6)
plt.scatter(x,y)
plt.suptitle('Multiple Scatter Plots')
plt.show()

import random
import time

class CongestionControl:
    def __init__(self):
        self.window_size = 1
        self.max_window = 10

    def send_packets(self):
        print(f"\nSending {self.window_size} packets...")
        
        # Random congestion simulation
        congestion = random.choice([True, False, False])

        if congestion:
            print("⚠ Congestion detected!")
            self.window_size = max(1, self.window_size // 2)
        else:
            print("✅ No congestion")
            if self.window_size < self.max_window:
                self.window_size += 1

    def start(self):
        for _ in range(10):
            self.send_packets()
            time.sleep(1)

# Run simulator
cc = CongestionControl()
cc.start()



import hashlib
import time

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
        return True

# Run blockchain
bc = Blockchain()
bc.add_block("Transaction A → B ₹500")
bc.add_block("Transaction B → C ₹200")

print("Blockchain valid?", bc.validate_chain())

for block in bc.chain:
    print("\nBlock", block.index)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.prev_hash)

