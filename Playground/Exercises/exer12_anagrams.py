
x = "ifailuhkqq"

def generate_substrings_list(s, n):
      i = 0
      ini_n = n
      substrings = []
      while n <= len(s):
        substrings.append(s[i:n])
        i = n
        n = n+ini_n
      return substrings

from itertools import combinations
def sherlock_and_anagrams(s):
    anagrams = 0
    for combination in [''.join(l) for i in range(len(s)) for l in combinations(s, i + 1)]:
        if combination in s:
           index = s.index(combination)
           index2 = len(combination)
           if  s[index:index2] != [] and s[index:index2] in s[:index+1] + s[index:]:
               print( s[index:index2])
               print(s[:index] + s[index:])
               anagrams +=1
    return anagrams


#print (sherlockAndAnagrams(x))


import itertools
perms = [''.join(perm) for perm in itertools.permutations(x)]
print(len(perms))


def strhash(s):
    h = 0
    for c in s:
        h += hash(c)
    return(h)

def seqsum(n):
    return int((n**2 + n) / 2)

def sherlock_and_anagrams(s):
    count = 0
    for l in range(len(s)):
        counter = dict()
        #l is length of substr.
        for i in range(len(s)-l):
            hashed = strhash(s[i:i+l+1])
            if hashed not in counter:
                counter[hashed] = 1
            else:
                counter[hashed] += 1
        for k,v in counter.items():
            if v > 1:
                count += seqsum(v-1)
    print(count)
    return count


from collections import Counter

def count_anagrams(string):
    buckets = {}
    print(len(string))
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            print(list(range(1, len(string) - i + 1)))
            key = frozenset(Counter(string[i:i+j]).items())
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count
if __name__ == "__main__":
    count_anagrams(x)