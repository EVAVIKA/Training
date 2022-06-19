from engine import fight
from man import Man
from item import (Weapon, Clothes, Eyes)

if __name__ == '__main__':
    vasy = Man()
    hat = Clothes('head', "Шляпа", 10)
    rubha = Clothes('body', "Рубаха", 120)
    sword = Weapon('left_hand', "Меч",111)
    blue_eye = Eyes('head', 'голубые глазки :3', 0, "bule")
    vasy.eqip_item(hat)
    vasy.eqip_item(rubha)
    vasy.eqip_item(sword)
    vasy.eqip_item(blue_eye)
    for item in vasy.eqipment:
        item = vasy.eqipment[item]
        if type(item) is Clothes:
            print("Эта одежда ", item.name, item.armor)
        elif type(item) is Weapon:
            print("Это оружие ", item.name, item.damage)
        elif type(item) is Eyes:
            print("Вы не понимаете, это другое... ", item.name, item.armor, item.color)
