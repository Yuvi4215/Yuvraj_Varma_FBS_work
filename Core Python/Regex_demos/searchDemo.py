import re

data="""101 test 25 pakistan
102 test 15 bangaladesh
103 test 45 china
104 test 35 turkey"""

result=re.search(r" \d{2} ", data) # check only first occurance in data
print(result)
print(result.span())
print(result.group())