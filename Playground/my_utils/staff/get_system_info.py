import os
import re
if __name__ == '__main__':
    drivers = re.findall(r"[A-Z]+:.*$", os.popen("mountvol /").read(), re.MULTILINE)
    print(drivers)

    import pyodbc

    print(pyodbc.drivers())
