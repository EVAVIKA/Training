class BankClient:
    def __init__(self, c_put, c_get, c_credit):
        self.__put = c_put
        self.__get = c_get 
        self.__credit = c_credit
    def put_money(self):
        self.__put.execute()
    def get_money(self):
        self.__get.execute()
    def _credit(self):
        self.__credit.execute()
        