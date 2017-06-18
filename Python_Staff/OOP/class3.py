def toUpper(self):
    return self.x.upper()

class rec : pass

rec.method = toUpper
rec.x = "Dupa"

a = rec()
print(a.method())