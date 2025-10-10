### finally

def divison(x, y):
    try:
        # raise ValueError("Value Error")
        div = x / y
    except ZeroDivisionError as e:
        print(f"Error : {e}")
    except Exception as e:
        print(f"Error : {e}")
    else:
        print(div)
    finally:
        return f"Program executed succesfully"


x = int(input("Enter the Divident : "))
y = int(input("Enter the Divisor : "))
print(divison(x, y))