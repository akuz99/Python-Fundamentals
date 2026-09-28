n = int(input())

numbers = [int(input()) for _ in range(n)]

filtered_numbers = []

command = input()

for n in numbers:
    if command == "even" and n % 2 == 0:
        filtered_numbers.append(n)
    elif command == "odd" and n % 2 != 0:
        filtered_numbers.append(n)
    elif command == "negative" and n < 0:
        filtered_numbers.append(n)
    elif command == "positive" and n >= 0:
        filtered_numbers.append(n)

print(filtered_numbers)
