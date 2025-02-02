from exceptions import InsufficientFundsError

class Account:
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError(f"Niewystarczające środki. Aktualne saldo: {self.balance}, wymagana kwota: {amount}.")
        self.balance -= amount

    async def transfer(self, to_account: "Account", amount: float):
        if amount > self.balance:
            raise InsufficientFundsError("Transfer nie powiódł się z powodu braku środków.")
        self.balance -= amount
        to_account.deposit(amount)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, owner: str, initial_balance: float = 0.0):
        if account_number in self.accounts:
            raise ValueError("Konto o podanym numerze już istnieje.")
        self.accounts[account_number] = Account(account_number, owner, initial_balance)

    def get_account(self, account_number: str) -> Account:
        if account_number not in self.accounts:
            raise ValueError(f"Nie znaleziono konta o numerze {account_number}.")
        return self.accounts[account_number]

    async def process_transaction(self, transaction_func):
        await transaction_func()
