capacity = 255
number_of_lines = int(input())
water_tank = 0


for current_line in range(number_of_lines):
    liters_of_water = int(input())


    if water_tank + liters_of_water > capacity:
        print(f"Insufficient capacity!")
        continue

    water_tank += liters_of_water

print(water_tank)






