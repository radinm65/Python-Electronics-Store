from Classes.User import User
from Classes.Product import Product
from Classes.Ticket import Ticket
from IDGenerator import seller_id_generator
from FileCommands import FileCommands


class Seller(User):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address, save
    ):
        super().__init__(
            firstname, lastname, username, password, age, phone_num, address
        )
        self.id = seller_id_generator.next_id()
        self.selling_products = []
        self.sold = []
        if save:
            new_seller = {
                "id": self.id,
                "firstname": self.firstname,
                "lastname": self.lastname,
                "username": self.username,
                "password": self.password,
                "age": self.age,
                "phone_num": self.phone_num,
                "address": self.address,
                "balance": self.balance,
                "selling_products": self.selling_products,
                "sold": self.sold,
            }
            FileCommands.add_data("./Database/UnapprovedSellers.json", new_seller)


    def get_seller_unapproved_products(self):
        seller_unapproved_products = []
        unapproved_products = FileCommands.get_file_data(
            "./Database/UnapprovedProducts.json"
        )
        for up in unapproved_products:
            if up["seller_id"] == self.id:
                seller_unapproved_products.append(up)
        return seller_unapproved_products

    @staticmethod
    def get_sellers():
        return FileCommands.get_file_data("./Database/Sellers.json")

    @staticmethod
    def get_seller_byID(seller_id):
        sellers = Seller.get_sellers()
        found_seller = next(
            (seller for seller in sellers if seller["id"] == seller_id), None
        )
        return found_seller
    
    @staticmethod
    def delete_product_from_seller(seller_json, product_id):
        seller_json["selling_products"] = [product_id_json for product_id_json in seller_json["selling_products"] if product_id_json != product_id]
        return FileCommands.edit_data("./Database/Sellers.json", seller_json)
        
    @classmethod
    def from_dict(cls, data):
        seller = cls(
            data["firstname"],
            data["lastname"],
            data["username"],
            "Temp123!45",
            str(data["age"]),
            data["phone_num"],
            data["address"],
            save=False,
        )

        seller.set_hashed_password(data["password"])
        seller.id = data["id"]
        seller.balance = data["balance"]
        seller.selling_products = data["selling_products"]
        seller.sold = data["sold"]

        return seller

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Firstname: {self.firstname}\n"
            f"Lastname: {self.lastname}\n"
            f"Username: {self.username}\n"
            f"Age: {self.age}\n"
            f"Phone_num: {self.phone_num}\n"
            f"Address: {self.address}\n"
            f"Balance: {self.balance}\n"
            f"Selling products ID: {self.selling_products}\n"
            f"Sold: {self.sold}\n"
        )
