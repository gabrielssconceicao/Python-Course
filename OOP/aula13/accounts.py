from abc import ABC, abstractmethod


class Account(ABC):
    
    def __init__(self, agency: int, account: int, balance:float=0):
        self.agency = agency
        self.account = account
        self.balance = balance
    
    @abstractmethod
    def withdraw(self, value):
        pass
    
    def deposit(self, value: float) -> None:
        self.balance += value
        self.details(f"Deposit: {value}")
    
    def details(self, msg='') -> None:
        print(f"Your balance is {self.balance:.2f} ({msg})")
        print('-'*20)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agency!r}, {self.account!r}, {self.balance!r}'
        return f'{class_name}({attrs})'
        
class SavingAccount(Account):
    
    def withdraw(self, value: float) -> float | None:
        value_after_withdraw = self.balance - value
        
        if value_after_withdraw >= 0:
            self.balance -= value
            self.details(f"Withdraw: {value}")
            return self.balance
        
        print("Cannot withdraw the desired value")
        self.details(f"withdrawal denied: {value}")


class CheckingAccount(Account):
    
    def __init__(self, agency, account, balance=0, limit=0):
        super().__init__(agency, account, balance)
        self.limit = limit
    
    def withdraw(self, value: float) -> float | None:
        value_after_withdraw = self.balance - value
        max_limit = -self.limit
        
        if value_after_withdraw >= max_limit:
            self.balance -= value
            self.details(f"Withdraw: {value}")
            return self.balance
        
        print("Cannot withdraw the desired value")
        print(f"Your limit is {-self.limit:.2f}")
        self.details(f"withdrawal denied: {value}")
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = (f'{self.agency!r}, {self.account!r}, {self.balance!r}, '
                 f'{self.limit!r}')
        return f'{class_name}({attrs})'
        
if __name__ == "__main__":
    sa1 = SavingAccount(123,988)
    sa1.withdraw(3)
    sa1.deposit(3)
    sa1.withdraw(3)
    
    ca1 = CheckingAccount(3435,34463,limit=100)
    ca1.withdraw(100)
    ca1.withdraw(1)
    ca1.deposit(3)
    ca1.withdraw(3)
