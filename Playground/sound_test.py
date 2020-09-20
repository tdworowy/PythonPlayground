import winsound
import random

if __name__ == "__main__":
    # for i in range(37, 32767):
    #     winsound.Beep(i, 100)

    x = list(range(37, 32767))
    random.shuffle(x)
    for i in x:
        winsound.Beep(i, 100)
