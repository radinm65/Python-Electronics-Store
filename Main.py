import colorama
from Classes.CustomerManager import CustomerManager
from Classes.SellerManager import SellerManager
from Classes.Person import Person
from Classes.Customer import Customer
from Classes.Seller import Seller
from Classes.CustomerEmployee import CustomerEmployee
from Classes.SellerEmployee import SellerEmployee
from Classes.Product import Product
from Report import Report
from Validator import Validator


def print_error(message):
    print(colorama.Fore.RED)
    print(message, colorama.Fore.WHITE)


def print_successful(message):
    print(colorama.Fore.GREEN)
    print(message, colorama.Fore.WHITE)


# Show Menus -------------------


def show_main_menu():
    print(
        colorama.Fore.YELLOW,
        "\nWelcome!\n\n"
        "1- Customer\n"
        "2- Seller\n"
        "3- Customer Employee\n"
        "4- Seller Employee\n"
        "5- Customer Manager\n"
        "6- Seller Manager\n"
        "7- Exit\n\n",
        colorama.Fore.WHITE,
    )


def show_customer_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Shop\n" "2- Tickets\n" "3- Account Info\n" "4- Back\n", colorama.Fore.WHITE
    )


def show_customer_shop_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Checkout\n"
        "2- Add to Cart\n"
        "3- Add To Favorites\n"
        "4- Add Favorites To cart\n"
        "5- Delete From Cart\n"
        "6- Delete From Favorites\n"
        "7- See Cart and Favorites\n"
        "8- Back\n",
        colorama.Fore.WHITE,
    )


def show_ticket_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- See Submited tickets\n" "2- Submit Ticket\n" "3- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Products Menu\n" "2- Tickets Menu\n" "3- Account Info\n" "4- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_product_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Make Product\n"
        "2- See Unapproved Products\n"
        "3- See Selling Products\n"
        "4- Back\n",
        colorama.Fore.WHITE,
    )


def show_customer_employee_menu():
    pass


def show_seller_employee_menu():
    pass


def show_customer_employee_manager_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Hire Customer Employee\n"
        "2- Fire Customer Employee\n"
        "3- Give Raise\n"
        "4- See All Customer Employees\n"
        "5- See All Customers\n"
        "6- Get top 5 Customers .xlsx Report\n"
        "7- See Account Info\n"
        "8- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_employee_manager_menu():
    print(
        colorama.Fore.YELLOW,
        "1- Hire seller Employee\n"
        "2- Fire seller Employee\n"
        "3- Give Raise\n"
        "4- See All seller Employees\n"
        "5- See All sellers\n"
        "6- Get top 5 sellers .xlsx Report\n"
        "7- See Account Info\n"
        "8- Back\n",
        colorama.Fore.WHITE,
    )


# Fuctions and Methods -----------------------------------------------------------------------------------

# Joined Managers Functions -----------------------


def hire_employee(employee_type):
    try:
        print_error("Enter 'e' on first input to exit\n")

        firstname = input("Enter Firstname:\n")
        if firstname == "e":
            print_successful("Exited Hiring!\n")
            return True

        Validator.validate_firstname(firstname)

        lastname = input("Enter Lastname:\n")
        Validator.validate_lastname(lastname)

        username = input("Enter Username:\n")
        Validator.validate_username(username)

        password = input("Enter Password:\n")
        Validator.validate_password(password)

        age = input("Enter age:\n")
        Validator.validate_age(age)

        phone_num = input("Enter Phone number:\n")
        Validator.validate_phone(phone_num)

        address = input("Enter Address:\n")
        Validator.validate_address(address)

        bank_account_num = input("Enter Bank Account Number:\n")
        Validator.validate_bank_account(bank_account_num)

        salary = int(input("Enter Salary:\n"))
        Validator.validate_salary(salary)

        if employee_type == "customer":
            CustomerManager.hire_employee(
                firstname,
                lastname,
                username,
                password,
                age,
                phone_num,
                address,
                bank_account_num,
                salary,
            )
            print_successful("Customer Employee has Been Hired Successfully!")

        elif employee_type == "seller":
            SellerManager.hire_employee(
                firstname,
                lastname,
                username,
                password,
                age,
                phone_num,
                address,
                bank_account_num,
                salary,
            )
            print_successful("Seller Employee has Been Hired Successfully!")
        return True

    except ValueError as e:
        print_error(e)
        return False


def fire_employee(employee_type):
    try:
        emp_id = int(input(f"\nEnter {employee_type} Employee ID to Fire:\n"))
        if employee_type == "customer":
            if CustomerManager.fire_employee(emp_id):
                print_successful("Customer Employee is Fired!")
        elif employee_type == "seller":
            if SellerManager.fire_employee(emp_id):
                print_successful("Seller Employee is Fired!")
    except Exception as e:
        print_error(e)


