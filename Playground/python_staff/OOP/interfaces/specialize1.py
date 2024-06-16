class Super:
    def method(self):
        print("in super.method")

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print("in Replacer.method")


class Extender(Super):
    def method(self):
        print("Begin Extender.method")
        Super.method(self)
        print("End Extender.method")


class Provider(Super):
    def action(self):
        print("in Prowider.action")


if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print("\n" + klass.__name__ + "...")
        klass().method()
    print("\nPrivider...")
    x = Provider()
    x.delegate()
