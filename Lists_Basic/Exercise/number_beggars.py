money_string = input().split(", ")
count_of_beggars = int(input())
money_int = []

for money in money_string:
    money_int.append(int(money))

beggars_sum = []
start_index = 0
for current_beggar in range(count_of_beggars):
    current_beggars_money = 0
    for index in range(start_index, len(money_int), count_of_beggars):
        current_beggars_money += money_int[index]

    beggars_sum.append(current_beggars_money)
    start_index += 1


print(beggars_sum)


