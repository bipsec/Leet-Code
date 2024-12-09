class Bank:

    def __init__(self, balance):
        self.bank_acc = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            self.deposit(account1, money)
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.bank_acc):
            self.bank_acc[account - 1] += money
            return True

        return False

    def withdraw(self, account: int, money: int) -> bool:

        if 1 <= account <= len(self.bank_acc) and self.bank_acc[account - 1] >= money:
            self.bank_acc[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)


# Your Bank object will be instantiated and called as such:
obj = Bank([10, 100, 20, 50, 30])
param_1 = obj.transfer(5, 1, 20)
print(param_1)
param_2 = obj.deposit(5, 20)
print(param_2)
param_3 = obj.withdraw(3, 10)
print(param_3)
param_4 = obj.withdraw(3, 100)
print(param_4)
