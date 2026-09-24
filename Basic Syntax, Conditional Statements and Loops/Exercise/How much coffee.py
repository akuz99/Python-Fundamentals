command = input()
number_of_coffees = 0
while command != "END":

    if command.lower() not in ["coding", "dog", "cat", "movie"]:
        command = input()
        continue

    if command.islower():
        number_of_coffees += 1
    elif command.isupper():
        number_of_coffees += 2

    command = input()


if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)




