import json
import csv
import yaml

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_csv(file_path):
    test_data = []
    with open(file_path, mode='r', encoding='utf-8',) as file:
        reader = csv.DictReader(file)
        for row in reader():
            if row.get("params"):
                row["params"] = json.loads(row["params"].replace("'", '"'))
            if row.get("headers"):
                row["headers"] = json.loads(row["headers"].replace("'", '"'))
            test_data.append(row)
    return test_data

def load_yaml(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        test_data = yaml.safe_load(file)
    return test_data