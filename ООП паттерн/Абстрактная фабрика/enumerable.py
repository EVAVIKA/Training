from abc import ABC, abstractmethod

class EIterator(ABC):
    @abstractmethod
    def first(self):
        pass    
    @abstractmethod
    def next(self):
        pass   
    @abstractmethod
    def is_done(self):
        pass     
    @abstractmethod
    def current_item(self): 
        pass
    @abstractmethod
    def add_item(self, item):
        pass
    
class EAggeregate(ABC):
    @abstractmethod
    def get_iterator(self):
        pass
    
class Fabrics(EAggeregate):
    __instance = 0
    @classmethod 
    def get_fabrics(_class):
        if Fabrics.__instance == 0:
            Fabrics.__instance = Fabrics()
        return Fabrics.__instance    
    def __init__(self):
        self._fabrics = []
    def get_iterator(self):
        return Fabrics.Iterator(self)
    class Iterator(EIterator):
        def __init__(self, parent):
            self.__index = 0
            self.__parent = parent 
        def first(self):
            self.__index = 0
        def next(self):
            self.__index += 1
        def set_index(self, index):
            self.__index = index
        def prelast(self):
            self.__index = len(self.__parent._fabrics) - 2
        def is_done(self):
            return self.__index >= len(self.__parent._fabrics)
        def current_item(self):
            return self.__parent._fabrics[self.__index]
        def add_item(self, item):
            self.__parent._fabrics.append(item)
        def delete(self, index):
            self.__parent._fabrics = self.__parent._fabrics[:index] + \
                                     self.__parent._fabrics[index+1:]
                                     
        