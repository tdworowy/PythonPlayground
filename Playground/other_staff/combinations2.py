from itertools import product

"""What is the number of sequences of six digits where the number of even digits is equal to the number of odd 
digits? """
if __name__ == "__main__":
    print(len([1 for x in product(range(10), repeat=6) if len([1 for e in x if e % 2 == 0]) == 3]))

