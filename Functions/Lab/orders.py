def order_price(product, quantity):
    prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }
    return prices[product] * quantity

product_ = input()
quantity_ = int(input())
result = order_price(product_, quantity_)
print(f"{result:.2f}")