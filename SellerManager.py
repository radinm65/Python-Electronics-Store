from Manager import Manager
from FileCommands import FileCommands
from SellerEmployee import SellerEmployee
from Validator import Validator


class SellerManager(Manager):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address
    ):
        super().__init__(
            firstname, lastname, username, password, age, phone_num, address
        )

    def raise_salary(self, seller_employee_id, amount):
        
        Validator.validate_raise_amount(amount)
        
        seller_employees = self.get_seller_employees()
        for se in seller_employees:
            if se["id"] == seller_employee_id:
                se["salary"] += amount
                return self.save_seller_employees(seller_employees)
        return False

    @staticmethod
    def hire_employee(
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
        new_employee = SellerEmployee(
            firstname,
            lastname,
            username,
            password,
            age,
            phone_num,
            address,
            bank_account_num,
            salary
        )
        json_employee = {
            "id": new_employee.id,
            "firstname": new_employee.firstname,
            "lastname": new_employee.lastname,
            "username": new_employee.username,
            "password": new_employee.password,
            "age": new_employee.age,
            "phone_num": new_employee.phone_num,
            "address": new_employee.address,
            "bank_account_num": new_employee.bank_account_num,
            "date_hired": new_employee.date_hired.isoformat(),
            "salary": new_employee.salary
        }
        return FileCommands.add_data("./SellerEmployees.json", json_employee)

    @staticmethod
    def fire_employee(seller_employee_id):
        return FileCommands.delete_data("./SellerEmployees.json", seller_employee_id)

    @staticmethod
    def get_seller_employees():
        return FileCommands.get_file_data("./SellerEmployees.json")

    @staticmethod
    def save_seller_employees(seller_employees):
        return FileCommands.save_file_data("./SellerEmployees.json", seller_employees)
