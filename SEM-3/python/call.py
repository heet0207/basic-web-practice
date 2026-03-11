def f(a):
    if a<4:
        b=a/(a-3)
    print(b)


try:
    f(3)
except Exception as e:
    print("Exception caught:", e)


def g(a,b):
    try:
        c=(a+b)/(a-b)
    except Exception as e:
        print("Exception caught in g:", e)
    else:
        print(c)
g(2,3)
g(3,3)


try :
    k=2/3
except Exception as e:
    print("Exception caught in main:", e)
else:
    print(k)
finally:
    print("Execution completed.")

age==-1 # type: ignore
if age<0: # type: ignore
    raise Exception('age')

class B(Exception):
    pass
l=5
if l<10:
    raise B('l is less than 10')


def f(a):
    if type(a)!=str:
        raise TypeError('a is not str')
    if (not a):
        raise ValueError('a is empty string')
    a.strip()
    if a=='':
        return True
    return False

try:
    a=123
    print('is Empty',f(a))
except TypeError as e:
    print('T Error ',e)
except ValueError as e:
    print("V Error ", e)