numbers = input().split()
text = list(input())
message = ""

for number in numbers:
    sum_of_digits = 0
    for i in range(len(number)):
        sum_of_digits += int(number[i])


    index = sum_of_digits % len(text)
    message += text.pop(index)


print(message)
