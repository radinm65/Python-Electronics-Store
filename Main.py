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
    pass


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


# Show Panels ----------------------


def customers_panel(customer):
    pass


def sellers_panel(seller):
    pass


def customer_employee_panel(customer_employee):
    pass


def seller_employee_panel(seller_employee):
    pass


# Fuctions and Methods -----------------------------


def hire_customer_employee():
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
        return True
    except ValueError as e:
        print(colorama.Fore.RED)
        print(e, colorama.Fore.WHITE)


def fire_customer_employee():
    try:
        emp_id = input("\nEnter Customer Employee ID to Fire:\n")
        if CustomerManager.fire_employee(emp_id):
            print(colorama.Fore.GREEN)
            print("Customer Employee is Fired!")
    except Exception as e:
        print(colorama.Fore.RED)
        print(e, colorama.Fore.WHITE)


def give_raise_customer_employee():
    try:
        emp_id = input("\nEnter Customer Employee ID to Give Raise:\n")
        if CustomerManager.check_employee_byID(emp_id):
            salary_raise = int(input("How much raise?\n"))
            CustomerManager.raise_salary()
            print(colorama.Fore.GREEN)
            print("Customer Employee is Fired!")
        else:
            print(colorama.Fore.RED)
            print("No Such ID Was Found", colorama.Fore.WHITE)
    except Exception as e:
        print(colorama.Fore.RED)
        print(e, colorama.Fore.WHITE)


def show_all_customer_employees():
    CEs = CustomerManager.get_customer_employees()
    if len(CEs) == 0:
        print(colorama.Fore.RED)
        print("No Customer Employees have been registered.", colorama.Fore.WHITE)
    for ce in CEs:
        print(colorama.Fore.BLUE)
        print(
            f"ID: {ce["id"]}\n"
            f"Firstname: {ce["firstname"]}\n"
            f"Lastname: {ce["lastname"]}\n"
            f"Username: {ce["username"]}\n"
            f"Password: *********\n"
            f"Age: {ce["age"]}\n"
            f"Phone_num: {ce["phone_num"]}\n"
            f"Address: {ce["address"]}\n"
            f"Bank account Number: {ce["bank_account_num"]}\n"
            f"Date Hired: {ce["date_hired"]}\n"
            f"Salary: {ce["salary"]}\n"
        )
    print(colorama.Fore.WHITE)


def show_all_customers():
    customers = CustomerEmployee.get_customers()
    if len(customers) == 0:
        print(colorama.Fore.RED)
        print("No Customers have been registered.", colorama.Fore.WHITE)
    for c in customers:
        print(colorama.Fore.BLUE)
        print(
            f"ID: {c["id"]}\n"
            f"Firstname: {c["firstname"]}\n"
            f"Lastname: {c["lastname"]}\n"
            f"Username: {c["username"]}\n"
            f"Password: *********\n"
            f"Age: {c["age"]}\n"
            f"Phone_num: {c["phone_num"]}\n"
            f"Address: {c["address"]}\n"
            f"Bank account Number: {c["bank_account_num"]}\n"
            f"Date Hired: {c["date_hired"]}\n"
            f"Salary: {c["salary"]}\n"
        )
    print(colorama.Fore.WHITE)
    
def generate_top5_customers_report():
    if len(CustomerEmployee.get_customers()) < 5:
        print(colorama.Fore.RED)
        print("Not enough data for report to generate.", colorama.Fore.WHITE)
    else:
        try:
            Report.generate_top_customers_report()
        except Exception as e:
            print(colorama.Fore.RED)
            print(e, colorama.Fore.WHITE) 
            
            
def show_account_info(customersManager):
    print(colorama.Fore.BLUE)
    print(
        f"Firstname: {customersManager.firstname}\n" 
        f"Lastname: {customersManager.lastname}\n" 
        f"Username: {customersManager.username}\n" 
        f"Age: {customersManager.age}\n" 
        f"Phone_num: {customersManager.phone_num}\n" 
        f"Address: {customersManager.address}\n", 
        colorama.Fore.WHITE
    )


def customer_employee_manager_panel(customersManager):
    while True:
        print(colorama.Fore.GREEN)
        print(
            f"Welcome Customer Manager {customersManager.firstname} {customersManager.lastname}!",
            colorama.Fore.WHITE,
        )
        show_customer_employee_manager_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                while True:
                    if hire_customer_employee() == True:
                        break
            case "2":
                fire_customer_employee()
                pass
            case "3":
                give_raise_customer_employee()
            case "4":
                show_all_customer_employees()
            case "5":
                show_all_customers()
            case "6":
                generate_top5_customers_report()
            case "7":
                show_account_info(customersManager)
            case "8":
                break
            case _:
                print(colorama.Fore.RED)
                print("Please only choose from options", colorama.Fore.WHITE)




def seller_employee_manager_panel(customersManager):
    while True:
        print(colorama.Fore.GREEN)
        print(
            f"Welcome Customer Manager {customersManager.firstname} {customersManager.lastname}!",
            colorama.Fore.WHITE,
        )
        show_customer_employee_manager_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                while True:
                    if hire_customer_employee() == True:
                        break
            case "2":
                fire_customer_employee()
                pass
            case "3":
                give_raise_customer_employee()
            case "4":
                show_all_customer_employees()
            case "5":
                show_all_customers()
            case "6":
                generate_top5_customers_report()
            case "7":
                show_account_info(customersManager)
            case "8":
                break
            case _:
                print(colorama.Fore.RED)
                print("Please only choose from options", colorama.Fore.WHITE)
                
                

def seller_employee_manager_panel(sellersManager):
    pass


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
        "Janan",
        "Jafarnezhad",
        "janan123",
        "Jananian@123",
        "18",
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
                    login, customer = Person.check_login(
                        "./Database/Customers.json", username, password
                    )
                    if login: 
                        customers_panel(customer)    
                       
                case "2":
                    login, seller = Person.check_login(
                        "./Database/Sellers.json", username, password
                    )
                    if login: 
                        sellers_panel(seller)
                    
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
                        customer_employee_manager_panel(customersManager)
                        login = True
                    else:
                        login = False
                case "6":
                    if (
                        username == sellersManager.username
                        and sellersManager.password
                        == Person.get_hash_Password(password)
                    ):
                        seller_employee_manager_panel(sellersManager)
                        login = True
                    else:
                        login = False
            if not login:
                print(colorama.Fore.RED)
                print("Wrong username or password",colorama.Fore.WHITE) 
        elif choice == "7":
            print(colorama.Fore.RED, "\nBye!\n", colorama.Fore.WHITE)
            break
        else:
            print(colorama.Fore.RED)
            print("Please only choose from options!", colorama.Fore.WHITE)


if __name__ == "__main__":
    main()
