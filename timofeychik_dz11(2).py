class BankAccount:
    def __init__(self, interest_rate=0):
        self.__balance = 0
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Депозит: +{amount}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"Снятие: -{amount}")
        else:
            print("Недостаточно средств на счете.")

    def add_interest(self):
        interest = self.__balance * self.__interest_rate / 100
        self.__balance += interest
        self.__transactions.append(f"Начисление процентов: +{interest}")

    def history(self):
        for transaction in self.__transactions:
            print(transaction)

    def get_balance(self):
        return self.__balance


account = BankAccount(5)  

account.deposit(1000)  
account.withdraw(500)  
account.add_interest() 
account.history()  
print(account.get_balance())  