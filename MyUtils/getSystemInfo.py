import os
import re

drivers = re.findall(r"[A-Z]+:.*$", os.popen("mountvol /").read(), re.MULTILINE)
print(drivers)

import pyodbc

print(pyodbc.drivers())
