products = [
    {"name": "Product 5", "price": 10.00},
    {"name": "Product 1", "price": 22.32},
    {"name": "Product 3", "price": 10.11},
    {"name": "Product 2", "price": 105.87},
    {"name": "Product 4", "price": 69.90},
    {"name": "Product 6", "price": 9.96},
]


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    