import re

data="""101 Boundary condition 25 pakistan
102 Moundary condition 15 bangaladesh
103 Foundary condition 45 china
104 Moundary and Boundary condition 35 turkey"""

result=re.sub(r" \d{2} ", " ** ",data) # replace/subtitude match pattern with given
print(result)
