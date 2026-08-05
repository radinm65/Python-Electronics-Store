from Person import Person
from abc import abstractmethod


class Manager(Person):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address
    ):
        super().__init__(firstname, lastname, username, password, age, phone_num, address)
        
    @staticmethod
    @abstractmethod
    def raise_salary():
        pass
    
    @staticmethod
    @abstractmethod
    def hire_employee():
        pass
    
    @staticmethod
    @abstractmethod
    def fire_employee():
        pass