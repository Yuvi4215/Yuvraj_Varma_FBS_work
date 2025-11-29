
# def fibonacci(num):
#     a=1
#     b=2

#     for _ in range(num):
#         print(a, end=" ")
#         c=a+b
#         a,b=b,c

# fibonacci(10)

def fibbonacci(start, end):
    a=0
    b=1
    while a<= end:
        if a>=start:
            print(a, end=" ")
            c=a+b
            a,b=b,c

fibbonacci(0,18)
