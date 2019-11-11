
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
ar2 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
from collections import Counter

def sock_merchant1(ar):
    pairs = 0
    for ele in set(ar):
        pairs = pairs + int(Counter(ar)[ele]/2)
    return pairs






def sock_merchant2(ar):
    pairs = 0
    for ele in set(ar):
       print(int(Counter(ar)[ele]/2))

if __name__ == "__main__":
    print(sock_merchant2(ar))
    print("_____________")
    sock_merchant2(ar)