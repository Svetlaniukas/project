import json
import logging
import os


def save_to_json(data, filename='form_data.json'):
    """"The save_to_json function is a robust Python utility designed for serializing and saving data to a JSON file,
    while ensuring smooth error handling and logging. It accepts two parameters: the data to be saved and an optional filename,
    defaulting to 'form_data.json'. The function attempts to open the specified file in write mode and serialize the data into JSON format 
    with neat indentation for readability. If the process succeeds,
    it logs an informational message and returns True as a confirmation of success. 
    In cases of exceptions, such as file access issues, it catches the error, 
    logs a detailed error message, and returns False to indicate failure. 
    This careful approach to error handling and feedback makes save_to_json a 
    reliable tool for data storage in JSON format, aiding in maintaining data integrity and facilitating debugging."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data saved to {filename}")
        return True
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        return False


def save_order(order_data):
    """The save_order function is specifically designed for handling the storage of order data in a JSON file
    in a thread-safe manner using Python's threading and file handling capabilities. 
    It begins by defining a file path for 'orders.json'. If this file doesn't exist,
    the function creates it and initializes it with an empty list,
    ensuring there's a structure in place for storing order data.
    """
    file_path = 'orders.json'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)

    try:
        with open(file_path, 'r+') as file:
            orders = json.load(file)
            orders.append(order_data)
            file.seek(0)
            json.dump(orders, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def convert_from_record_to_int(record):
    """function is convert data to int
    """
    data_record = record[0]
    record_convert_to_int = data_record[0]
    return int(record_convert_to_int)
