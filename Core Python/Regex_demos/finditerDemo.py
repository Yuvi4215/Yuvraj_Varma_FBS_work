import re

data="""100 Tester brain power is equal to 1 developer brain.
tester-101 test 25 pakistan
tester-102 test 15 bangaladesh
tester-103 test 45 china
tester-104 test 35 turkey
it will take atleast 5+ year to become developer."""

result=re.finditer(r" \d{2} ",data)
# print(result)
for iter in result:
    print(iter)
    # print(iter.span())
    print(iter.group())