from abc import ABC, abstractmethod

class IFactory(ABC):
    @abstractmethod
    def create_a(self):
        pass
    @abstractmethod
    def create_b(self):
        pass
    
class IProductA(ABC):
    @abstractmethod
    def test_a(self):
        pass
       
class IProductB(ABC):
    @abstractmethod
    def test_b(self):
        pass

