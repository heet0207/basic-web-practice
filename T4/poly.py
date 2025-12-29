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

