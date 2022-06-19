class Soda(object):
    def __init__(self, additional):
        self.additional = additional
    def show_my_drink(self):
        if type(self.additional) is Cherry:
            print("Газировка и " + self.additional.name + (" Уникальное свойство Вишнёвой газявы - ") + self.additional.unique)
        elif type(self.additional) is Lemon:
            print("Газировка и " + self.additional.name + (" Уникальное свойство Лимонной газявы - ") + self.additional.color)
        elif type(self.additional) is Additional:
            print("Газировка и " + self.additional.name)
        else: 
            print("Обычная газировка")
        
class Additional(object):
    def __init__(self, name):
        self.name = name
class Cherry(Additional):
    pass
    def __init__(self, name, unique):
        super().__init__(name)
        self.unique = unique
class Lemon(Additional):
    pass
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color 
        
if __name__ == '__main__':      
    caramel = Additional("Карамель", "Красная")
    coca_cola = Soda(caramel)
    coca_cola.show_my_drink()
    vanilla = Lemon("Лимон", "Желтая")
    lemonade = Soda(vanilla)
    lemonade.show_my_drink()