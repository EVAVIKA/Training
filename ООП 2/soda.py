class Soda(object):
    def __init__(self, additional):
        self.additional = additional
    def show_my_drink(self):
        if self.additional:
            print("Газировка и " + self.additional + ("Уникальное свойство - ") + self.unique)
        else: 
            print("Обычная газировка")
        
class Additional(object):
    def __init__(self, name, unique):
        self.name = name
        self.unique = unique
class Cherry(Additional):
    pass
    def __init__(self, name, unique):
        super().__init__(self, name, unique)
        unique = 'red'
