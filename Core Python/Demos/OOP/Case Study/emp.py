###
from abc import ABC, abstractmethod


class Emp(ABC):
    def __init__(self, id, name, basic_sal, dept, total_sal=0.0):
        self.id = id
        self.name = name
        self.basic_sal = basic_sal
        self.dept = dept
        self.total_sal = total_sal

    @abstractmethod
    def calculateSalary():
        pass

    def __str__(self):
        return (
            f"{self.id}, {self.name}, {self.basic_sal}, {self.total_sal}, {self.dept}"
        )
