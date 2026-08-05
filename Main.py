import colorama
from CustomerManager import CustomerManager 
from SellerManager import SellerManager 
from Person import Person 
from Customer import Customer 
from Seller import Seller 
from CustomerEmployee import CustomerEmployee 
from SellerEmployee import SellerEmployee 

# Show Menus -------------------

def show_main_menu():
    print(
        "\nWelcome!\n\n"
        "1- Customer\n"
        "2- Seller\n"
        "3- Customer Employee\n"
        "4- Seller Employee\n"
        "5- Customer Manager\n"
        "6- Seller Manager\n"
        "7- Exit\n\n"
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
    print(
            "1- Hire Customer Employee\n"
            "2- Fire Customer Employee\n"
            "3- Give Raise\n"
            "4- See All Customer Employees\n"
            "5- See All Customers\n"
            "6- Get top 5 Customers .xlsx Report\n"
            "7- See Account Info\n"
            "8- Back\n"
        )

def show_seller_employee_manager_menu():
    print(
            "1- Hire seller Employee\n"
            "2- Fire seller Employee\n"
            "3- Give Raise\n"
            "4- See All seller Employees\n"
            "5- See All sellers\n"
            "6- Get top 5 sellers .xlsx Report\n"
            "7- See Account Info\n"
            "8- Back\n"
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

def customer_employee_manager_panel(customersManager):
    
        
        

def seller_employee_manager_panel(sellersManager):
    pass

def main():
    
    customersManager = CustomerManager("Radin", "Motahhary", "radinm123", "Radinian@123", "21", "9379499511", "Karaj_ mehrshahr")
    sellersManager = SellerManager("Janan", "Jafarnezhad", "janan123", "Radinian@123", "18" , "9379499511", "Karaj_ mehrshahr")

    while True:
        show_main_menu()
        choice = input("Please choose:\n")
        
        if choice == "7":
            print("\nBye!\n")
            break
        
        username = input("Please enter your username:\n")
        password = input("Please enter your password:\n")
        match choice:
            case "1":
                login, customer = Person.check_login("./Customers.json", username, password)
                customers_panel(customer) if login else print("Wrong username or password")
            case "2":
                login, seller = Person.check_login("./Sellers.json", username, password)
                sellers_panel(seller) if login else print("Wrong username or password")
            case "3":
                login, customer_employee = Person.check_login("./CustomerEmployees.json", username, password)
                customer_employee_panel(customer_employee) if login else print("Wrong username or password")
            case "4":
                login, seller_employee = Person.check_login("./SellerEmployees.json", username, password)
                seller_employee_panel(seller_employee) if login else print("Wrong username or password")
            case "5":
                if username == customersManager.username and customersManager.password == Person.get_hash_Password(password):
                    customer_employee_manager_panel(customersManager)
                else:
                    print("Wrong username or password")
            case "6":
                if username == sellersManager.username and sellersManager.password == Person.get_hash_Password(password):
                    seller_employee_manager_panel(sellersManager)
                else:
                    print("Wrong username or password")
            case _:
                print("Please only choose from options")
            
                
                
                



if __name__ == "__main__":
    main()