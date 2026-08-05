from Classes.Person import Person
from Classes.Ticket import Ticket
from Validator import Validator 

class User(Person):
    def __init__(
        self, firstname, lastname, username, password, age, phone_num, address
    ):
        super().__init__(
            firstname, lastname, username, password, age, phone_num, address
        )
        self.balance = 0


    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        Validator.validate_balance(value)
        self.__balance = value
        
    @staticmethod
    def get_user_tickets(user_id, sender_type):
        user_tickets = []
        if sender_type == "customer":
            tickets = Ticket.get_sellers_tickets()
        else: 
            tickets = Ticket.get_customers_tickets()
            
        for ticket in tickets:
            if ticket["from_id"] == user_id:
                user_tickets.append(ticket)
        return user_tickets
            

    
       
