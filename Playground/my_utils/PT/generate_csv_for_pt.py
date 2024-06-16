from Playground.root_directory import get_root_directory


def generate(count):
    headers = "username,password\n"
    credentials = ["employee" + str(i) + "," + "test10" + "\n" for i in range(count)]
    f = open(get_root_directory() + "//credentials.csv", "w")
    f.write(headers)
    for x in credentials:
        f.write(x)


if __name__ == "__main__":
    generate(10)
