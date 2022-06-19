class Man(object):
    def __init__(self):
        self.health = 100
        self.damage = 1
        self.stamina = 100
        self.eqipment = {"head": None, "left_hand": None, "right_hand": None, "body": None, "left_leg": None, "right_leg": None}
    def eqip_item(self, item):
        self.eqipment[item.type] = item
        
        