import json


class Loader:

    @staticmethod
    def read_file(input_text: str):
        path = input(input_text)
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
