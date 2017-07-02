from imp import reload

from MyUtils.randomString import generateRandomString
from Python_Staff.reload_ import changer

f = open("changer.py",'w')
f.write("""message = "{x}"
def printer():
    print(message)\n""".format(x=generateRandomString(20)))
f.flush()
reload(changer)
changer.printer()

f.write("""message2 = "{x}"
def printer2():
    print(message2)""".format(x=generateRandomString(5)))
f.flush()

reload(changer)
print(reload(changer))
changer.printer()
changer.printer2()