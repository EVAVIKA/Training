#abstract product
class Employee:
    def testmessage(self):
        print("Работник")

#concrete product
class Manager(Employee):
    def testmessage(self):
        print("Менеджер")

class Developer(Employee):
    def testmessage(self):
        print("Разработчик")
        
#///////////////////////

class EmployeeFabric:
    def create_employee(self):
        return Employee()
    def test(self):
        self.create_employee().testmessage()
        
class ManagerFabric(EmployeeFabric):
    def create_employee(self):
        return Manager()
    
class DeveloperFabric(EmployeeFabric):
    def create_employee(self):
        return Developer()
        
if __name__ == "__main__":
    fabric = ManagerFabric()
    fabric.test()
    fabric = EmployeeFabric()
    fabric.test()
    fabric = DeveloperFabric()
    fabric.test()