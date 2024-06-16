import os

if __name__ == "__main__":
    print("CPU count", os.cpu_count())
    print("OS name", os.name)
    print(os.get_exec_path(env=None))
    print(os.getlogin())
    print(os.getppid())
