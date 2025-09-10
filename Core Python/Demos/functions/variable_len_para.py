#Variable length of parameter/arguments
# 1. mentioning asterisk(*) symbol before para
# 2. we can pass multiple para to that funcyion
# 3. 
# 4.

def add(*values):
    sum=0
    print(type(values))
    for i in values:
        sum+=i

    return sum

sum = add(55,544,1,545,12,554,5,5,454,4,12,12)
print(sum)
sum = add(8745,879,78,787,97,87,978,78,8,748,87,8,74,88,78,798,78,8,748,554,5,5,454,4,12,12)
print(sum)