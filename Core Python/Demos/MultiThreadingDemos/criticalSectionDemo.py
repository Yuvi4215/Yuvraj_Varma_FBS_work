#critical section
from threading import Thread

def deposite(amt):

    with open("Core Python/Demos/MultiThreadingDemos/account.txt","r") as fp:
        content=fp.read()
        balance=float(content)
        balance+=amt
    
    with open("Core Python/Demos/MultiThreadingDemos/account.txt", "w") as fp:
        fp.write(str(balance))
    
def withdraw(amt):

    with open("Core Python/Demos/MultiThreadingDemos/account.txt","r") as fp:
        content=fp.read()
        balance=float(content)
        balance-=amt

    with open("Core Python/Demos/MultiThreadingDemos/account.txt", "w") as fp:
        fp.write(str(balance))
    

if __name__=="__main__":
    t1=Thread(name="Thread1", target=deposite, args=(5000,))
    t2=Thread(name="Thread2", target=withdraw, args=(3000,))
    t1.start()
    t2.start()