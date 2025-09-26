### Operator overloadding

class Time:

    def __init__(self, hour, min,sec):
        self.h=hour
        self.m=min
        self.s=sec

    def __add__(left,right):
        s=left.s +right.s
        m=s//60
        s=s%60

        m+=left.m + right.m
        h=m//60
        m=m%60

        h+=left.h + right.h
        # return f"{h} : {m} : {s}"
        # print(f"{h} : {m} : {s}")
        return Time(h,m,s)
    
    def __str__(self):
        return f"{self.h} : {self.m} : {self.s}"

t1=Time(35,43,29)
t2=Time(20,34,55)
t3=Time(14,16,17)
t4=Time(37,56,37)

# print(t1+t2)
print(t1+t2+t3+t4)