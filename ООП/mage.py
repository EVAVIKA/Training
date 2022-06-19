from man import Man 
class Mage(Man):
    def __init__(self, staff):
        self.health = super().get_regular_health() * staff.health_power
        self.attack = staff.attack_power
        self.is_alive = True
class Staff(object):
    def __init__(self, health_power, attack_power):
        self.health_power = health_power
        self.attack_power = attack_power