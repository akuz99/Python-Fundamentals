numbers = input().split(", ")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])



for number in numbers.copy():
    if number == 0:
        numbers.remove(number)
        numbers.append(number)




print(numbers)












