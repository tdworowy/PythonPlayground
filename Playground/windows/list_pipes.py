import glob


if __name__ == "__main__":
    for pipe in glob.glob(r"\\.\pipe\*"):
        print(pipe)