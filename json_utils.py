import json


def json_sum_of_all(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return sum(int(row[1]) for row in data)


def json_to_str(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return "\n".join(f"{i + 1}. {item[0]} - {item[1]}" for i, item in enumerate(data))


def json_for_one_item(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data[0][0]


def create_dump(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)
