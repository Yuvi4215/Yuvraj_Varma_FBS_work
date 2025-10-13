### 2. A teacher came to class with a large box tokhat has several coins. Each coin has a number printed on it.
#   Before coming to class, she ensured that All the numbers occur an Even number of times. However,
#   while coming to the class, one coin fell down and got lost. She wants to find out the number on the missing coin.
#   Inputs:
#       The original number of coins and the actual number on each of the coins, separated by spaces.

#   Output:
#       The number on the missing coin
# Sample Input: 8
#       5 7 2 7 5 2 5
# Sample Output: 5


def printMissingCoin():
    n = int(input("Input number of coins : "))
    if n % 2 == 0:
        coins_str = input("Enter coins with spaces : ")
        li = coins_str.split()
        # print(li)
        if len(li) % 2 == 1:
            for index in range(0, len(li)):
                li[index] = int(li[index])
        # print(li)

        for ele in li:
            if li.count(ele) % 2 == 1:
                print(f"The Number on  Missing Coin is : {ele}")
                break
        else:
            print("You have already even Coin set : ")

    else:
        print("Wrong coin set. ")


printMissingCoin()
