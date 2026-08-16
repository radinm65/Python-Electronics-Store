from datetime import datetime
from IDGenerator import ticket_id_generator
from FileCommands import FileCommands
from Validator import Validator


class Ticket:

    def __init__(self, from_name, from_id, request, sender_type, save, response=""):
        self.id = ticket_id_generator.next_id()
        self.from_name = from_name
        self.from_id = from_id
        self.request = request
        self.response = response
        self.sender_type = sender_type
        self.__date_created = datetime.today()
        if save:
            new_ticket = {
                "id": self.id,
                "from_name": self.from_name,
                "from_id": self.from_id,
                "request": self.request,
                "response": self.response,
                "sender_type": self.sender_type,
                "date_created": self.date_created.isoformat(),
            }
            FileCommands.add_data("./Database/Tickets.json", new_ticket)

    @property
    def request(self):
        return self.__request

    @request.setter
    def request(self, new_request):
        Validator.validate_ticket_request(new_request)
        self.__request = new_request

    @property
    def from_name(self):
        return self.__from_name

    @from_name.setter
    def from_name(self, new_from_name):
        Validator.validate_name(new_from_name)
        self.__from_name = new_from_name

    @property
    def date_created(self):
        return self.__date_created
    
    @property
    def sender_type(self):
        return self.__sender_type

    @sender_type.setter
    def sender_type(self, new_type):
        Validator.validate_sender_type(new_type)
        self.__sender_type = new_type
        
    @staticmethod    
    def get_all_tickets():
        return FileCommands.get_file_data("./Database/Tickets.json")
    
    @staticmethod    
    def get_sendertype_tickets(sender_type):
        user_tickets = []
        all_tickets = Ticket.get_all_tickets()
        for ticket in all_tickets:
            if ticket["sender_type"] == sender_type:
                user_tickets.append(ticket)
        return user_tickets
    
    @staticmethod    
    def get_unanswered_sendertype_tickets(sender_type):
        unanswered_tickets = []
        all_tickets = Ticket.get_all_tickets()
        for ticket in all_tickets:
            if ticket["sender_type"] == sender_type and ticket["response"] == "":
                unanswered_tickets.append(ticket)
        return unanswered_tickets
    
    @staticmethod
    def check_unanswered_ticketID(ticketID, sender_type):
        unanswered_tickets = Ticket.get_unanswered_sendertype_tickets(sender_type)
        for ut in unanswered_tickets:
            if ticketID == ut["id"]:
                return True
        return False
            
    
    @staticmethod
    def get_user_tickets(user_id, sender_type):
        user_tickets = []
        if sender_type == "customer":
            tickets = Ticket.get_sendertype_tickets("customer")
        else: 
            tickets = Ticket.get_sendertype_tickets("seller")
                
        for ticket in tickets:
            if ticket["from_id"] == user_id:
                user_tickets.append(ticket)
        return user_tickets

    @staticmethod
    def from_dict(ticket_dict):
        ticket =  Ticket(
            from_name=ticket_dict["from_name"],
            from_id=ticket_dict["from_id"],
            request=ticket_dict["request"],
            sender_type=ticket_dict["sender_type"],
            save=False,
            response=ticket_dict.get("response", "")
        )
        ticket.id = ticket_dict["id"]
        
        return ticket
    
    
    def __str__(self):
            return (
                f"ID: {self.id}\n"
                f"From: {self.from_name}\n"
                f"From ID: {self.from_id}\n"
                f"Request: {self.request}\n"
                f"Response: {self.response}\n"
                f"Date Created: {self.date_created}"
            )
