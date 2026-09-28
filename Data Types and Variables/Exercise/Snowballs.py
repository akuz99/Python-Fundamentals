number_of_snowballs = int(input())
value = 0
max_weight = 0
max_time_needed = 0
max_quality = 0

for current_ball in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    current_value = (weight // time_needed) ** quality

    if current_value > value:
        value = current_value
        max_weight = weight
        max_time_needed = time_needed
        max_quality = quality

print(f"{max_weight} : {max_time_needed} = {value} ({max_quality})")