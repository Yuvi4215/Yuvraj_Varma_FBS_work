import re

data="""101 Yogi 25 adi@gmail.com
102 dinesh 15 dani@gmail.com
103 vansh 105 vsh@gamil.co.in
104 ansh 5 ansh.u@gmail.com"""

result=re.findall(r"^\d+", data, re.M) # get starting value(ID)
print(result)
