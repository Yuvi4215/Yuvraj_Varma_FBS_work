# 2. Implement a generator function that yields palindrome numbers. Palindromes are numbers that read
#    the same backward as forward (e.g., 121, 1331). Generate palindromes lazily and infinitely.


def palindromeGenerator():
    num = 1
    while True:
        if num < 9:
            yield num
        else:
            temp = num
            pal_num = 0
            while temp > 0:
                digit = temp % 10
                temp = temp // 10

                pal_num = pal_num * 10 + digit
            if pal_num == num:
                yield num
        num += 1


res = palindromeGenerator()
rng = int(input("Enter how many palindrome numbers you want to generate : "))
print("""
--------------------
Palindrome Numbers :""")
for _ in range(rng):
    print(next(res), end=" ")