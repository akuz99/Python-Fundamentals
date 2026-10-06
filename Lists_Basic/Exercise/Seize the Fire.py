cells = input().split("#")
amount_of_water = int(input())
total_effort = 0
cells_putted_out = []

high_range = range(81, 125 + 1)
medium_range = range(51, 80 + 1)
low_range = range(1, 50 + 1)


for cell in cells:
    type_of_fire, range_of_fire = cells.split(" = ")
    range_of_fire = int(range_of_fire)
    if amount_of_water >= range_of_fire:

        if type_of_fire == "High" and range_of_fire in high_range:
            total_effort += range_of_fire * 0.25
            amount_of_water -= range_of_fire
            cells_putted_out.append(range_of_fire)

        elif type_of_fire == "Medium" and range_of_fire in medium_range:
            total_effort += range_of_fire * 0.25
            amount_of_water -= range_of_fire
            cells_putted_out.append(range_of_fire)

        elif type_of_fire == "Low" and range_of_fire in low_range:
            total_effort += range_of_fire * 0.25
            amount_of_water -= range_of_fire
            cells_putted_out.append(range_of_fire)

print("Cells:")
for cell in cells_putted_out:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells_putted_out)}")






















