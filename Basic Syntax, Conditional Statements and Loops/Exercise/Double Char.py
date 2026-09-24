command = input()
new_word = ""

while command != "End":

    if command == "SoftUni":
        command = input()
        continue

    for char in range(len(command)):
        new_word += command[char] * 2

    print(new_word)
    new_word = ""
    command = input()




