from abc import ABC
from datetime import datetime
import hashlib
from Validator import Validator
from FileCommands import FileCommands


class Person(ABC):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.age = age
        self.phone_num = phone_num
        self.address = address
        
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, new_firstname):
        Validator.validate_firstname(new_firstname)
        self.__firstname = new_firstname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, new_lastname):
        Validator.validate_lastname(new_lastname)
        self.__lastname = new_lastname

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        Validator.validate_username(value)
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        Validator.validate_password(new_password)
        self.__password = hashlib.sha256(new_password.encode()).hexdigest()
        
    def set_hashed_password(self, hashed_password):
        self.__password = hashed_password

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):

        Validator.validate_age(new_age)

        self.__age = int(new_age)

    @property
    def phone_num(self):
        return self.__phone_num

    @phone_num.setter
    def phone_num(self, new_num):

        Validator.validate_phone(new_num)

        self.__phone_num = new_num

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):

        Validator.validate_address(value)

        self.__address = value
        
        
    def get_hash_Password(password):
        return hashlib.sha256(password.encode()).hexdigest()
        
    @staticmethod    
    def check_login(file_path, input_username, input_password):
        hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
        get_users = FileCommands.get_file_data(file_path)
        
        if len(get_users) == 0 :
            raise ValueError("No users of this type have been registered yet")
        for user in get_users:
            if hashed_password == user["password"] and input_username == user["username"]:
                return True, user
            
        return False, None

