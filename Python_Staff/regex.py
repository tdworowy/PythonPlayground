import re

s = "Test 123 spam xxx"

x =  re.findall(r'\b\d+\b', s)
print(x)