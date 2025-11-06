import re

data="""101 Yogi 25 adi@gmail.com
102 dinesh 15 dani@gmail.com
103 vansh 105 v.sh@gamil.system.co.in
104 ansh 5 ansh.u@gmail.com"""

result=re.findall(r"[\w.-]+@[\w.]+", data) # get email ids
print(result)
