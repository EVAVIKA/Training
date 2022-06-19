from component import IShape
class ShapeDecorator(IShape):
    def __init__(self, shape):
        self.shape = shape
    def show_info(self):
        self.shape.show_info()
        
class ColorDecorator(ShapeDecorator):
    def __init__(self, shape, color):
        super().__init__(shape) 
        self.color = color 
    def show_info(self):
        print(self.color + ' ')
        self.shape.show_info()
        
class ShadowDecorator(ShapeDecorator):
     def show_info(self):
        self.shape.show_info()
        print("С тенью")