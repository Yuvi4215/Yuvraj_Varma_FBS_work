num = 123  # int(input("Enter the Number :: "))
count = 0
rev = 0
# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num //= 10
#     count += 1

# print(rev)
# print(count)


# name="This String is to be reversed."
# def reverse_string(s):
#     return s[::-1]

# print("Original String ::", name)
# print("Reversed String ::", reverse_string(name))

# name="level"
# def is_palindrome(s):
#     s=s.lower()
#     return s==s[::-1]

# print("palindrome :: ", is_palindrome(name))


# def string_reversed(s):
#     reversed_str = ""

#     for i in range(len(s) - 1, -1, -1):
#         reversed_str += s[i]
#     return reversed_str

# name = "This String is to be reversed"
# print(f"Original String is :: {name}")
# print("Reversed String is ::", string_reversed(name))


def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


name = "madaM"
print("palindrome :: ", is_palindrome(name))
