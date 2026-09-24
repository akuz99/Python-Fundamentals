budget = float(input())
price_kg_flour = float(input())
eggs = 0
loaf_counter = 0
lost_eggs = 0
price_pack_eggs = 0.75 * price_kg_flour
price_l_milk = 1.25 * price_kg_flour

one_loaf_price = price_pack_eggs + price_kg_flour + price_l_milk / 4

while budget > one_loaf_price:
    budget -= one_loaf_price
    loaf_counter += 1
    eggs += 3
    if loaf_counter % 3 == 0:
        lost_eggs += loaf_counter - 2

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {eggs - lost_eggs} eggs and {budget:.2f}BGN left.")
