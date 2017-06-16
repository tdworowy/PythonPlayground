
def cachExeption(f):
    def func(*args):
        try:
            return f(*args)
        except Exception  as err:
            print(str(err))
            pass
    return func
