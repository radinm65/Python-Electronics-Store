from Classes.User import User
from Classes.Product import Product
from Classes.CustomerEmployee import CustomerEmployee
from IDGenerator import customer_id_generator
from FileCommands import FileCommands
from datetime import datetime


class Customer(User):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address, save
    ):
        super().__init__(
            firstname, lastname, username, password, age, phone_num, address
        )
        self.id = customer_id_generator.next_id()
        self.cart = []
        self.favorites = []
        self.bought = []
        if save:
            new_customer = {
                "id": self.id,
                "firstname": self.firstname,
                "lastname": self.lastname,
                "username": self.username,
                "password": self.password,
                "age": self.age,
                "phone_num": self.phone_num,
                "address": self.address,
                "balance": self.balance,
                "cart": self.cart,
                "favorites": self.favorites,
                "bought": self.bought,
            }
            FileCommands.add_data("./Database/Customers.json", new_customer)


    @staticmethod
    def get_customers():
        return FileCommands.get_file_data("./Database/Customers.json")


    def add_to_cart(self, product_id):
        product = Product.get_product_byID(product_id)

        if product is None:
            raise ValueError("Product not found.")

        customers = Customer.get_customers()

        for customer in customers:
            if customer["id"] == self.id:

                if product_id in customer["cart"]:
                    raise ValueError("Already in cart.")

                customer["cart"].append(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def add_to_favorites(self, product_id):

        product = Product.get_product_byID(product_id)

        if product is None:
            raise ValueError("Product not found.")

        customers = Customer.get_customers()
        for customer in customers:
            if customer["id"] == self.id:

                if product_id in customer["favorites"]:
                    raise ValueError("Already in favorites.")

                customer["favorites"].append(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def remove_from_favorites(self, product_id):
        customers = Customer.get_customers()

        for customer in customers:
            if customer["id"] == self.id:

                if product_id not in customer["favorites"]:
                    raise ValueError("Product is not in favorites.")

                customer["favorites"].remove(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def remove_from_cart(self, product_id):
        customers = Customer.get_customers()

        for customer in customers:
            if customer["id"] == self.id:

                if product_id not in customer["cart"]:
                    raise ValueError("Product is not in cart.")

                customer["cart"].remove(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def checkout(self):
        customers = Customer.get_customers()
        for customer in customers:
            if customer["id"] == self.id:
                if len(customer["cart"]) == 0:
                    raise ValueError("Cart is empty.")
                sellers = FileCommands.get_file_data("./Database/Sellers.json")
                purchase_date = datetime.today().isoformat()
                total_price = 0
                # اول چک موجودی
                for product_id in customer["cart"]:
                    product = Product.get_product_byID(product_id)
                    if product is None:
                        raise ValueError("Product not found.")
                    total_price += product["price"]
                if total_price > customer["balance"]:
                    raise ValueError("Not enough balance.")
                # خرید انجام شود
                for product_id in customer["cart"]:
                    product = Product.get_product_byID(product_id)
                    customer["bought"].append(
                        {"product_id": product_id, "date": purchase_date}
                    )
                    # پیدا کردن فروشنده
                    for seller in sellers:
                        if seller["id"] == product["seller_id"]:
                            seller["balance"] += product["price"]
                            seller["sold"].append(
                                {"product_id": product_id, "date": purchase_date}
                            )
                            break
                customer["balance"] -= total_price
                # خالی کردن سبد
                customer["cart"].clear()
                FileCommands.save_file_data("./Database/Sellers.json", sellers)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False
    
    @staticmethod
    def get_customer_byID(customer_id):
        customers = Customer.get_customers()
        found_customer = next(
            (customer for customer in customers if customer["id"] == customer_id), None
        )
        return found_customer
    
    @staticmethod
    def add_cart_to_favorites(customer_id):

        customers = Customer.get_customers()

        for customer in customers:

            if customer["id"] == customer_id:

                if len(customer["favorites"]) == 0:
                    raise ValueError("Favorites is empty.")

                for product_id in customer["favorites"]:
                    
                    if product_id not in customer["cart"]:
                        customer["cart"].append(product_id)
                    
                customer["favorites"] = []

                return FileCommands.save_file_data(
                    "./Database/Customers.json",
                    customers
                )

        return False
    
    @staticmethod
    def add_to_balance(customer_id, balance):

        customers = Customer.get_customers()

        for customer in customers:

            if customer["id"] == customer_id:

                customer["balance"] += balance

                return FileCommands.save_file_data(
                    "./Database/Customers.json",
                    customers
                )

        return False

    @staticmethod
    def from_dict(data):
        customer = Customer(
            data["firstname"],
            data["lastname"],
            data["username"],
            "Temp123!45",
            str(data["age"]),
            data["phone_num"],
            data["address"],
            False,
        )

        customer.set_hashed_password(data["password"])
        customer.id = data["id"]
        customer.balance = data["balance"]
        customer.cart = data["cart"]
        customer.favorites = data["favorites"]
        customer.bought = data["bought"]

        return customer

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
            f"Cart: {self.cart}\n"
            f"Favorites: {self.favorites}\n"
            f"Bought: {self.bought}\n"
        )