def give_employee_raise(employee_type):
    try:
        success = False
        emp_id = int(input("\nEnter Customer Employee ID to Give Raise:\n"))
        if employee_type == "customer":
            if CustomerManager.check_employee_byID(emp_id):
                salary_raise = int(input("How much raise?\n"))
                CustomerManager.raise_salary(emp_id, salary_raise)
                success = True
            else:
                print_error("No Such ID Was Found")

        elif employee_type == "seller":

            if SellerManager.check_employee_byID(emp_id):
                salary_raise = int(input("How much raise?\n"))
                SellerManager.raise_salary(emp_id, salary_raise)
                success = True
            else:
                print_error("No Such ID Was Found")
        if success:
            print_successful(f"{employee_type} Employee was given a raise!")

    except Exception as e:
        print_error(e)


def show_all_employees(employee_type):
    if employee_type == "customer":
        employees = CustomerManager.get_customer_employees()

    elif employee_type == "seller":
        employees = SellerManager.get_seller_employees()

    if len(employees) == 0:
        print_error(f"No {employee_type} employees have been registered.")
        return

    for emp in employees:
        print(colorama.Fore.BLUE)
        print(
            f"ID: {emp['id']}\n"
            f"Firstname: {emp['firstname']}\n"
            f"Lastname: {emp['lastname']}\n"
            f"Username: {emp['username']}\n"
            f"Password: *********\n"
            f"Age: {emp['age']}\n"
            f"Phone_num: {emp['phone_num']}\n"
            f"Address: {emp['address']}\n"
            f"Bank account Number: {emp['bank_account_num']}\n"
            f"Date Hired: {emp['date_hired']}\n"
            f"Salary: {emp['salary']}\n"
        )

    print(colorama.Fore.WHITE)


def show_all_users(employee_type):
    if employee_type == "customer":
        users = Customer.get_customers()

    elif employee_type == "seller":
        users = SellerEmployee.get_sellers()

    else:
        print_error("Invalid user type.")
        return

    if len(users) == 0:
        print_error(f"No {employee_type}s have been registered.")
        return

    for user in users:
        print(colorama.Fore.BLUE)
        print(
            f"ID: {user['id']}\n"
            f"Firstname: {user['firstname']}\n"
            f"Lastname: {user['lastname']}\n"
            f"Username: {user['username']}\n"
            f"Password: *********\n"
            f"Age: {user['age']}\n"
            f"Phone_num: {user['phone_num']}\n"
            f"Address: {user['address']}\n"
            f"Balance: {user['balance']}\n"
        )

        if employee_type == "customer":
            print(
                f"Cart: {user['cart']}\n"
                f"Favorites: {user['favorites']}\n"
                f"Bought: {user['bought']}\n"
            )

        elif employee_type == "seller":
            print(f"Sold: {user['sold']}\n")

        print()

    print(colorama.Fore.WHITE)


def generate_top3_report(employee_type):
    successfull = False
    if employee_type == "customer":
        if len(Customer.get_customers()) < 5:
            print_error("Not enough data for report to generate.")
        else:
            try:
                if Report.generate_top_customers_report():
                    successfull = True
            except Exception as e:
                print_error(e)
    elif employee_type == "seller":
        if len(SellerEmployee.get_sellers()) < 5:
            print_error("Not enough data for report to generate.")
        else:
            try:
                if Report.generate_top_sellers_report():
                    successfull = True
            except Exception as e:
                print_error(e)

    if successfull:
        print_successful("Generated Succesfully")


def show_manager_account_info(manager):
    print(colorama.Fore.BLUE)
    print(
        f"Firstname: {manager.firstname}\n"
        f"Lastname: {manager.lastname}\n"
        f"Username: {manager.username}\n"
        f"Age: {manager.age}\n"
        f"Phone_num: {manager.phone_num}\n"
        f"Address: {manager.address}\n",
        colorama.Fore.WHITE,
    )


def signup_login_user(username, password, usertype):

    data = {
        "customer": {
            "file": "./Database/Customers.json",
            "class": Customer,
            "panel": customers_panel,
        },
        "seller": {
            "file": "./Database/Sellers.json",
            "class": Seller,
            "panel": sellers_panel,
        },
    }

    try:
        user_data = data[usertype]

        login, user = Person.check_login(user_data["file"], username, password)

        if login:
            user_obj = user_data["class"].from_dict(user)
            user_data["panel"](user_obj)
            return True

        print_error("Wrong Username or Password.")

        while True:
            signup_choice = input("\nDo you have an Account?\n1- Yes\n2- No\n")

            if signup_choice == "1":
                return False

            elif signup_choice == "2":

                signedup, new_user = signup_user(usertype)

                if signedup:
                    user_data["panel"](new_user)
                    return True

            else:
                print("Please only choose from options!")

    except ValueError as e:
        print_error(e)


