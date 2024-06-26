from collections.abc import Sequence


class MyList(Sequence):

    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0
    
    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1
    
    def __len__(self):
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        
        value = self._data[self._next_index]
        self._next_index += 1
        return value
        
        
if __name__ == "__main__":
    lista = MyList()
    lista.append("Mary", "Helen")
    lista.append("Louis", "Bob","Joe")
    lista[0] = "__setitem__"
    print(lista[0])
    print(len(lista))
    print("-"*20)
    for item in lista:
        print(item)
    
    print("-"*20)

    for i, e in enumerate(lista):
        print(i, e)
    