### Named/keyword - parameter/arguments
# 1. Assigning value to the para in function call
# 2. flow of mentionig keyword is from right to left
# 3. it ingore sequacnce of position para concept
# 4. 


def emp(id, name ,dept,sal, age,address):
    data=f"ID:{id}\n NAME:{name}\n DEPARTMENT:{dept}\n SALARY:{sal}\n AGE:{age}\n ADDRESS:{address}\n"
    return data

print(emp(1,"YUVRAJ","DS",69000,27,"SOLAPUR")) # not using keyword and maintaining sequace of parameter
print(emp(address="Solapur",age=27,sal=45000, dept="DS",name="YUVRAJ",id=10))