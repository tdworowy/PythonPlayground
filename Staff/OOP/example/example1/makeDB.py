from Staff.OOP.example.example1.person import Person, Manager

homer = Person("Homer Simposon")
boJack = Person("BoJack Horseman ", job="Actor", pay=1000)
rick = Manager("Rick Sanches", 20000)

import  shelve
db = shelve.open('personDB')
for obj in (homer,boJack,rick):
    db[obj.name] = obj
db.close()