import  math
x=10
y=4
d=math.sqrt(x**2 + y**2)
r=5.0
area=math.floor(math.pi * r**2)
print(area)

from math import floor, sqrt
x=5.2
y=2.4
d=floor(sqrt(x**2 + y**2))
print(d)


from math import *
x=5.2
y=2.4
d=floor(sqrt(x**2 + y**2))
print(d)

from datetime import date
today=date.today()
print(today)

from datetime import date
d=date(2020, 12,5)
print(d)

from datetime import time
t=time(20,30,35)
print(t)

from datetime import datetime
n=datetime.now()
print(n)

import os
p=os.getcwd()
print(p)

import os
p=os.listdir()
print(p)

import os
s=os.mkdir("D:/py")
print(os.getcwd())

import os
p=os.chdir("D:/py")
print(os.getcwd())

import os
p=os.rmdir("D:/py")
print(os.getcwd())

import os
print(os.listdir())

import os
f='friend.txt'
l='D:/Web Dev/practice/'
p=os.path.join(l,f)
os.remove(p)

