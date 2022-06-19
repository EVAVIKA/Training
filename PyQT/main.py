import re
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication


class UI:
    def __init__(self):
        Form, Window = uic.loadUiType('calc.ui')

        self.Window = Window()
        self.Form = Form()
        self.Form.setupUi(self.Window)

    def show_window(self):
        self.Window.show()


class Calc:
    def __init__(self):
        self.clear()

    def add(self, sym):
        self.input += str(sym)
        
    def sqrt(self, x):
        return x**0.5

    def equals(self):
        result = ''
        sqrt = lambda x: self.sqrt(x)
        try:
            result = eval(self.input)
        except:
            result = 'Неправильный ввод'
        return result

    def clear(self):
        self.input = ''

    def backspace(self):
        self.input = self.input[:len(self.input) - 1] 

class App:
    def __init__(self):
        self.app = QApplication([])
        self.ui = UI()
        self.calc = Calc()

        form = self.ui.Form
        self.answer = form.lbl_answer

        self.add_event(form.btn_0, 'clicked', lambda: self.oninput('0'))
        self.add_event(form.btn_1, 'clicked', lambda: self.oninput('1'))
        self.add_event(form.btn_2, 'clicked', lambda: self.oninput('2'))
        self.add_event(form.btn_3, 'clicked', lambda: self.oninput('3'))
        self.add_event(form.btn_4, 'clicked', lambda: self.oninput('4'))
        self.add_event(form.btn_5, 'clicked', lambda: self.oninput('5'))
        self.add_event(form.btn_6, 'clicked', lambda: self.oninput('6'))
        self.add_event(form.btn_7, 'clicked', lambda: self.oninput('7'))
        self.add_event(form.btn_8, 'clicked', lambda: self.oninput('8'))
        self.add_event(form.btn_9, 'clicked', lambda: self.oninput('9'))
        self.add_event(form.btn_plus, 'clicked', lambda: self.oninput('+'))
        self.add_event(form.btn_minus, 'clicked', lambda: self.oninput('-'))
        self.add_event(form.btn_mult, 'clicked', lambda: self.oninput('*'))
        self.add_event(form.btn_div, 'clicked', lambda: self.oninput('/'))
        self.add_event(form.btn_equals, 'clicked', lambda: self.onequals())
        self.add_event(form.btn_clear, 'clicked', lambda: self.onclear())
        self.add_event(form.btn_left_bracket, 'clicked', lambda: self.oninput('('))
        self.add_event(form.btn_right_bracket, 'clicked', lambda: self.oninput(')'))
        self.add_event(form.btn_square_root, 'clicked', lambda: self.oninput('sqrt('))
        self.add_event(form.btn_square_power, 'clicked', lambda: self.oninput('**2'))
        self.add_event(form.btn_dot, 'clicked', lambda: self.oninput('.'))
        self.add_event(form.btn_backspace, 'clicked', lambda: self.onbackspace())
        

    def refreshText(self, answer = None):
        if answer == None: self.answer.setText(self.calc.input)
        else: self.answer.setText(str(answer))

    def onbackspace(self):
        self.calc.backspace()
        self.refreshText()

    def oninput(self, sym):
        self.calc.add(sym)
        self.refreshText()
        
    def onequals(self):
        self.refreshText(self.calc.equals())
        
    def onclear(self):
        self.calc.clear() 
        self.refreshText()
        
    def start_app(self):
        self.ui.show_window()
        self.app.exec()

    def add_event(self, obj, name_event, handler):
        obj_event = getattr(obj, name_event)
        obj_event.connect(handler)


app = App()
app.start_app()
