g=lambda x,y:x+y

def f(n):
    if n>1:
        return n*f(n-1)
    else:
        return 1
##print(f(5))
import functools
if __name__=="__main__":
    print(functools.reduce(lambda x,y:x*y,[1,2,3,4,5]))

def add(x,y):
    return x+y

