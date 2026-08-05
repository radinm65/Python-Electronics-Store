from User import User
from Product import Product
from IDGenerator import seller_id_generator
from FileCommands import FileCommands
from Ticket import Ticket


class Seller(User):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address
    ):
        super().__init__(
            firstname, lastname, username, password, age, phone_num, address
        )
        self.id = seller_id_generator.next_id()
        self.sold = []
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
            "sold": self.sold
        }
        FileCommands.add_data("./UnapprovedSellers.json", new_seller)
        
        
    def make_product(self, name, brand, price, category):
        return Product(name, brand, price, category, self.id)
            
    def get_seller_unapproved_products(self):
        seller_unapproved_products = []
        unapproved_products = FileCommands.get_file_data("./UnapprovedProducts.json")
        for up in unapproved_products:
            if up["seller_id"] == self.id:
                seller_unapproved_products.append(up)
        return seller_unapproved_products
    
    
                
