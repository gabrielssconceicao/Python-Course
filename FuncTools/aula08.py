from products import *

# Filter
# new_products = [
#     p for p in products
#     if p["price"] > 10
# ]
new_products = filter(
    lambda p: p["price"] > 20,
    products
)
print_iter(new_products)
