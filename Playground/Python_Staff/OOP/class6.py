class Printer():
    def print(self):
        print("Printer print")
if __name__ == '__main__':
    x =Printer()
    Printer.print(x)
    Printer.print(Printer())
    Printer.print(Printer)