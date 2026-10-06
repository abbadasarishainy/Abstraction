from abc import ABC,abstractmethod
class Acc(ABC):
    @abstractmethod
    def creation(self):
        pass
    @abstractmethod
    def Deposit(self):
        pass
    def withdraw(self):
        pass
    @abstractmethod
    def display(self):
        pass
class Bankaccount(Acc):
    def creation(self):
        print("Account creation")
    def Deposit(self):
        print("Amount Deposit")
    def withdraw(self):
        print("Amount withdraw")
    def display(self):
        print("Display")
s=Bankaccount()
s.creation()
s.Deposit()
s.withdraw()
s.display()
