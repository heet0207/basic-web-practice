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