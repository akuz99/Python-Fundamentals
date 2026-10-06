events = input().split("|")
current_energy= 100
current_coins = 100
day_completed = True


for event in events:
    command, number = event.split("-")
    number = int(number)

    if command == "rest":

        if current_energy + number > 100:
            gained_energy = 100 - current_energy
            current_energy = 100
        else:
            gained_energy = number
            current_energy += number

        print(f"You gained {gained_energy} energy.\nCurrent energy: {current_energy}.")

    elif command == "order":
        if current_energy >= 30:
            current_energy -= 30
            current_coins += number
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print("You had to rest!")

    else:
        if current_coins >= number:
            current_coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            day_completed = False
            break


if day_completed:
    print(f"Day completed!\nCoins: {current_coins}\nEnergy: {current_energy}")
