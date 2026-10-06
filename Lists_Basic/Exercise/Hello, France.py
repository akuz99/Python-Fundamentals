collection_of_items = input().split("|")
budget = int(input())
bought_items = []


TRAIN_TICKET= 150

for item_info in collection_of_items:
    item, price = item_info.split("->")
    price = float(price)

    if item == "Clothes" and price <= 50.00 and budget >= price:
        budget -= price
        bought_items.append(price)

    elif item == "Shoes" and price <= 35.00 and budget >= price:
        budget -= price
        bought_items.append(price)

    elif item == "Accessories" and price <= 20.50 and budget >= price:
        budget -= price
        bought_items.append(price)

total_bought_price = 0


for price in bought_items:
    print(f"{price * 1.40:.2f}", end= " ")
    total_bought_price += price
print()

print(f"Profit: {(total_bought_price * 1.40) - total_bought_price:.2f}")

if budget + total_bought_price * 1.40 >= TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
