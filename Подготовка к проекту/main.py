from lib import * 
import datetime as dt
import os 

class Balance:
    __balance = 0 
    def get_balance(): 
        if Balance.__balance == 0:
            Balance.set_prev()
        return Balance.__balance
        
    def set_prev():
        files = [file for file in os.listdir() if (os.path.isfile(file) and 'json' in file.split('.'))]
        try:
            lastfile = max(files, key = os.path.getctime)[:-5]
            file = EnJSONeer.read_from_JSON(lastfile)
            Balance.clear_balance()
            Balance.add_balance(file.balance)
        except:
            Balance.clear_balance()        
        return Balance.__balance 
        
    def add_balance(value):
        Balance.__balance += value
    def minus_balance(value):
        Balance.__balance -= value 
    def clear_balance():
        Balance.__balance = 0
   
class Traffic:
    def __init__(self, add_type, value, date = None):
        self.add_type = add_type 
        self.date = str(dt.datetime.now())[:-7].replace(':', '.') if date == None else date
        self.value = value
        self.balance = Balance.get_balance()
         
class Invest:
    def __init__(self, name_invset, time_invest, value, percent = 0.1):
        span = Span('Инвестиция ' + name_invset, value)
        span.save_doc()
        percent *= 100
        day_percent = percent / 360
        for day in range(time_invest):
            value += value * day_percent/100
        value = round(value, 2)
        addition = Addition('invest\\Инвустиция ' + name_invset, value,  str(dt.datetime.now() + dt.timedelta(days = time_invest))[:-7].replace(':', '.') )
        addition.save_doc()
        
        
class Span(Traffic):
    
    def save_doc(self):
        Balance.minus_balance(self.value)
        self.balance = Balance.get_balance()
        EnJSONeer.save_to_JSON(self, self.add_type + ' от ' + self.date) 
    
class Addition(Traffic):
    
    def save_doc(self):
        Balance.add_balance(self.value)
        self.balance = Balance.get_balance()
        EnJSONeer.save_to_JSON(self, self.add_type + ' от ' + self.date)
        
invest = Invest("ALPHA", 360, 100000)