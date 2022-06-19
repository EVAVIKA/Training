class Man(object):
    def get_regular_health(self):
        return 10 
    def check_alive(self):
        self.is_alive = self.health > 0
        if self.is_alive == False: 
            self.health = 0
    def hit(self, damage):
        self.health -= damage 
        self.check_alive()