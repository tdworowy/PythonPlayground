from Playground.my_utils.staff.random_string import generate_random_string
from Playground.rootDirectory import get_root_directory


def generate(count):
    with open(get_root_directory() + '\\target%s.csv' % count, 'w') as f:
        f.write("userName,userId\n")
        for i in range(0, count):
            f.write(generate_random_string(10) + "," + generate_random_string(10) + "\n")


if __name__ == "__main__":
    generate(50000)
