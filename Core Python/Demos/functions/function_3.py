### perfect number


def isPerfect():
    # Number
    number = 496
    sum = 0
    # perform operation
    for i in range(1, number):
        if number % i == 0:
            sum += i

    if sum == number:
        print("It is perfect number. ")
    else:
        print("not a perfect number")


isPerfect()
