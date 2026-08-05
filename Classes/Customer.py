from Classes.User import User
from IDGenerator import customer_id_generator
from FileCommands import FileCommands
from Classes.Product import Product


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
                "bought": self.bought
            }
            FileCommands.add_data("./Database/Customers.json", new_customer)


    def add_to_cart(self, product_id):
        product = Product.get_product_byID(product_id)
        
        if product is None:
            raise ValueError("Product not found.")
        
        customers = self.get_customers()
        
        for customer in customers:
            if customer["id"] == self.id:
                
                if product_id in customer["cart"]:
                    raise ValueError("Already in cart.")
                
                customer["cart"].append(product_id)
                return FileCommands.save_file_data("./Database/Customers.json", customers)
        return False
    
    def add_to_favorites(self, product_id):
        
        product = Product.get_product_byID(product_id)
        
        if product is None:
            raise ValueError("Product not found.")
        
        customers = self.get_customers()
        for customer in customers:
            if customer["id"] == self.id:
                
                if product_id in customer["favorites"]:
                    raise ValueError("Already in favorites.")
                
                customer["favorites"].append(product_id)
                return FileCommands.save_file_data("./Database/Customers.json", customers)
        return False

    def remove_from_favorites(self, product_id):
        customers = self.get_customers()
        
        for customer in customers:
            if customer["id"] == self.id:
                
                if product_id not in customer["favorites"]:
                    raise ValueError("Product is not in favorites.")
                
                customer["favorites"].remove(product_id)
                return FileCommands.save_file_data("./Database/Customers.json", customers)
        return False
    
    
    def remove_from_cart(self, product_id):
        customers = self.get_customers()
        
        for customer in customers:
            if customer["id"] == self.id:
                
                if product_id not in customer["cart"]:
                    raise ValueError("Product is not in cart.")
                
                customer["cart"].remove(product_id)
                return FileCommands.save_file_data("./Database/Customers.json", customers)
        return False
    
    def buy_product(self, product_id):
        product = Product.get_product_byID(product_id)
        if product is None:
            raise ValueError("Product not found.")
        
        customers = self.get_customers()

        for customer in customers:
            if customer["id"] == self.id:

                if product["price"] > customer["balance"]:
                    raise ValueError("Product Price is More than balance.")

                if product_id not in customer["cart"]:
                    raise ValueError("Product is not in cart.")

                customer["balance"] -= product["price"]
                customer["bought"].append(product)
                customer["cart"].remove(product_id)

                return FileCommands.save_file_data("./Database/Customers.json", customers)

        return False
    
    @staticmethod
    def from_dict(data):
        customer = Customer(
            data["firstname"],
            data["lastname"],
            data["username"],
            data["password"],
            data["age"],
            data["phone_num"],
            data["address"],
            False
        )

        customer.id = data["id"]
        customer.balance = data["balance"]
        customer.cart = data["cart"]
        customer.favorites = data["favorites"]
        customer.bought = data["bought"]

        return customer
    
    
    
    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"firstname: {self.firstname}\n"
            f"lastname: {self.lastname}\n"
            f"username: {self.username}\n"
            f"age: {self.age}\n"
            f"phone_num: {self.phone_num}\n"
            f"address: {self.address}\n"
        )
        
    
