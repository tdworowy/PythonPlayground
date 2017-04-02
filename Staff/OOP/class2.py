class rec : pass

rec.test="Dupa"
rec.a = 1
rec.b =2

print(rec.test)
print(rec.a+rec.b)

x = rec()
x.test2 = "Dupa2"

print(x.test2)
print(x.test)

print(rec.__dict__.keys())
print(x.__dict__.keys())