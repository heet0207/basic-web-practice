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