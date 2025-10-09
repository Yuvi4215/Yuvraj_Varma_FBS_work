### specific exception and genrelize exception

li = [10, 20, 30, 40, 50, 60]

try:
    # nu=1/0
    print(li)
    index = int(input("Enter the index to pop : "))
    li.pop(index)
    print(li)

    val = int(input("Enter the value to get index : "))
    print(li.index(val))
    raise ValueError
except ValueError:
    print("ValueError occured :")
except IndexError:
    print("IndexError occured :")
# except ZeroDivisionError as e:
#     print("ZeroDivisionError occured :", e)

except Exception as e:
    print("Genrealize error occured : ",e)
