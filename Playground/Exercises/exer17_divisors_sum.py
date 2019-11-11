class AdvancedArithmetic(object):
    def divisor_sum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisor_sum(self, n):
        return sum([i for i in range(1, n + 1) if n % i == 0])

if __name__ == "__main__":
    c = Calculator()
    print(c.divisor_sum(6))