lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())


helmet_broken = lost_fights_count // 2
sword_broken = lost_fights_count // 3
shield_broken = lost_fights_count // 6
armor_broken = shield_broken // 2

expenses = helmet_price * helmet_broken +\
           sword_price * sword_broken +\
           shield_price * shield_broken +\
           armor_price * armor_broken


print(f"Gladiator expenses: {expenses:.2f} aureus")