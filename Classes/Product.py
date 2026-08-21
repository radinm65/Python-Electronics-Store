from datetime import datetime
from IDGenerator import product_id_generator
from FileCommands import FileCommands


class Product:
    def __init__(self, seller_id):
        self.id = product_id_generator.next_id()
        self.seller_id = seller_id
        self.__date_created = datetime.today()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 3:
            raise ValueError(
                "Product name should be longer than 3 characters."
            )
        self.__name = new_name

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        if len(new_brand) < 3:
            raise ValueError(
                "Brand should be longer than 3 characters."
            )

        if any(char.isdigit() for char in new_brand):
            raise ValueError(
                "Brand shouldn't have numbers."
            )
        self.__brand = new_brand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        try:
            new_price = float(new_price)
        except ValueError:
            raise ValueError(
                "Price must be numeric."
            )

        if new_price <= 0:
            raise ValueError(
                "Price must be positive."
            )

        if new_price > 999999:
            raise ValueError(
                "Price can't be greater than 999999."
            )
        self.__price = new_price

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        if any(char.isdigit() for char in new_category):
            raise ValueError(
                "Category shouldn't have numbers."
            )

        if new_category not in ("Phone", "Laptop", "Camera"):
            raise ValueError(
                "Only Phone, Laptop and Camera categories are allowed."
            )
        self.__category = new_category

    @property
    def date_created(self):
        return self.__date_created

    def save(self):
        new_product = {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "price": self.price,
            "category": self.category,
            "seller_id": self.seller_id,
            "date_created": self.date_created.isoformat(),
        }
        return FileCommands.add_data("./Database/UnapprovedProducts.json", new_product)

    @staticmethod
    def get_approved_products():
        return FileCommands.get_file_data("./Database/ApprovedProducts.json")

    @staticmethod
    def save_approved_products(approvedProducts):
        return FileCommands.save_file_data("./Database/ApprovedProducts.json", approvedProducts)

    @staticmethod
    def delete_product(product_id):
        return FileCommands.delete_data("./Database/ApprovedProducts.json", product_id)

    @staticmethod
    def edit_product(json_product):
        return FileCommands.edit_data("./Database/ApprovedProducts.json", json_product)

    @staticmethod
    def get_product_byID(product_id):
        products = Product.get_approved_products()
        found_product = next(
            (product for product in products if product["id"] == product_id), None
        )
        return found_product

    @staticmethod
    def from_dict(product_data):
        product = Product(product_data["seller_id"])
        product.id = product_data["id"]
        product.name = product_data["name"]
        product.brand = product_data["brand"]
        product.price = product_data["price"]
        product.category = product_data["category"]

        return product

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
