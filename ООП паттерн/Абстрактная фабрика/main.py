from concrete import *
from enumerable import Fabrics

def start_factory(factory):
    product_a = factory.create_a()
    product_b = factory.create_b()
    product_a.test_a()
    product_b.test_b()
def create_factories():
    Factory1()
    Factory2()
    Factory3()
    Factory4()
    Factory5()
if __name__ == '__main__':
    create_factories()
    iterator = Fabrics.get_fabrics().get_iterator()
    while iterator.is_done() == False:
        factory = iterator.current_item()
        start_factory(factory)
        iterator.next()
        
    