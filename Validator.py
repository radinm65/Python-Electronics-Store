import re


class Validator:


    # Person Validators --------------------------------
    
    @staticmethod
    def validate_firstname(firstname):
        if len(firstname) < 3:
            raise ValueError("Firstname can't be shorter than 3 characters.")

        if any(char.isdigit() for char in firstname):
            raise ValueError("Firstname shouldn't have numbers.")

        return True


    @staticmethod
    def validate_lastname(lastname):
        if len(lastname) < 3:
            raise ValueError("Lastname can't be shorter than 3 characters.")

        if any(char.isdigit() for char in lastname):
            raise ValueError("Lastname shouldn't have numbers.")

        return True


    @staticmethod
    def validate_username(username):
        if len(username) < 5:
            raise ValueError("Username can't be shorter than 5 characters.")

        if not any(char.isdigit() for char in username):
            raise ValueError("Username should have numbers.")

        return True


    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password too short.")

        if sum(char.isdigit() for char in password) < 3:
            raise ValueError("Password needs 3 numbers.")

        if not password[0].isupper():
            raise ValueError("Password needs capital letter.")

        if not re.search(r"[^a-zA-Z0-9]", password):
            raise ValueError("Password needs special character.")

        return True


    @staticmethod
    def validate_age(age):
        if not age.isdigit():
            raise ValueError("Age must be numeric.")

        if int(age) > 80:
            raise ValueError("Age cannot be above 80.")

        return True


    @staticmethod
    def validate_phone(phone):
        if len(phone) != 10:
            raise ValueError("Phone must have 10 digits.")

        if not phone.isdigit():
            raise ValueError("Phone must be numeric.")

        return True


    @staticmethod
    def validate_address(address):
        if len(address) < 10:
            raise ValueError("Address is too short.")

        return True
    
    
    
    
    # User Validators --------------------------------

    @staticmethod
    def validate_balance(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Balance must be numeric.")

        if value < 0:
            raise ValueError("Balance can't be negative.")
        
        
        
    # Employee Validators --------------------------------
        
    @staticmethod
    def validate_salary(value):

        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be numeric.")

        if value < 0:
            raise ValueError("Salary can't be negative.")


    @staticmethod
    def validate_bank_account(value):

        value = str(value)

        if not value.isdigit():
            raise ValueError("Bank account must contain only numbers.")

        if len(value) < 10:
            raise ValueError("Bank account number is too short.")
        
        
    
    # Product Validators --------------------------------
    

    @staticmethod
    def validate_product_name(name):
        if len(name) < 3:
            raise ValueError(
                "Product name should be longer than 3 characters."
            )

        if any(char.isdigit() for char in name):
            raise ValueError(
                "Product name shouldn't have numbers."
            )


    @staticmethod
    def validate_brand(brand):
        if len(brand) < 3:
            raise ValueError(
                "Brand should be longer than 3 characters."
            )

        if any(char.isdigit() for char in brand):
            raise ValueError(
                "Brand shouldn't have numbers."
            )


    @staticmethod
    def validate_price(price):

        try:
            price = float(price)
        except ValueError:
            raise ValueError(
                "Price must be numeric."
            )

        if price <= 0:
            raise ValueError(
                "Price must be positive."
            )

        if price > 999999:
            raise ValueError(
                "Price can't be greater than 999999."
            )


    @staticmethod
    def validate_category(category):

        if any(char.isdigit() for char in category):
            raise ValueError(
                "Category shouldn't have numbers."
            )

        if category not in ("Phone", "Laptop", "Camera"):
            raise ValueError(
                "Only Phone, Laptop and Camera categories are allowed."
            )
            
              
            
    # Ticket Validators --------------------------------
            
            
    @staticmethod
    def validate_ticket_request(request):
        if len(request) > 200:
            raise ValueError(
                "Ticket request must be under 200 characters."
            )

        if len(request) < 10:
            raise ValueError(
                "Ticket request must be at least 10 characters."
            )


    @staticmethod
    def validate_name(name):
        if len(name) < 3:
            raise ValueError(
                "Name must be at least 3 characters."
            )

        if any(char.isdigit() for char in name):
            raise ValueError(
                "Name shouldn't have numbers."
            )


    @staticmethod
    def validate_sender_type(sender_type):
        if sender_type not in ("customer", "seller"):
            raise ValueError(
                "Sender type must be customer or seller."
            )
            
    
    # Sellers Manager Validators --------------------------------
    
        
    @staticmethod
    def validate_raise_amount(amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be numeric.")

        if amount <= 0:
            raise ValueError("Raise amount must be greater than zero.")