import threading
import time
import random

buffer = []
BUFFER_SIZE = 5
condition = threading.Condition()

def producer(name):
    while True:
        item = random.randint(1, 100)
        with condition:
            while len(buffer) == BUFFER_SIZE:
                print(f"{name} waiting, buffer full...")
                condition.wait()
            buffer.append(item)
            print(f"{name} produced {item} | Buffer:", buffer)
            condition.notify_all()
        time.sleep(random.random())

def consumer(name):
    while True:
        with condition:
            while not buffer:
                print(f"{name} waiting, buffer empty...")
                condition.wait()
            item = buffer.pop(0)
            print(f"{name} consumed {item} | Buffer:", buffer)
            condition.notify_all()
        time.sleep(random.random())

t1 = threading.Thread(target=producer, args=("Producer 1",))
t2 = threading.Thread(target=producer, args=("Producer 2",))
t3 = threading.Thread(target=consumer, args=("Consumer 1",))
t4 = threading.Thread(target=consumer, args=("Consumer 2",))

t1.start()
t2.start()
t3.start()
t4.start()
