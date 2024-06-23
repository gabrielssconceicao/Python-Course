from sys import getsizeof

# is in memory
lista = [n for n in range(1_000_000)]

generator = (n for n in range(1_000_000))

print(getsizeof(lista))
print(getsizeof(generator))

