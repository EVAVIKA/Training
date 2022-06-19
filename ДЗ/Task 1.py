from abc import abstractmethod

class ITextBuilder:
    @abstractmethod
    def add_text(self, value):
        pass
    
    @abstractmethod
    def add_new_line(self, value):
        pass

    @abstractmethod
    def add_dollar_symbol(self):
        pass

    @abstractmethod
    def get_text(self):
        pass
    
class SomeBuilder(ITextBuilder):
    def __init__(self):
        self.text = ""
        
    def add_text(self, value):
        self.text += value
   
    def add_new_line(self, value):
        self.text += '\n' + value

    def add_dollar_symbol(self):
        self.text += '$'
        
    def get_text(self):
        return self.text
    
if __name__ == "__main__":
    Builder = SomeBuilder()
    Builder.add_text("sometext")
    Builder.add_new_line("textatnewline")
    Builder.add_dollar_symbol()
    print(Builder.get_text())