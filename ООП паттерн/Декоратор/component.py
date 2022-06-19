from abc import ABC, abstractclassmethod, abstractmethod 

class IShape(ABC):
    @abstractmethod 
    def show_info(self):
        pass 
    
class Square(IShape):
    def show_info(self):
        print('Квадрат')
        