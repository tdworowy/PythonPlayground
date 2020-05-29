# https://en.wikipedia.org/wiki/Logistic_map
from typing import Union


def find_fixed_point(r: float, x: float) -> Union[float, str]:
    try:
        x2 = r * (x - x ** 2)
        print(x2)
        if x == x2:
            return x
        else:
            return find_fixed_point(r, x2)

    except RecursionError:
        return "Probably there is no fix point"


print(f"Fix point: {find_fixed_point(2.5, 0.2)}")
print("*"*10)
print(f"Fix point: {find_fixed_point(2, 0.3)}")
print("*"*10)
print(f"Fix point: {find_fixed_point(2.1, 0.4)}")
print("*"*10)
print(f"Fix point: {find_fixed_point(3, 0.4)}")
print("*"*10)
