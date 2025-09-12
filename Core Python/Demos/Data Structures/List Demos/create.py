### adding elements in list

li = []

flag = True
count = 1
while flag:
    element = int(input(f"Enter the number {count} ::"))
    li.append(element)
    count += 1
    option = input("y-for next element, s- for stop ::")
    if option == "s":
        flag = False

print(li)
