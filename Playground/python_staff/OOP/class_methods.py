class Spam:
    num_instances = 0

    def __init__(self):
        Spam.num_instances += 1

    def print_num_instances():  # it works
        print("Instances created: ", Spam.num_instances)


if __name__ == "__main__":
    x = Spam()
    y = Spam()

    Spam.print_num_instances()
