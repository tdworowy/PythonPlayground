if __name__ == "__main__":
    import glob

    print(glob.glob("person*"))
    print(open("personDB.dir").read())
    print(open("personDB.dat", "rb").read())

    import shelve

    db = shelve.open("personDB")
    print(len(db))
    print(list(db.keys()))

    rick = db["Rick Sanches"]
    print(rick.last_name())
