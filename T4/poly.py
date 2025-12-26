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
