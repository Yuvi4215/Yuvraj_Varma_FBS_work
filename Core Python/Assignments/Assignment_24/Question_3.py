from threading import Thread
import string
import time

def lowercase():
    for ch in string.ascii_lowercase:
        print("Lower:", ch)
        time.sleep(0.05)

def uppercase():
    for ch in string.ascii_uppercase:
        print("Upper:", ch)
        time.sleep(0.05)


if __name__=="__main__":
    t1 = Thread(target=lowercase)
    t2 = Thread(target=uppercase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
