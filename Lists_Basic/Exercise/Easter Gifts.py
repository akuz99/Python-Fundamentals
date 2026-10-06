gifts_planed = input().split()
command = input()



while command != "No Money":
    if command.startswith("OutOfStock"):
        _, gift = command.split()
        for i in range(len(gifts_planed)):
            if gifts_planed[i] == gift:
                gifts_planed[i] = "None"

    elif command.startswith("Required"):
        _, gift, index = command.split()
        index = int(index)
        if index in range(0, len(gifts_planed)):
            gifts_planed[index] = gift

    elif command.startswith("JustInCase"):
        _, gift = command.split()
        gifts_planed[-1] = gift

    command = input()

while "None" in gifts_planed:
    gifts_planed.remove("None")

print(" ".join(gifts_planed))







