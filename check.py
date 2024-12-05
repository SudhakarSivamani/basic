from timeit import timeit
from random import randint

def add(a:int, b:int):
    return a+b

if __name__ == "__main__":
    x = randint(1000, 10_000)
    total:int = 0
    for no in range(x):
        total += add (no, total)
    print(f"\n\n{total = }")
