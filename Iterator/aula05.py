
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()


persons = ["John", "Emily", "William", "Mia"]

shirts = [
    ["black", "white"],
    ["s", "m", "l"],
]

print("Combinations")
print_iter(combinations(persons,2))

print("Permutations")
print_iter(permutations(persons,2))

print("Product")
print_iter(product(*shirts))