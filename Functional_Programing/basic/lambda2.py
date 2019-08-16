def echo_IMP():
    while 1:
        x = input('IMS ---')
        if x == 'quit':
            break
        else:
            print(x)


# echo_IMP()


# functional version

def echo_func():
    def identity_print(y):
        print(y)
        return y
    echo = lambda: identity_print(input('FP --- ')) == 'quit' or echo()
    echo()


echo_func()
