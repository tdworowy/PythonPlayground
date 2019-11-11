def toUpper(self):
    return self.x.upper()

class rec : pass

if __name__ == '__main__':
    rec.method = toUpper
    rec.x = "Dupa"

    a = rec()
    print(a.method())