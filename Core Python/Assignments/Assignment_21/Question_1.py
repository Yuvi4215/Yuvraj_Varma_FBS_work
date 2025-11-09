flag = True
while flag:
    print("""
============================ Menu ============================
 1. Show Calculator
 2. Exit""")
    choice = input("Choice :: ")
    if choice == "1":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operator (+,-,*,/): ")
            if op not in ["+", "-", "*", "/"]:
                raise ValueError
            if op == "+":
                print("Result:", a + b)
            elif op == "-":
                print("Result:", a - b)
            elif op == "*":
                print("Result:", a * b)
            elif op == "/":
                if b == 0:
                    raise ZeroDivisionError
                print("Result:", a / b)
        except ValueError:
            print("Invalid number or operator")
        except ZeroDivisionError:
            print("Division by zero error")
    elif choice == "2":
        flag = False
    else:
        print("wrong choice.")
