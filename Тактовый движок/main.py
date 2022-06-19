from datetime import *
from threading import Thread 

class Engine:
    def __init__(self, interval, func):
        self.i = timedelta(milliseconds = interval)
        self.f = func
        
    def tact(self):
        c = datetime.now()
        while True:
            t = datetime.now()
            if t < (c + self.i):
                continue
            self.f()
            c = datetime.now()
            
def test():
    print("Первый", datetime.now().time())
def test2():
    print("Второй", datetime.now().time())
   
engine1 = Engine(700, test)
engine2 = Engine(350, test2)

th_1, th_2 = Thread(target = engine1.tact), Thread(target = engine2.tact)

if __name__ == '__main__':
    th_1.start(), th_2.start()
    th_1.join(), th_2.join()

