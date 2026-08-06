import colorama
from Classes.CustomerManager import CustomerManager
from Classes.SellerManager import SellerManager
from Classes.Person import Person
from Classes.Customer import Customer
from Classes.Seller import Seller
from Classes.CustomerEmployee import CustomerEmployee
from Classes.SellerEmployee import SellerEmployee
from Report import Report
from Validator import Validator

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
        "1- Shop\n" "2- Tickets\n" "2- Account Info\n" "4- Back\n",
        colorama.Fore.WHITE,
    )


def show_customer_shop_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Buy Product\n"
        "2- Add to Cart\n"
        "3- Add To Favorites\n"
        "4- See Cart and Favorites\n"
        "5- Back\n",
        colorama.Fore.WHITE,
    )


def show_customer_ticket_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- See Submited tickets\n" "2- Submit Ticket\n" "3- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_menu():
    pass


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
        print(colorama.Fore.RED)
        print("Enter 'e' on first input to exit\n", colorama.Fore.WHITE)

        firstname = input("Enter Firstname:\n")
        if firstname == "e":
            print(colorama.Fore.GREEN)
            print("Exited Hiring!\n", colorama.Fore.WHITE)
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
            print(colorama.Fore.GREEN)
            print("Customer Employee has Been Hired Successfully!", colorama.Fore.WHITE)

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
            print(colorama.Fore.GREEN)
            print("Seller Employee has Been Hired Successfully!", colorama.Fore.WHITE)
        return True

    except ValueError as e:
        print(colorama.Fore.RED)
        print(e, colorama.Fore.WHITE)
        return False


def fire_employee(employee_type):
    try:
        emp_id = int(input(f"\nEnter {employee_type} Employee ID to Fire:\n"))
        if employee_type == "customer":
            if CustomerManager.fire_employee(emp_id):
                print(colorama.Fore.GREEN)
                print("Customer Employee is Fired!")
        elif employee_type == "seller":
            if SellerManager.fire_employee(emp_id):
                print(colorama.Fore.GREEN)
                print("Seller Employee is Fired!")
    except Exception as e:
        print(colorama.Fore.RED)
        print(e, colorama.Fore.WHITE)


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
                print(colorama.Fore.RED)
                print("No Such ID Was Found", colorama.Fore.WHITE)

        elif employee_type == "seller":

            if SellerManager.check_employee_byID(emp_id):
                salary_raise = int(input("How much raise?\n"))
                SellerManager.raise_salary(emp_id, salary_raise)
                success = True
            else:
                print(colorama.Fore.RED)
                print("No Such ID Was Found", colorama.Fore.WHITE)
        if success:
            print(colorama.Fore.GREEN)
            print(f"{employee_type} Employee was given a raise!")

    except Exception as e:
        print(colorama.Fore.RED)
        print(e, colorama.Fore.WHITE)


