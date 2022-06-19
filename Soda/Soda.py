from soda import Soda 
from soda import Additional

if __name__ == '__main__':      
    caramel = Additional("Карамель", "Сладкая")
    coca_cola = Soda(caramel)
    coca_cola.show_my_drink() # принтуется: "Газировка и Карамель. Уникальное свойство - Сладкая"