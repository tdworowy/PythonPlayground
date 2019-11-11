
d = 4
a = [1, 2, 3, 4, 5]
def rot_left(a, d):
     return a[d:] + a[:d]

if __name__ == "__main__":
     print (rot_left(a, d))