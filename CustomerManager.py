from Manager import Manager
from FileCommands import FileCommands
from CustomerEmployee import CustomerEmployee
from Validator import Validator


class CustomerManager(Manager):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address
    ):
        super().__init__(
            firstname, lastname, username, password, age, phone_num, address
        )

    def raise_salary(self, customers_employee_id, amount):
        
        Validator.validate_raise_amount(amount)
        
        customer_employees = self.get_customer_employees()
        for ce in customer_employees:
            if ce["id"] == customers_employee_id:
                ce["salary"] += amount
                return self.save_customer_employees(customer_employees)
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
        new_customer = CustomerEmployee(
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
        json_customer = {
            "id": new_customer.id,
            "firstname": new_customer.firstname,
            "lastname": new_customer.lastname,
            "username": new_customer.username,
            "password": new_customer.password,
            "age": new_customer.age,
            "phone_num": new_customer.phone_num,
            "address": new_customer.address,
            "bank_account_num": new_customer.bank_account_num,
            "date_hired": new_customer.date_hired.isoformat(),
            "salary": new_customer.salary
        }
        return FileCommands.add_data("./CustomerEmployees.json", json_customer)

    @staticmethod
    def fire_employee(customers_employee_id):
        return FileCommands.delete_data("./CustomerEmployees.json", customers_employee_id)

    @staticmethod
    def get_customer_employees():
        return FileCommands.get_file_data("./CustomerEmployees.json")

    @staticmethod
    def save_customer_employees(customer_employees):
        return FileCommands.save_file_data("./CustomerEmployees.json", customer_employees)
