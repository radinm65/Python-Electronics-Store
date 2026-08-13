from Classes.Employee import Employee
from FileCommands import FileCommands
from IDGenerator import seller_employee_id_generator


class SellerEmployee(Employee):
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
        date_hired,
        salary,
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
            date_hired,
            salary,
        )
        self.id = seller_employee_id_generator.next_id()

    @staticmethod
    def save_sellers(sellers):
        return FileCommands.save_file_data("./Database/Sellers.json", sellers)

    @staticmethod
    def get_unapproved_sellers():
        return FileCommands.get_file_data("./Database/UnapprovedSellers.json")

    @staticmethod
    def get_unapproved_products():
        return FileCommands.get_file_data("./Database/UnapprovedProducts.json")

    @staticmethod
    def approve_seller(seller_id):
        unapproved_sellers = SellerEmployee.get_unapproved_sellers()
        for us in unapproved_sellers:
            if us["id"] == seller_id:
                FileCommands.delete_data("./Database/UnapprovedSellers.json", seller_id)
                return FileCommands.add_data("./Database/Sellers.json", us)
        return False

    @staticmethod
    def remove_seller(seller_id):
        return FileCommands.delete_data("./Database/Sellers.json", seller_id)

    @staticmethod
    def approve_product(product_id):
        unapproved_products = SellerEmployee.get_unapproved_products()
        for up in unapproved_products:
            if up["id"] == product_id:
                FileCommands.delete_data("./Database/UnapprovedProducts.json", product_id)
                return FileCommands.add_data("./Database/Products.json", up)
        return False

    @staticmethod
    def answer_ticket(ticket_id, answer):
        tickets = FileCommands.get_file_data("./Database/SellerTickets.json")
        for ticket in tickets:
            if ticket["id"] == ticket_id:
                if ticket["response"] == "":
                    ticket["response"] = answer
                    return FileCommands.save_file_data("./Database/SellerTickets.json", tickets)
                else:
                    raise ValueError("Ticket already has a response")
        return False
