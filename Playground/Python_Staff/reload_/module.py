from importlib import reload

from Playground.Python_Staff.reload_ import changer
from Playground.my_utils.staff.random_string import generate_random_string

if __name__ == '__main__':
    f = open("changer.py",'w')
    f.write("""message = "{x}"
    def printer():
        print(message)\n""".format(x=generate_random_string(20)))
    f.flush()
    reload(changer)
    changer.printer()

    f.write("""message2 = "{x}"
    def printer2():
        print(message2)""".format(x=generate_random_string(5)))
    f.flush()

    reload(changer)
    print(reload(changer))
    changer.printer()
    changer.printer2()