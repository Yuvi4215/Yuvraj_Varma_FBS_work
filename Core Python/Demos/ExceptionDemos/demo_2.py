### specific exception and genrelize exception

li = [10, 20, 30, 40, 50, 60]

try:
    print(li)
    index = int(input("Enter the index to pop : "))
    li.pop(index)
    print(li)

    val = int(input("Enter the value to get index : "))
    print(li.index(val))

    # nu=1/0
except ValueError:
    print("ValueError occured :")
except IndexError:
    print("IndexError occured :")
except ZeroDivisionError:
    print("ZeroDivisionError occured :")

except:
    print("Genrealize error occured :")
