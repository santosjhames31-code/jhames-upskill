"Encapsulation Create a BankAccount class with a private __balance. Add deposit(), withdraw() (reject if insufficient funds), and get_balance()."

class BankAccount:

    def __init__(self, __balance):
        self.__balance = __balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if(self.__balance > amount):
            self.__balance = self.__balance - amount
        else:
            print(f"Insufficient balance : {self.__balance}")

bank = BankAccount(599)

balance = bank.getBalance()
print(balance)


bank.deposit(500)
balance = bank.getBalance()
print(balance)

bank.withdraw(10000)
balance = bank.getBalance()
print(balance)

bank.withdraw(500)
balance = bank.getBalance()
print(balance)
