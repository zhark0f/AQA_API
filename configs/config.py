import json
import os


def get_data(file_name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)) as file:
        return json.load(file)
