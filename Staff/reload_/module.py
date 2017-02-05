from imp import reload

from Staff.myUtils.randomString import randomString
from Staff.reload_ import changer

f = open("changer.py",'w')
f.write("""message = "{x}"
def printer():
    print(message)\n""".format(x=randomString(20)))
f.flush()
reload(changer)
changer.printer()

f.write("""message2 = "{x}"
def printer2():
    print(message2)""".format(x=randomString(5)))
f.flush()

reload(changer)
print(reload(changer))
changer.printer()
changer.printer2()