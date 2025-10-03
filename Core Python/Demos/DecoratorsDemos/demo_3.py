###
def add(x,y):
    print("Add( ) method")
    print(x+y)

def demo(func):
    print("demo( ) method")
    func(10,20)

demo(add)