### Decorator


def add(x,y):
    print(x+y)

print(id(add))
demo=add
del add
print(id(demo))
demo(20,50)