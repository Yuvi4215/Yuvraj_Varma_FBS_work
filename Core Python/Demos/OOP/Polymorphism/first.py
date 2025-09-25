### method overloading, method overwriting

def add(n1,n2):
    return n1+n2

def add(n1,n2,n3):
    return n1+n2+n3


# print(add(1,2))
print(add(10,20,30))
# print(add(10,20)) #TypeError- missing args as add method is overriden 