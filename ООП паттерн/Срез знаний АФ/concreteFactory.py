from iFactory import *


class Factory(IFactory):
    def create_a(self):
        return ProductA()

    def create_b(self):
        return ProductB()


class Factory2(Factory):
    pass
    def create_a1(self):
        return ProductA1()

    def create_b1(self):
        return ProductB1()

class Factory3(Factory2):
    def create_a1(self):
        return ProductNone()
    def create_b5(self):
        return ProductB5()

class CProductA(IProductA):
    def test_a(self):
        print('Продукта нет')

class CProductB(IProductB):
    def test_b(self):
        print('Продукта нет')

class ProductNone(CProductA, CProductB):
    pass
    def seo(self):
        print("Рекламное место свободно")

class ProductA(CProductA):
    def test_a(self):
        print('Продукт а')


class ProductB(CProductB):
    def test_b(self):
        print('Продукт b')
        
class ProductA1(CProductA):
    def test_a(self):
        print('Продукт а1')


class ProductB1(CProductB):
    def test_b(self):
        print('Продукт b1')

class ProductB5(CProductB):
    def test_b(self):
        print('Продукт b5')