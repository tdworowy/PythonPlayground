import re
from math import log2


def shannon_information_text(text: str) -> float:
    words_freq = {}
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    words = text.split(" ")

    for word in words:
        if word not in words_freq.keys():
            words_freq[word] = 1
        else:
            words_freq[word] += 1

    probabilities = [p/len(words_freq) * log2(p/len(words_freq)) for p in words_freq.values()]
    result = -sum(probabilities)
    return result if result > 0 else 0


print(shannon_information_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi facilisis quam et "
                               "mauris cursus laoreet."))

print(shannon_information_text("test test test"))
print(shannon_information_text("test test"))
print(shannon_information_text("test"))
