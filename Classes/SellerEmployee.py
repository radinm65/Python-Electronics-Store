from Classes.Employee import Employee
from Classes.Ticket import Ticket
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
        if not SellerEmployee.check_unapproved_sellerID(seller_id):
            raise ValueError("ID not found.\n")
        unapproved_sellers = SellerEmployee.get_unapproved_sellers()
        for us in unapproved_sellers:
            if us["id"] == seller_id:
                FileCommands.delete_data("./Database/UnapprovedSellers.json", seller_id)
                return FileCommands.add_data("./Database/Sellers.json", us)
        return False

    @staticmethod
    def approve_product(product_id):
        if not SellerEmployee.check_unapproved_productID(product_id):
            raise ValueError("ID not found.\n")
        unapproved_products = SellerEmployee.get_unapproved_products()
        for up in unapproved_products:
            if up["id"] == product_id:
                FileCommands.delete_data(
                    "./Database/UnapprovedProducts.json", product_id
                )
                return FileCommands.add_data("./Database/ApprovedProducts.json", up)
        return False

    @staticmethod
    def check_unapproved_sellerID(sellerID):
        unapproved_sellers = SellerEmployee.get_unapproved_sellers()
        for us in unapproved_sellers:
            if sellerID == us["id"]:
                return True
        return False

    @staticmethod
    def check_unapproved_productID(productID):
        unapproved_products = SellerEmployee.get_unapproved_products()
        for up in unapproved_products:
            if productID == up["id"]:
                return True
        return False

    @staticmethod
    def remove_seller(seller_id):
        return FileCommands.delete_data("./Database/Sellers.json", seller_id)

    @staticmethod
    def remove_product(product_id):
        return FileCommands.delete_data("./Database/ApprovedProducts.json", product_id)
    
    
    @staticmethod
    def answer_ticket(ticket_id, answer):
        seller_tickets = Ticket.get_sendertype_tickets("seller")
        for ticket in seller_tickets:
            if ticket["id"] == ticket_id:
                if ticket["response"] == "":
                    ticket["response"] = answer
                    return FileCommands.edit_data("./Database/Tickets.json", ticket)
                else:
                    raise ValueError("Ticket already has a response")
        return False

    @staticmethod
    def get_sellers():
        return FileCommands.get_file_data("./Database/Sellers.json")

    @staticmethod
    def get_seller_byID(seller_id):
        sellers = SellerEmployee.get_sellers()
        found_seller = next(
            (seller for seller in sellers if seller["id"] == seller_id), None
        )
        return found_seller

    @classmethod
    def from_dict(cls, data):
        seller_employee = cls(
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
        seller_employee.set_hashed_password(data["password"])
        seller_employee.id = data["id"]
        seller_employee.date_hired = data["date_hired"]

        return seller_employee

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
