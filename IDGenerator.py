class IDGenerator:
    def __init__(self, start = 0):
        current = start
        
    def next_id(self):
        self.current += 1
        return self.current
    
ticket_id_generator = IDGenerator()
product_id_generator = IDGenerator()
customer_id_generator = IDGenerator()
seller_id_generator = IDGenerator()
seller_employee_id_generator = IDGenerator()
customer_employee_id_generator = IDGenerator()