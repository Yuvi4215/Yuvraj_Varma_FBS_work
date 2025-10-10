### user defined exception


class UserAgeException(Exception):

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"The Age : {self.age}, is Invalid. "

class UserNameException(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The name : {self.name}, is Invalid. "

if __name__=="__main__":
    u1=UserAgeException(25)
    print(u1)
    u2=UserNameException("Sample")
    print(u2)