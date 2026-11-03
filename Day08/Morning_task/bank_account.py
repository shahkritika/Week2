# A1: BankAccount with private balance, validated deposit and withdraw

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account({self.owner}) | Balance: ${self.__balance:.2f}"


# --- Test ---
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  # Should fail
print(acc)

