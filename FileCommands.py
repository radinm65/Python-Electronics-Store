import os
import json

class FileCommands:
    
    @staticmethod
    def get_file_data(path):
        try:
            if not os.path.exists(path):
                with open(path, "w") as file:
                    json.dump([], file)
            with open(path, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(e)
            return []


    @staticmethod
    def save_file_data(path, datas):
        try:
            with open(path, 'w') as file:
                json.dump(datas, file, indent=4)
                return True
        except Exception as e:
            print(e)
            return False
            
            
    @staticmethod
    def add_data(path, new_data):
        try: 
            all_datas = FileCommands.get_file_data(path)
            all_datas.append(new_data)
            return FileCommands.save_file_data(path, all_datas)
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def delete_data(path, data_id):
        try: 
            datas = FileCommands.get_file_data(path)
            datas = [ data for data in datas if data["id"] != data_id]
            return FileCommands.save_file_data(path, datas)
        except Exception as e:
            print(e)
            return False