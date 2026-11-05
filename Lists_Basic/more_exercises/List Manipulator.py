numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
command = ""

while True:
    command = input().split()

    if command[0] == "end":
        break

    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers):
            numbers = numbers[index + 1:] + numbers[:index + 1]

        else:
            print("Invalid index")

    elif command[0] == "max":
        if command[1] == "even":
            even_numbers = []
            for number in numbers:
                if number % 2 == 0:
                    even_numbers.append(number)
            if len(even_numbers) > 0:
                biggest = max(even_numbers)
                print(len(numbers) - 1 - numbers[::-1].index(biggest))
            else:
                print("No matches")
        if command[1] == "odd":
            odd_numbers = []
            for number in numbers:
                if number % 2 != 0:
                    odd_numbers.append(number)
            if len(odd_numbers) > 0:
                biggest = max(odd_numbers)
                print(len(numbers) - 1 - numbers[::-1].index(biggest))
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            even_numbers = []
            for number in numbers:
                if number % 2 == 0:
                    even_numbers.append(number)
            if len(even_numbers) > 0:
                smallest = min(even_numbers)
                print(len(numbers) - 1 - numbers[::-1].index(smallest))
            else:
                print("No matches")
        elif command[1] == "odd":
            odd_numbers = []
            for number in numbers:
                if number % 2 != 0:
                    odd_numbers.append(number)
            if len(odd_numbers) > 0:
                smallest = min(odd_numbers)
                print(len(numbers) - 1 - numbers[::-1].index(smallest))
            else:
                print("No matches")

    elif command[0] == "first":
        count = 0
        count = int(command[1])

        if count > len(numbers):
            print("Invalid count")

        else:

            if command[2] == "even":
                first_evens = []
                for number in numbers:
                    if number % 2 == 0:
                        first_evens.append(number)
                        count -= 1

                        if count == 0:
                            break
                print(first_evens)
            elif command[2] == "odd":
                first_odds = []
                for number in numbers:
                    if number % 2 != 0:
                        first_odds.append(number)
                        count -= 1

                        if count == 0:
                            break
                print(first_odds)

    elif command[0] == "last":
        count = int(command[1])

        if count > len(numbers):
            print("Invalid count")

        else:

            if command[2] == "even":
                last_evens = []
                for number in numbers[::-1]:
                    if number % 2 == 0:
                        last_evens.append(number)
                        count -= 1

                        if count == 0:
                            break
                print(last_evens[::-1])
            elif command[2] == "odd":
                last_odds = []
                for number in numbers[::-1]:
                    if number % 2 != 0:
                        last_odds.append(number)
                        count -= 1

                        if count == 0:
                            break

                print(last_odds[::-1])


print(numbers)








