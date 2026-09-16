quantity_deco = int(input())
days_left = int(input())
day = 0
points = 0
total_cost = 0


ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_deco += 2
    if day % 2 == 0:
        total_cost += ornament_set * quantity_deco
        points += 5
    if day % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * quantity_deco
        points += 13
    if day % 5 == 0:
        total_cost += tree_lights * quantity_deco
        points += 17

    if day % 3 == 0 and day % 5 == 0:
        points += 30

    if day % 10 == 0:
        points -= 20
        total_cost += tree_skirt + tree_garland + tree_lights

    if day == days_left and day % 10 == 0:
        points -= 30

print(f"Total cost: {total_cost}")

print(f"Total spirit: {points}")




