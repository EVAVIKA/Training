from decorate import ColorDecorator, ShadowDecorator
from component import Square
if __name__ == "__main__":
    square = Square()
    square = ColorDecorator(square, "Красный")
    square = ShadowDecorator(square)
    square.show_info()