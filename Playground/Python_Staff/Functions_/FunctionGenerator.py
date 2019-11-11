def func_generator(count):
    def funA(arg):
        state = arg
        def FunB(*arg):
             nonlocal  state
             print(state,*arg)
        return  FunB
    list = []

    for i in range(count):
        list.append(funA(i))
    return list

if __name__ == "__main__":


    functions = func_generator(10)

    functions[5]("TestX")

    for x in functions:
        x("Test")