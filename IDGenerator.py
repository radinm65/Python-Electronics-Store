from FileCommands import FileCommands


class IDGenerator:
    def __init__(self, files):
        self.files = files if isinstance(files, list) else [files]
        self.current = self.get_last_id()
        
    def get_last_id(self):
        max_id = 0

        for file in self.files:
            try:
                data = FileCommands.get_file_data(file)

                for item in data:
                    if "id" in item and item["id"] > max_id:
                        max_id = item["id"]

            except FileNotFoundError:
                continue

        return max_id
        
    def next_id(self):
        self.current += 1
        return self.current
    

ticket_id_generator = IDGenerator([
    "./Database/CustomerTickets.json",
    "./Database/SellerTickets.json"
])

product_id_generator = IDGenerator([
    "./Database/ApprovedProducts.json",
    "./Database/UnapprovedProducts.json"
])

customer_id_generator = IDGenerator("./Database/Customers.json")

seller_id_generator = IDGenerator("./Database/Sellers.json")

seller_employee_id_generator = IDGenerator("./Database/SellerEmployees.json")

customer_employee_id_generator = IDGenerator("./Database/CustomerEmployees.json")