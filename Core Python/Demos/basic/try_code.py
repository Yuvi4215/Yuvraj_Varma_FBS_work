num = 123           #int(input("Enter the Number :: "))
count=0
rev=0
while num>0:
    rem=num%10
    rev=rev*10 +rem
    num//=10
    count+=1

print(rev)
print(count)

