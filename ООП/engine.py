def fight(first, second):
    while first.is_alive and second.is_alive:     
        second.hit(first.attack)
        print("Первый нанес свой удар и оставил сопернику здоровья " + str(second.health))
        if not second.is_alive:
            break
        first.hit(second.attack)
        print("Второй нанес свой удар и оставил сопернику здоровья " + str(first.health))
    return True if first.is_alive else False