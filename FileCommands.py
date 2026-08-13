import os
import json


class FileCommands:

    @staticmethod
    def get_file_data(path):
        if not os.path.exists(path):
            with open(path, "w") as file:
                json.dump([], file)
        with open(path, "r") as file:
            data = json.load(file)
        return data


    @staticmethod
    def save_file_data(path, datas):
        with open(path, "w") as file:
            json.dump(datas, file, indent=4)
            return True


    @staticmethod
    def add_data(path, new_data):
        all_datas = FileCommands.get_file_data(path)
        all_datas.append(new_data)
        return FileCommands.save_file_data(path, all_datas)


    @staticmethod
    def delete_data(path, data_id):

        datas = FileCommands.get_file_data(path)

        data_id = int(data_id)

        if not any(data["id"] == data_id for data in datas):
            raise ValueError("ID not found.")

        datas = [data for data in datas if data["id"] != data_id]

        return FileCommands.save_file_data(path, datas)
    
    
    @staticmethod
    def edit_data(path, json_obj):

        datas = FileCommands.get_file_data(path)

        data_id = json_obj["id"]

        if not any(data["id"] == data_id for data in datas):
            raise ValueError("ID not found.")

        for data in datas:
            if data["id"] == data_id:
                data.update(json_obj)
                break

        return FileCommands.save_file_data(path, datas)
