class accesscontrol:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = "age: "+str(value)
        else: raise AttributeError(key +' is not allowed')

x = accesscontrol()

x.age = 40
print(x.age)

x.name = "Test"