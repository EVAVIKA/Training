from receiver import Bank 
from invoker import BankClient
class Command:
    def __init__(self, bank):
        self.bank = bank
    def execute(self):
        print("Команда не описана: " + type(self).__name__)
class PutCommand(Command):
    pass
    def execute(self):
        self.bank.receive_money()
class GetCommand(Command):
    pass  
class CreditCommand(Command):
    pass 
    def execute(self):
        self.bank.gave_credit()
        
if __name__ == '__main__':
    bank = Bank()
    c_put = PutCommand(bank)
    c_get = GetCommand(bank)
    c_credit = CreditCommand(bank)
    client = BankClient(c_put, c_get, c_credit)
    client.put_money()
    client.get_money()
    client._credit()
    
    