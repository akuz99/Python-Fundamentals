factor = int(input())
count = int(input())
my_list = []
number = 1

while len(my_list) < count:
    if number % factor == 0:
        my_list.append(number)

    number += 1

print(my_list)






