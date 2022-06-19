from abstract import *
from enumerable import Fabrics


class MainFactory:
    def __init__(self, child):
        Fabrics.get_fabrics().get_iterator().add_item(child)


class Factory1(MainFactory, IFactory):
    def __init__(self):
        super().__init__(self)

    def create_a(self):
        return ProductA1()

    def create_b(self):
        return ProductB1()


class Factory2(MainFactory, IFactory):
    def __init__(self):
        super().__init__(self)

    def create_a(self):
        return ProductA2()

    def create_b(self):
        return ProductB2()


class Factory3(MainFactory, IFactory):
    def __init__(self):
        super().__init__(self)

    def create_a(self):
        return ProductA1()

    def create_b(self):
        return ProductB2()


class Factory4(MainFactory, IFactory):
    def __init__(self):
        super().__init__(self)

    def create_a(self):
        return ProductA3()

    def create_b(self):
        return ProductB3()

class Factory5(MainFactory, IFactory):
    def __init__(self):
        super().__init__(self)

    def create_a(self):
        return ProductA2()

    def create_b(self):
        return ProductB3()

class ProductA1(ProductA):
    def test_a(self):
        print('Продукт А1')


class ProductA2(ProductA):
    def test_a(self):
        print('Продукт А2')


class ProductA3(ProductA):
    def test_a(self):
        print('Продукт А3')


class ProductB1(ProductB):
    def test_b(self):
        print('Продукт B1')


class ProductB2(ProductB):
    def test_b(self):
        print('Продукт B2')


class ProductB3(ProductB):
    def test_b(self):
        print('Продукт B3')
