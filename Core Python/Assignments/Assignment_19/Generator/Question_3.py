# 3. Write a generator function that mimics the behavior of the built-in range() function. The generator
#    should take start, stop, and step arguments and yield numbers within the specified range.


def iteratorFunction(start, end, step=1):
    while start < end:
        yield start
        start += step


start = int(input("Enter Starting Number : "))
end = int(input("Enter Starting Number : "))
step = int(input("Enter Step :"))
res = iteratorFunction(start, end, step)
for ele in res:
    print(ele,end="  ")