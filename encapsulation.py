class BankAccount:
    def __init__(self,name, balance):
        self.name = name #public attribute
        self._balance = balance #private attribute

    def get_balance(self):
        return self._balance

acc1=BankAccount("Rizwana", 10_000)
print(acc1.name,acc1.get_balance()) #accessing private attribute