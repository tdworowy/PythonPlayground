from myUtils.randomString import generateRandomString


def generate(count):
    with open('target%s.csv'%count  ,'w') as f:
        f.write("userName,userId\n")
        for i in range(0,count):
            f.write(generateRandomString(10)+","+generateRandomString(10)+"\n")





if __name__ == "__main__":
    generate(300000)