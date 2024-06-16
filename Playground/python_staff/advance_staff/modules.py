seplen = 60
sepchr = "-"


def listing(module, verbose=True):
    sepline = seplen * sepchr
    if verbose:
        print(sepline)
        print("name: ", module.__name__, "file:", module.__file__)
        print(sepline)
    count = 0
    for attr in module.__dict__:
        print("%02d) %s" % (count, attr), end=" ")
        if attr.startswith("__"):
            print("<built-in variable>")
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, "have %d variables" % count)
        print(sepline)


if __name__ == "__main__":
    import Modules
    import tkinter

    listing(Modules)
    listing(tkinter)
