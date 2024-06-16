import shelve

if __name__ == "__main__":

    db = shelve.open("persondb")
    for key in sorted(db):
        print(key, "\t=>", db[key])

    rick = db["Rick Sanches"]
    rick.give_raise(10)
    db["Rick Sanches"] = rick
    db.close()
