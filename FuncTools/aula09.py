from functools import reduce
from products import *


print(f"Total with sum: {sum([ p['price'] for p in products])}")

# Reduce


def func_reduce(accumulator, product):
    return product['price'] + accumulator


total = reduce(
    func_reduce,
    products,
    0
)
print(f"Total with reduce: {total}")
