class TestStaff:
    def __init__(self):
        self.message = "TestM"

    def prt(self):
        print(self.message)

    def generate_functions(self):
        funcs = {}
        for i in range(3):
            def fun():
                self.prt()

            funcs["Name" + str(i)] = fun
        return funcs


if __name__ == "__main__":
    x = TestStaff()
    functions = x.generate_functions()
    for fun_name in functions.keys():
        functions[fun_name]()
