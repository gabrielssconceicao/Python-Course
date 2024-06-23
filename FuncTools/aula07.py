from functools import partial
from products import *

# Map


def raise_percent(value, percent):
    return round(value * percent,2)


raise_ten_percent = partial(
    raise_percent,
    percent=1.1
)


# new_products = [
#     {
#         **p,
#         "price": raise_ten_percent(p['price'])
#     }
#     for p in products
# ]

def change_product_price(product):
    return {
        **product,
        "price": raise_ten_percent(product['price'])
    }


new_products = map(
    change_product_price,
    products
)

print_iter(products)
print_iter(new_products)