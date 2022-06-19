from inspect import stack


class CollectionManager:
    def __init__(self):
        self.clear()

    def push(self, value):
        self.collection = self.Element(self.collection, value)
        self.collection.index = self.collection.parent.index + 1
        self.collection.parent.child = self.collection
        if self.collection.parent.first == object:
            self.collection.first = self.collection
        else:
            self.collection.first = self.collection.parent.first

    def pop(self):
        if self.collection.parent == object:
            return "Стек пуст"
        if self.collection.index == 0:
            self.collection.first = object
        result = self.collection.value
        self.collection.parent.first = self.collection.first
        self.collection = self.collection.parent
        return result

    def last(self):
        return self.collection.value
    
    def first_element(self):
        return self.collection.first

    def first(self):
        return self.first_element.value

    def len(self):
        return self.collection.index + 1

    def get_element_by_index(self, index):
        len = self.len() - 1
        if index > len:
            return 'За пределами диапаозона'
        if index == 0:
            return self.first_element()
        if (len // 2) < index:
            result = self.collection
            while len > 0 and len != index:
                len -= 1
                result = result.parent
        else:   
            i = 0
            result = self.collection.first
            while len > i and i != index:
                i += 1
                result = result.child
        return result 

    def index(self, index):
        return self.get_element_by_index(index).value


    def to_list(self, with_clear=False):
        result = []
        len = self.len() - 1
        element = self.collection
        while len >= 0:
            if with_clear:
                result.insert(0, self.pop())
            else:
                result.insert(0, element.value)
                element = element.parent
            len -= 1

        return result

    def clear(self):
        self.collection = self.Element()
    
    def insert(self, index, value):
        if index == self.len():
            self.push(value)
            return 
        if index > self.len():
            print('Ошибка, за пределами диапазона')
            return
        new_element = self.Element(object, value)
        current_element = self.get_element_by_index(index-1) if index > 0 else self.first_element().parent
        next_to_element = current_element.child
        new_element.index = index        
        current_element.child = new_element if index > 0 else object
        new_element.child = next_to_element
        next_to_element.parent = new_element
        new_element.parent = current_element
        while next_to_element != object:
            next_to_element.index += 1
            if index == 0:
                next_to_element.first = new_element
            next_to_element = next_to_element.child            
        
    class Element:
        def __init__(self, parent=object, value=object):
            self.parent = parent
            self.child = object 
            self.value = value
            self.first = object
            self.index = -1
         

def get_next(elem):
    return elem.child

if __name__ == '__main__':
    stack = CollectionManager()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.insert(6, 9)
    stack.insert(1568, 999)
    first = stack.get_element_by_index(0)
    i = 0
    while i < stack.len():
        print(first.index, "|", first.value)
        first = get_next(first)
        i += 1