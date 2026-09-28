from math import floor

group_size = int(input())
days_of_the_adventure = int(input())
profit = 0
loss = 0


for days in range(1, days_of_the_adventure + 1):

    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5

    profit += 50
    loss += 2 * group_size


    if days % 3 == 0:
        loss += 3 * group_size
    if days % 5 == 0:
        profit += group_size * 20
    if days % 3 == 0 and days % 5 == 0:
        loss += 2 * group_size


total_profit = profit - loss
result = total_profit / group_size

print(f"{group_size} companions received {floor(result)} coins each.")
