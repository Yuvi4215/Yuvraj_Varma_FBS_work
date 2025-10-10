### User define exception use
from userAgeException import UserAgeException, UserNameException


class Emp:

    def __init__(self, id, name, age):
        if not (age > 0 and age < 120):
            raise UserAgeException(age)
        if not (name.isalpha()):
            raise UserNameException(name)
        self.id = id
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"

if __name__=="__main__":
    e1=Emp(101,"14user",25)
    print(e1)