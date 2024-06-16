def annotate(label):
    def decorate(func):
        func.label = label
        return func

    return decorate


if __name__ == "__main__":

    @annotate("Test label")
    def spam(a, b):
        return a + b

    print(spam(1, 2), spam.label)
