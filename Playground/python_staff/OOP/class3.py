def to_upper(self):
    return self.x.upper()


class Rec: pass


if __name__ == '__main__':
    Rec.method = to_upper
    Rec.x = "Dupa"

    a = Rec()
    print(a.method())
