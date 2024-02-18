import sys

if __name__ == "__main__":

    try:
         test = []
         test[1]

    except Exception:
        print(sys.exc_info())