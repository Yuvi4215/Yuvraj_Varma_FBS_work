### Math and Random
import random


print(random.random())
print(random.randint(0,9999))
print(random.randbytes(2))
print(random.gauss(1.2, 7.4))
li=[1,2,3,4,5,6,7,8,9]
print(random.choice(li))
random.shuffle(li)
print(li)
print(random.uniform(1.0,3.0))
print(random.sample(li,3))