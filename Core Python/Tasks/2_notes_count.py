### Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# Take The amount values from user
amount = int(input("Enter the amount value :: "))

# Perform notes calculation
# only consider legal tender notes- 500,200,100,50,20,10
n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10


# Display the result
print(
    f"""Finally  note distribution is given by following
        500 ::{n500} 
        200 ::{n200}
        100 ::{n100} 
        50 ::{n50}
        20 ::{n20} 
        10 ::{n10}"""
)
