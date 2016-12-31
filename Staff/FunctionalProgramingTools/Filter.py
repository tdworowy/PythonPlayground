f= filter((lambda x : x >0),range(-20,20))
print(list(f))

f = filter((lambda x : x%2 ==0),range(100))
print(list(f))