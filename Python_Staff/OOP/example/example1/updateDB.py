import shelve
db = shelve.open('persondb')
for key in sorted(db):
    print(key, '\t=>' , db[key])

rick = db['Rick Sanches']
rick.giveRaise(10)
db['Rick Sanches'] = rick
db.close()