def show_all_employees(employee_type):
    if employee_type == "customer":
        employees = CustomerManager.get_customer_employees()

    elif employee_type == "seller":
        employees = SellerManager.get_seller_employees()

    if len(employees) == 0:
        print(colorama.Fore.RED)
        print(f"No {employee_type} employees have been registered.")
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
        users = CustomerEmployee.get_customers()

    elif employee_type == "seller":
        users = SellerEmployee.get_sellers()

    else:
        print(colorama.Fore.RED)
        print("Invalid user type.")
        print(colorama.Fore.WHITE)
        return

    if len(users) == 0:
        print(colorama.Fore.RED)
        print(f"No {employee_type}s have been registered.", colorama.Fore.WHITE)
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
        if len(CustomerEmployee.get_customers()) < 5:
            print(colorama.Fore.RED)
            print("Not enough data for report to generate.", colorama.Fore.WHITE)
        else:
            try:
                if Report.generate_top_customers_report():
                    successfull = True
            except Exception as e:
                print(colorama.Fore.RED)
                print(e, colorama.Fore.WHITE)
    elif employee_type == "seller":
        if len(SellerEmployee.get_sellers()) < 5:
            print(colorama.Fore.RED)
            print("Not enough data for report to generate.", colorama.Fore.WHITE)
        else:
            try:
                if Report.generate_top_sellers_report():
                    successfull = True
            except Exception as e:
                print(colorama.Fore.RED)
                print(e, colorama.Fore.WHITE)

    if successfull:
        print(colorama.Fore.GREEN)
        print("Generated Succesfully", colorama.Fore.WHITE)


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
    if usertype == "customer":
        try:
            login, customer = Person.check_login(
                "./Database/Customers.json", username, password
            )
            if login:
                customer_obj = Customer.from_dict(customer)
                customers_panel(customer_obj)
                return True
            else:
                print(colorama.Fore.RED)
                print(
                    "Wrong Username or Password.",
                    colorama.Fore.WHITE,
                )
                while True:
                    signup_choice = input("\nDo you have an Account?\n1- Yes\n2- No\n")
                    if signup_choice == "1":
                        return False
                    elif signup_choice == "2":
                        while True:

                            signedup, signedup_customer = signup_user("customer")
                            if signedup:
                                customers_panel(signedup_customer)
                                return True
                    else:
                        print(colorama.Fore.RED)
                        print(
                            "Please only choose from options!",
                            colorama.Fore.WHITE,
                        )
        except ValueError as e:
            print(colorama.Fore.RED)
            print(
                e,
                colorama.Fore.WHITE,
            )
    elif usertype == "seller":
        try:
            login, seller = Person.check_login(
                "./Database/Sellers.json", username, password
            )
            if login:
                seller_obj = Seller.from_dict(seller)
                customers_panel(seller_obj)
                return True
            else:
                print(colorama.Fore.RED)
                print(
                    "Wrong Username or Password.",
                    colorama.Fore.WHITE,
                )
                while True:
                    signup_choice = input("\nDo you have an Account?\n1- Yes\n2- No\n")
                    if signup_choice == "1":
                        return False
                    elif signup_choice == "2":
                        while True:

                            signedup, signedup_customer = signup_user("seller")
                            if signedup:
                                sellers_panel(signedup_customer)
                                return True
                    else:
                        print(colorama.Fore.RED)
                        print(
                            "Please only choose from options!",
                            colorama.Fore.WHITE,
                        )
        except ValueError as e:
            print(colorama.Fore.RED)
            print(
                e,
                colorama.Fore.WHITE,
            )


def signup_user(signup_type):
    try:
        print(colorama.Fore.RED)
        print("Enter 'e' on first input to exit\n", colorama.Fore.WHITE)

        firstname = input("Enter Firstname:\n")
        if firstname == "e":
            print(colorama.Fore.GREEN)
            print("Exited signup!\n", colorama.Fore.WHITE)
            return False, None

        Validator.validate_firstname(firstname)

        lastname = input("Enter Lastname:\n")
        Validator.validate_lastname(lastname)

        username = input("Enter Username:\n")
        Validator.validate_username(username)

        for customer in CustomerEmployee.get_customers():
            if customer["username"] == username:
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
            print(colorama.Fore.GREEN)
            print("Customer Signed up Successfully!", colorama.Fore.WHITE)

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
            print(colorama.Fore.GREEN)
            print("Seller signed up Successfully!", colorama.Fore.WHITE)
        return True, user

    except ValueError as e:
        print(colorama.Fore.RED)
        print(e, colorama.Fore.WHITE)
        return False, None


# Panels -----------------------------------------------------------------


def customers_panel(customer):
    while True:
        print(colorama.Fore.GREEN)
        print(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n",
            colorama.Fore.WHITE,
        )

        show_customer_menu()
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
                print(colorama.Fore.RED)
                print("Please only choose from options")


def customers_Shop_panel(customer):
    while True:
        print(colorama.Fore.GREEN)
        print(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n",
            colorama.Fore.WHITE,
        )
        show_customer_shop_menu()
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
                print(colorama.Fore.RED)
                print("Please only choose from options")


def customers_Ticket_panel(customer):
    while True:
        print(colorama.Fore.GREEN)
        print(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n",
            colorama.Fore.WHITE,
        )
        show_customer_ticket_menu()
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
                print(colorama.Fore.RED)
                print("Please only choose from options")


def sellers_panel(seller):
    pass


def customer_employee_panel(customer_employee):
    pass


def seller_employee_panel(seller_employee):
    pass


def show_employee_manager_panel(manager, employee_type):
    while True:
        print(colorama.Fore.GREEN)
        print(
            f"Welcome {employee_type.capitalize()} Manager {manager.firstname} {manager.lastname}!\n",
            colorama.Fore.WHITE,
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
                print(colorama.Fore.RED)
                print("Please only choose from options")


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
                    login = signup_login_customer(username, password)
                case "2":
                    login, seller = Person.check_login(
                        "./Database/Sellers.json", username, password
                    )
                    seller_obj = Seller.from_dict(seller)
                    if login:
                        sellers_panel(seller_obj)

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
            print(colorama.Fore.RED)
            print("Please only choose from options!", colorama.Fore.WHITE)


if __name__ == "__main__":
    main()
