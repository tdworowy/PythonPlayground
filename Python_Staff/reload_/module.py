from imp import reload

from my_utils.randomString import generate_random_string
from Python_Staff.reload_ import changer

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