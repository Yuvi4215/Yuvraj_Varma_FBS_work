### filter elements

def even(num):
    if num%2==0:
        return num



nums=[1,2,3,4,5,6,7,8,9,10]

# results=list(filter(lambda x: x%2==0,nums))
results=list(filter(even,nums))
print(results)