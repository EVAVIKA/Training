class Item(object):
    def __init__(self, _type, name):
        self.strength = 100
        self.type = _type
        self.name = name
class Weapon(Item):
    pass
    def __init__(self, _type, name, damage):  
        super().__init__(_type, name)      
        self.damage = damage

class Clothes(Item):
    pass
    def __init__(self, _type, name, armor):
        super().__init__(_type, name)
        self.armor = armor 
class Eyes(Clothes):
    pass
    def __init__(self, _type, name, armor, color):
        super().__init__(_type, name, armor)
        self.color = color