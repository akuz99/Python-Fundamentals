numbers = input().split()

opposite_numbers = []

for current_number in numbers:
    number = int(current_number)
    opposite_numbers.append(-number)

print(opposite_numbers)