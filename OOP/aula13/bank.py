import persons
import accounts as acc


class Bank:
    def __init__(
            self,
            agencies: list[int] | None = None,
            clients: list[persons.Client] | None = None,
            accounts: list[acc.Account] | None = None
    ):
        self.agencies = agencies or []
        self.accounts = accounts or []
        self.clients = clients or []
    
    def _check_agency(self, account):
        if account.agency in self.agencies:
            return True
        return False
    
    def _check_client(self, client):
        if client in self.clients:
            return True
        return False
    
    def _check_account(self, account):
        if account in self.accounts:
            return True
        return False
    
    def _check_client_account(self, client, account):
        if account is client.account:
            return True
        return False
    
    def authenticate(self, client: persons.Client, account: acc.Account):
        return self._check_agency(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_client_account(client,account)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'\n\t{self.agencies!r},\n\t{self.accounts!r},\n\t{self.clients!r}\n'
        return f'{class_name}({attrs})'

if __name__ == "__main__":
    c1 = persons.Client("John Doe", 34)
    ca1 = acc.CheckingAccount(111, 222, 0, 0)
    c1.account = ca1
    
    c2 = persons.Client("John Doe", 34)
    sa2 = acc.SavingAccount(222, 554, 0)
    c2.account = sa2
    
    bank = Bank()
    bank.clients.extend([c1,c2])
    bank.accounts.extend([sa2,ca1])
    bank.agencies.extend([111,222])
    print(bank)
    if bank.authenticate(c1,ca1):
        ca1.deposit(10)
        print(c1.account)
    
   