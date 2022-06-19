import json

class Test:
    def __init__(self):
        self.x = 2

class Example:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.test = Test()

    def get_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


example = Example(1, 2, 3)
print(example.get_json())