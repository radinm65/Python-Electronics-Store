from Person import Person
from abc import abstractmethod
from datetime import datetime 
from Validator import Validator


class Employee(Person):
    def __init__(
        self,
        firstname,
        lastname,
        username,
        password,
        age,
        phone_num,
        address,
        bank_account_num,
        salary,
    ):
        super().__init__(
            firstname, lastname, username, password, age, phone_num, address
        )
        self.bank_account_num = bank_account_num
        self.date_hired = datetime.today()
        self.salary = salary
        
    @property
    def bank_account_num(self):
        return self.__bank_account_num


    @bank_account_num.setter
    def bank_account_num(self, value):
        Validator.validate_bank_account(value)
        self.__bank_account_num = value


    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, value):
        Validator.validate_salary(value)
        self.__salary = value

    @staticmethod
    @abstractmethod
    def answer_ticket():
        pass
