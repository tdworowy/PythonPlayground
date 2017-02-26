from Staff.Utils import rootDirectory


def generate(count):
    headers = "username,password\n"
    credentials = ["employee"+str(i)+","+"test10"+"\n" for i in range(count)]
    f = open(rootDirectory() + '//credentials.csv', 'w')
    f.write(headers)
    for x in credentials:
        f.write(x)

generate(10)