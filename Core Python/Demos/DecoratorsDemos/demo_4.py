def myDecorator(fun):
    # print("myDecorator( ) start")
    def wrapper():
        print("wrapper( ) start ")
        fun()
        print("wrapper( ) end.")
    # print("myDecorator( ) End")
    return wrapper

@myDecorator
def greet():
    print("greet( ) method")

print(greet())


# def myDecorator(fun):
#     print("myDecorator( ) start")
#     def wrapper(x,y):
#         print("wrapper( ) start ")
#         fun(x,y)
#         print("wrapper( ) end.")
#     print("myDecorator( ) End")
#     return wrapper

# @myDecorator
# def greet(x,y):
#     print("greet( ) method")
#     print(x+y)

# greet(10,20)