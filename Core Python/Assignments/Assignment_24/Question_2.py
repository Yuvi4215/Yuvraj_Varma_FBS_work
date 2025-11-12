from threading import Thread, Condition

condition = Condition()
current = 1

def print_odd():
    global current
    while current <= 10:
        with condition:
            if current % 2 == 1:
                print("Odd:", current)
                current += 1
                condition.notify()
            else:
                condition.wait()

def print_even():
    global current
    while current <= 10:
        with condition:
            if current % 2 == 0:
                print("Even:", current)
                current += 1
                condition.notify()
            else:
                condition.wait()

if __name__=="__main__":
    t1 = Thread(target=print_odd)
    t2 = Thread(target=print_even)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
