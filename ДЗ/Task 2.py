from abc import abstractmethod

class ICollectionManager:
    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

class Collection:
    def __init__(self, parent = object, value = object):  # по умолчанию значения - пустые объекты
        self.parent = parent  # предыдущий экземпляр стека
        self.value = value  # значение текущего экземпляра стека

class CollectionManager(ICollectionManager):
    def __init__(self, collection):
        self.collection = Collection()
    def push(self, value):
        if value == 1:
            print("Зеленая") 
        elif value == 2:
            print("Красная")
        elif value == 3:
            print("Синяя")
        else:
            print('Стек пуст')
        
    def pop(self):
        
        
if __name__ == "__main__":
    stack = CollectionManager()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1
    print(stack.pop())  # "Стек пуст"
