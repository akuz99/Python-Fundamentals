key = int(input())
number_of_lines = int(input())
word = ""
new_word = ""

for _ in range(number_of_lines):
    letter = input()

    word += letter

for char in word:
    char = ord(char) + key
    new_word += chr(char)

print(new_word)


