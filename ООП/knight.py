from man import Man 
class Knight(Man):
    def __init__(self, health):
        self.health = super().get_regular_health() + health
        self.attack = 7 
        self.is_alive = True