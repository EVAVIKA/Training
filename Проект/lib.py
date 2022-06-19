import json
from types import SimpleNamespace

class EnJSONeer:
    
    def save_to_JSON(data, filename):
        with open(filename + ".json", 'w') as text_file:
             text_file.write(EnJSONeer.__get_json(data))

    def read_from_JSON(filename):
        with open(filename + ".json", 'r') as text_file:
            data = text_file.read()
            return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    
    def __get_json(data):
        return json.dumps(data, default=lambda o: o.__dict__, sort_keys=True)