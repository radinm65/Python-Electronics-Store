from Employee import Employee
from FileCommands import FileCommands
from datetime import datetime


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

    @staticmethod
    def get_customers():
        return FileCommands.get_file_data("./Customers.json")

    @staticmethod
    def save_customers(datas):
        return FileCommands.save_file_data("./Customers.json", datas)

    @staticmethod
    def delete_customer(customer_id):
        return FileCommands.delete_data("./Customers.json", customer_id)

    @staticmethod
    def answer_ticket(ticket_id, answer):
        tickets = FileCommands.get_file_data("./CustomerTickets.json")
        for ticket in tickets:
            if ticket["id"] == ticket_id:
                if ticket["response"] == "":
                    ticket["response"] = answer
                    return FileCommands.save_file_data(
                        "./CustomerTickets.json", tickets
                    )
                else:
                    raise ValueError("Ticket already has a response")
        return False
