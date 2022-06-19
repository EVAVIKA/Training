from abc import ABC, abstractmethod


class Switcher:
    def __init__(self):
        self.state = False
        
    def switch(self, lamp):     
        self.state = not self.state
        lamp.switch_lamp()
    

class Lamp:
    def __init__(self, switcher1, switcher2):
        self.switcher1 = switcher1
        self.switcher2 = switcher2
        
    def switch_lamp(self):
        if switcher1.state != switcher2.state:
            self.turn_on()
        elif switcher1.state == switcher2.state:
            self.turn_off()    
            
    def turn_on(self):
        print("Лампочка горит")

    def turn_off(self):
        print("Не знаю горит ли лампочка, я её не вижу, темно")
        
if __name__ == '__main__':
    
    switcher1 = Switcher()
    switcher2 = Switcher()
    lamp = Lamp(switcher1, switcher2)
    switcher1.switch(lamp)
    switcher1.switch(lamp)
    switcher2.switch(lamp)
    switcher1.switch(lamp)
    switcher2.switch(lamp)
    