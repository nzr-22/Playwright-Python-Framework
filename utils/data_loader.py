import json
import os

def load_json_data():
    # Gets the path to the data file dynamically
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", "test_data.json")
    
    with open(file_path) as f:
        return json.load(f)