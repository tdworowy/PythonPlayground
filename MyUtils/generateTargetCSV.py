from MyUtils.randomString import generate_random_string
from rootDirectory import getRootDirectory


def generate(count):
    with open(getRootDirectory()+'\\target%s.csv'%count  ,'w') as f:
        f.write("userName,userId\n")
        for i in range(0,count):
            f.write(generate_random_string(10) + "," + generate_random_string(10) + "\n")





if __name__ == "__main__":
    generate(50000)