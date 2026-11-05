my_list = input().split()
left_time = 0
right_time = 0


middle = len(my_list) // 2

left_racer_sequence = my_list[:middle]
right_racer_sequence = my_list[:middle:-1]

for i in range(len(left_racer_sequence)):
    left_racer_sequence[i] = int(left_racer_sequence[i])
    left_time += left_racer_sequence[i]
    if left_racer_sequence[i] == 0:
        left_time *= 0.8

for i in range(len(right_racer_sequence)):
    right_racer_sequence[i] = int(right_racer_sequence[i])
    right_time += right_racer_sequence[i]
    if right_racer_sequence[i] == 0:
        right_time *= 0.8

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")

else:
    print(f"The winner is right with total time: {right_time:.1f}")