def signup_user(signup_type):
    try:
        print_error("Enter 'e' on first input to exit\n")

        firstname = input("Enter Firstname:\n")
        if firstname == "e":
            print_successful("Exited signup!\n")
            return False, None

        Validator.validate_firstname(firstname)

        lastname = input("Enter Lastname:\n")
        Validator.validate_lastname(lastname)

        username = input("Enter Username:\n")
        Validator.validate_username(username)

        if signup_type == "customer":
            for customer in Customer.get_customers():
                if customer["username"] == username:
                    raise ValueError("Username already exists.")
        elif signup_type == "seller":
            for seller in SellerEmployee.get_sellers():
                if seller["username"] == username:
                    raise ValueError("Username already exists.")

        password = input("Enter Password:\n")
        Validator.validate_password(password)

        age = input("Enter age:\n")
        Validator.validate_age(age)

        phone_num = input("Enter Phone number:\n")
        Validator.validate_phone(phone_num)

        address = input("Enter Address:\n")
        Validator.validate_address(address)

        if signup_type == "customer":
            user = Customer(
                firstname,
                lastname,
                username,
                password,
                age,
                phone_num,
                address,
                save=True,
            )
            print_successful("Customer Signed up Successfully!")

        elif signup_type == "seller":
            user = Seller(
                firstname,
                lastname,
                username,
                password,
                age,
                phone_num,
                address,
                save=True,
            )
            print_successful(
                "Seller signed up Successfully!\nAfter Being Approved, you can signin"
            )
        return True, user

    except ValueError as e:
        print_error(e)
        return False, None


def show_products():
    try:
        products = Product.get_approved_products()
        print(colorama.Fore.BLUE)
        for product in products:
            product_obj = Product.from_dict(product)
            print(product_obj)
        print(colorama.Fore.WHITE)

    except ValueError as e:
        print_error(e)


def handle_customer_add_actions(customer, method):

    actions = {"cart": customer.add_to_cart, "favorites": customer.add_to_favorites}

    messages = {
        "cart": "Enter Product ID To Add to cart:\n",
        "favorites": "Enter Product ID To Add to favorites:\n",
    }

    while True:
        try:
            print_error("enter e to exit")
            product_id = input(messages[method])

            if product_id == "e":
                break

            product_id = int(product_id)

            successful = actions[method](product_id)

            if not successful:
                print_error("Failed To do task")
                continue

            again = input("Anything Else?\n1- Yes\n2- No\n")

            if again != "1":
                break

        except ValueError as e:
            print_error(e)


def handle_customer_remove_actions(customer, method):

    actions = {
        "cart": customer.remove_from_cart,
        "favorites": customer.remove_from_favorites,
    }

    messages = {
        "cart": "Enter Product ID To remove from cart:\n",
        "favorites": "Enter Product ID To remove from favorites:\n",
    }

    if method not in actions:
        print_error("Invalid remove action")

    while True:
        try:
            print_error("enter e to exit")
            product_id = input(messages[method])
            if product_id == "e":
                break

            product_id = int(product_id)
            successful = actions[method](product_id)

            if successful:
                print_successful("Removed Successfully")
            else:
                print_error("Failed To do task")

            again = input("Anything Else?\n1- Yes\n2- No\n")

            if again != "1":
                break

        except ValueError as e:
            print_error(e)


def show_customer_cart_and_favorites(customer_id):
    print(colorama.Fore.BLUE)

    customer = Customer.get_customer_byID(customer_id)

    print("\n========== CART ==========")

    if len(customer["cart"]) == 0:
        print("Your cart is empty.")
    else:
        for product_id in customer["cart"]:
            product = Product.get_product_byID(product_id)

            if product:
                print(
                    f"ID: {product['id']}\n"
                    f"Name: {product['name']}\n"
                    f"Brand: {product['brand']}\n"
                    f"Price: {product['price']}\n"
                    f"Category: {product['category']}\n"
                    f"-------------------------\n"
                )

    # Favorites
    print("\n======== FAVORITES ========")

    if len(customer["favorites"]) == 0:
        print("Your favorites are empty.")
    else:
        for product_id in customer["favorites"]:
            product = Product.get_product_byID(product_id)

            if product:
                print(
                    f"ID: {product['id']}\n"
                    f"Name: {product['name']}\n"
                    f"Brand: {product['brand']}\n"
                    f"Price: {product['price']}\n"
                    f"Category: {product['category']}\n"
                    f"-------------------------\n"
                )

    print(colorama.Fore.WHITE)


