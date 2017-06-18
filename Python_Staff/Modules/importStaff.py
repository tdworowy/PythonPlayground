modename = "string"
exec("import "+modename)
print(string) # it will work

modename2 = "os"
os = __import__(modename2)
print(os)