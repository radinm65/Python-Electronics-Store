from Classes.Employee import Employee
from Classes.Ticket import Ticket
from FileCommands import FileCommands
from IDGenerator import customer_employee_id_generator

class CustomerEmployee(Employee):
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
        salary
    ):
        super().__init__(
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
        self.id = customer_employee_id_generator.next_id()


    @staticmethod
    def get_customers():
        return FileCommands.get_file_data("./Database/Customers.json")

    @staticmethod
    def get_customer_byID(customer_id):
        customers = CustomerEmployee.get_customers()
        found_customer = next(
            (customer for customer in customers if customer["id"] == customer_id), None
        )
        return found_customer
    
    
    @staticmethod
    def delete_customer(customer_id):
        return FileCommands.delete_data("./Database/Customers.json", customer_id)
    
    @staticmethod
    def answer_ticket(ticket_id, answer):
        customer_tickets = Ticket.get_sendertype_tickets("customer")
        for ticket in customer_tickets:
            if ticket["id"] == ticket_id:
                if ticket["response"] == "":
                    ticket["response"] = answer
                    return FileCommands.edit_data("./Database/Tickets.json", ticket)
                else:
                    raise ValueError("Ticket already has a response")    
        return False
    
    
    @classmethod
    def from_dict(cls, data):
        customer_employee = cls(
            data["firstname"],
            data["lastname"],
            data["username"],
            "Temp123!45",
            str(data["age"]),
            data["phone_num"],
            data["address"],
            data["bank_account_num"],
            data["salary"],
        )
        customer_employee.set_hashed_password(data["password"])
        customer_employee.id = data["id"]
        customer_employee.date_hired = data["date_hired"]

        return customer_employee
    
    
    def __str__(self):
        return (
            f"Firstname: {self.firstname}\n"
            f"Lastname: {self.lastname}\n"
            f"Username: {self.username}\n"
            f"Age: {self.age}\n"
            f"Phone_num: {self.phone_num}\n"
            f"Address: {self.address}\n"
            f"Bank_account_num: {self.bank_account_num}\n"
            f"Salary: {self.salary}\n"
            f"Date_hired: {self.date_hired}\n"
        )