def add_cart_to_favorites(customer):
    try:
        if Customer.add_cart_to_favorites(customer.id):
            print_successful("Favorites added to cart successfully!")
        else:
            print_error("Customer not found.")

    except ValueError as e:
        print_error(e)


# Panels -----------------------------------------------------------------


def customers_panel(customer):
    while True:

        print_successful(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n"
        )

        show_customer_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                customers_Shop_panel(customer)
            case "2":
                customers_Ticket_panel(customer)
            case "3":
                print(colorama.Fore.BLUE)
                print(customer)
            case "4":
                break
            case _:
                print_error("Please only choose from options")


def customers_Shop_panel(customer):
    while True:
        print_successful(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n"
        )

        show_products()

        show_customer_shop_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                try:
                    customer.checkout()
                except ValueError as e:
                    print_error(e)
            case "2":
                handle_customer_add_actions(customer, "cart")
            case "3":
                handle_customer_add_actions(customer, "favorites")
            case "4":
                add_cart_to_favorites(customer)
            case "5":
                handle_customer_remove_actions(customer, "cart")
            case "6":
                handle_customer_remove_actions(customer, "favorites")
            case "7":
                show_customer_cart_and_favorites(customer.id)
            case "8":
                break
            case _:
                print_error("Please only choose from options")


def customers_Ticket_panel(customer):
    while True:
        print_successful(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n"
        )
        show_ticket_menu()
        choice = input("Please Choose:\n")

        match choice:

            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case _:
                print_error("Please only choose from options")


def sellers_panel(seller):
    pass


def customer_employee_panel(customer_employee):
    pass


def seller_employee_panel(seller_employee):
    pass


def show_employee_manager_panel(manager, employee_type):
    while True:
        print_successful(
            f"Welcome {employee_type.capitalize()} Manager {manager.firstname} {manager.lastname}!\n"
        )

        if employee_type == "customer":
            show_customer_employee_manager_menu()
        else:
            show_seller_employee_manager_menu()

        choice = input("Please Choose:\n")

        match choice:

            case "1":
                while True:
                    if hire_employee(employee_type):
                        break

            case "2":
                fire_employee(employee_type)

            case "3":
                give_employee_raise(employee_type)

            case "4":
                show_all_employees(employee_type)

            case "5":
                show_all_users(employee_type)

            case "6":
                generate_top3_report(employee_type)

            case "7":
                show_manager_account_info(manager)

            case "8":
                break

            case _:
                print_error("Please only choose from options")


# Main -----------------------------------------------------------------------


def main():

    customersManager = CustomerManager(
        "Radin",
        "Motahhary",
        "radinm123",
        "Radinian@123",
        "21",
        "9379499511",
        "Karaj_ mehrshahr",
    )
    sellersManager = SellerManager(
        "Radin",
        "Motahhary",
        "radinm123",
        "Radinian@123",
        "21",
        "9379499511",
        "Karaj_ mehrshahr",
    )

    while True:
        show_main_menu()
        choice = input("Please choose:\n")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            username = input("Please enter your username:\n")
            password = input("Please enter your password:\n")

            match choice:
                case "1":
                    login = signup_login_user(username, password, "customer")
                case "2":
                    login = signup_login_user(username, password, "seller")
                case "3":
                    login, customer_employee = Person.check_login(
                        "./Database/CustomerEmployees.json", username, password
                    )
                    if login:
                        customer_employee_panel(customer_employee)

                case "4":
                    login, seller_employee = Person.check_login(
                        "./Database/SellerEmployees.json", username, password
                    )
                    if login:
                        seller_employee_panel(seller_employee)

                case "5":
                    if (
                        username == customersManager.username
                        and customersManager.password
                        == Person.get_hash_Password(password)
                    ):
                        show_employee_manager_panel(customersManager, "customer")
                        login = True
                    else:
                        login = False
                case "6":
                    if (
                        username == sellersManager.username
                        and sellersManager.password
                        == Person.get_hash_Password(password)
                    ):
                        show_employee_manager_panel(sellersManager, "seller")
                        login = True
                    else:
                        login = False
            if not login:
                print(colorama.Fore.RED)
                print("Wrong username or password", colorama.Fore.WHITE)
        elif choice == "7":
            print(colorama.Fore.RED, "\nBye!\n", colorama.Fore.WHITE)
            break
        else:
            print_error("Please only choose from options")


if __name__ == "__main__":
    main()
