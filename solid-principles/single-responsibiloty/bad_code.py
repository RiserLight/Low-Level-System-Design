class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount))
        else:
            raise ValueError("Insufficient funds")

    def send_notification(self, message):
        # Code to send notification to the user
        pass

    def generate_report(self):
        # Code to generate a report of the account transactions
        pass