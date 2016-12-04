def f(a,b,c,d): print(a,b,c,d)

args = (1,2)
args +=(3,4)

f(*args)

args = {'a':1,'b':2,'c':3,'d':4}
f(**args)