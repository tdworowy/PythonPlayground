from Staff.rootDirectory import  getRootDirectory


def generate(count):
    headers = "username,password\n"
    credentials = ["employee"+str(i)+","+"test10"+"\n" for i in range(count)]
    f = open(getRootDirectory() + '//credentials.csv', 'w')
    f.write(headers)
    for x in credentials:
        f.write(x)

generate(10)