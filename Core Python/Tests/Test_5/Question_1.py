### 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5] Accept an amount from user and calculate how many
# minimum number of notes will be needed for that amount.


def calculateMinNote(li):
    amount = int(input("Enter the Amount : "))
    di = {}
    for i in range(0, len(li)):
        note = amount // li[i]
        amount %= li[i]
        di[li[i]] = note
    return di


li = [2000, 500, 200, 100, 50, 20, 10, 5]
di = calculateMinNote(li)
print("Denominations and Count is : ", di)
