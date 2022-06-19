from man import Man 
class Warrior(Man):
    def __init__(self, attack):
        self.health = super().get_regular_health() * 5
        self.attack = attack
        self.is_alive = True