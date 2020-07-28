def get_primes():
    candidate = 2
    found = []
    while True:
        if all(candidate % prime !=0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate +=1


if __name__ == "__main__":

    primes = get_primes()


    x1 ,x2 ,x3 = next(primes), next(primes), next(primes)
    print(x1, x2,x3)
