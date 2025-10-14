def outer(x):
    def inner(y):
        return x + y
    return inner

add=outer(1)
print(add(1))