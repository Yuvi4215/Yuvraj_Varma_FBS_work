### Print series from n to 1.


def series(n):
    if n > 0:
        print(n, end=" ")
        series(n - 1)

def sumOfSeries(n):
    if n==0:
        return 0
    
    return n+ sumOfSeries(n-1)

### get n factorial.
def factrorial(n):
    if n == 0:
        return 1
    return n * factrorial(n - 1)

def fibonacciSeries(n,a,b): 
    if n>0:
        c= a+b
        print(c, end=" ")
        fibonacciSeries(n-1, b,c)



num = 25
print("Printing series. ")
print("-------------------------------------------")
series(num)

print("\nSum of series :: ", sumOfSeries(num))
print("-------------------------------------------")
print("Factorial :: ", factrorial(7))

print("-------------------------------------------")
print("fibinacci series- ",fibonacciSeries(25,-1,1))
