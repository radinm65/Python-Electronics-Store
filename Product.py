from datetime import datetime
from IDGenerator import product_id_generator
from FileCommands import FileCommands
from Validator import Validator


class Product:
    def __init__(self, name, brand, price, category, seller_id):
        self.id = product_id_generator.next_id()
        self.name = name
        self.brand = brand
        self.price = price
        self.category = category
        self.seller_id = seller_id
        self.__date_created = datetime.today()
        new_product = {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "price": price,
            "category": self.category,
            "seller_id": self.seller_id,
            "date_created": self.date_created.isoformat(),
        }
        FileCommands.add_data("./UnapprovedProducts.json", new_product)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        Validator.validate_product_name(new_name)
        self.__name = new_name

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        Validator.validate_brand(new_brand)
        self.__brand = new_brand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        Validator.validate_price(new_price)
        self.__price = float(new_price)

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        Validator.validate_category(new_category)
        self.__category = new_category
        
    @property
    def date_created(self):
        return self.__date_created

    @staticmethod
    def get_approved_products():
        return FileCommands.get_file_data("./ApprovedProducts.json")

    @staticmethod
    def save_approved_products(approvedProducts):
        return FileCommands.save_file_data("./ApprovedProducts.json", approvedProducts)

    @staticmethod
    def get_product_byID(product_id):
        products = Product.get_approved_products()
        found_product = next(
            (product for product in products if product["id"] == product_id), None
        )
        return found_product

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Brand: {self.brand}\n"
            f"Price: {self.price}\n"
            f"Category: {self.category}\n"
            f"Made By ID: {self.seller_id}\n"
            f"Date Created: {self.date_created}\n"
        )
