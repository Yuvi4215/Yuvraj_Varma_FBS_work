from threading import Thread

def fun1(string1):
    for char in string1:
        print(char, end=" ",flush=True)

def fun2(string2):
    for char in string2:
        print(char, end=" ",flush=True)

if __name__=="__main__":
    t1=Thread(name="Thread1", target=fun1, args=("aaaaaaaaaa", ))
    t2=Thread(name="Thread2", target=fun2, args=("bbbbbbbbbb", ))
    t1.start()
    t1.join(4)
    t2.start()
    print("This is executed by main thread....")