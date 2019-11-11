from math import fabs
from string import ascii_lowercase

a = "fsqoiaidfaukvngpsugszsnseskicpejjvytviya"
b = "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget"

def make_anagram(a, b):
    count = 0
    for letter in ascii_lowercase:
        ia = a.count(letter)
        ib = b.count(letter)
        count += abs(ia - ib)
    return count
if __name__ == "__main__":
    print(make_anagram(a,b))


