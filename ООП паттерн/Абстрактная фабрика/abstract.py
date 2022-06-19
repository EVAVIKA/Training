from abc import ABC, abstractmethod 

class IFactory(ABC):
    @abstractmethod
    def create_a(self):
        pass
    @abstractmethod
    def create_b(self):
        pass

class ProductA(ABC):
    @abstractmethod
    def test_a(self):
        pass
     
class ProductB(ABC):
    @abstractmethod
    def test_b(self):
        pass