from Classes.Employee import Employee
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
        bank_account,
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
            bank_account,
            salary
        )
        self.id = customer_employee_id_generator.next_id()

    @staticmethod
    def get_customers():
        return FileCommands.get_file_data("./Database/Customers.json")

    @staticmethod
    def save_customers(datas):
        return FileCommands.save_file_data("./Database/Customers.json", datas)

    @staticmethod
    def delete_customer(customer_id):
        return FileCommands.delete_data("./Database/Customers.json", customer_id)

    @staticmethod
    def answer_ticket(ticket_id, answer):
        tickets = FileCommands.get_file_data("./Database/CustomerTickets.json")
        for ticket in tickets:
            if ticket["id"] == ticket_id:
                if ticket["response"] == "":
                    ticket["response"] = answer
                    return FileCommands.save_file_data(
                        "./Database/CustomerTickets.json", tickets
                    )
                else:
                    raise ValueError("Ticket already has a response")
        return False
    
