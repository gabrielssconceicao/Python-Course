import accounts


class Person:
    
    def __init__(self, name:str, age: int):
        self._name = name
        self._age = age
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self,value:str)-> None:
        self._name = value
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.name!r}, {self.age!r}'
        return f'{class_name}({attrs})'


class Client(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account: accounts.Account | None = None
        
        
if __name__ == "__main__":
    c1 = Client("John Doe", 34)
    c1.account = accounts.CheckingAccount(111,222,0,0)
    print(c1)
    print(c1.account)
    
    c2 = Client("John Doe", 34)
    c2.account = accounts.SavingAccount(111, 222, 0)
    print(c2)
    print(c2.account)