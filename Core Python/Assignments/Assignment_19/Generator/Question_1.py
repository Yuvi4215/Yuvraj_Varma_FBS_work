### 1. We want to generate Fibonacci numbers up to a certain limit. Instead of computing and storing
#      the entire sequence in memory, create generator to yield Fibonacci numbers one by one, conserving memory and
#      allowing for easy iteration.


def fibonacciGenerator():
    a = -1
    b = 1
    while True:
        c = a + b
        a, b = b, c
        yield b


res = fibonacciGenerator()
rng = int(input("How many Fibonacci numbers you want to generate : "))
print(
    """
------------------
Fibonacci Series :""")
for _ in range(rng):
    print(next(res), end=" ")