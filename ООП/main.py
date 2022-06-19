from engine import fight
from knight import Knight
from warrior import Warrior
from mage import (Mage, Staff)
if __name__ == '__main__':
    chuck = Knight(80)
    # bruce = Warrior(5)
    # print("Победил первый" if fight(chuck, bruce) else "Победил второй")
    magic_stick = Staff(10, 10)
    harry = Mage(magic_stick)
    print("Победил первый" if fight(chuck, harry) else "Победил второй")