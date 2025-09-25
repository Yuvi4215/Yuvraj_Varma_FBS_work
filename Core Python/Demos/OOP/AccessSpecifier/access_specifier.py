### Access specifier
# variable-->public
# _variable-->protected
# __variable-->private



class EMP:
    def __init__(self,id, name, salary):
        self.id=id              #public
        self._name=name         #protected
        self.__salary=salary    # private
    


e1=EMP("E-101", "Yuvi", 69000)
print(e1.id)
print(e1._name)
# print(e1.__salary)    #Can not access private member
print(e1._EMP__salary)  #way to access the private member