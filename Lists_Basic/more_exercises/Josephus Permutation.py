number_of_people = input().split()
step = int(input())
new_list = []
result = []

for i in range(len(number_of_people)):
    number_of_people[i] = int(number_of_people[i])
    new_list.append(number_of_people[i])

index = 0
while len(new_list) > 0:
    index = (index + step - 1) % len(new_list)
    result.append(new_list.pop(index))
print(str(result).replace(" ", ""))




