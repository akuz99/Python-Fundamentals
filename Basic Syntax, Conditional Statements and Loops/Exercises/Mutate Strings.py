# first_string = input()
# second_string = input()
#
#
# for char in range(len(first_string)):
#     if first_string[char] != second_string[char]:
#         first_string = first_string[:char] + second_string[char] + first_string[char + 1:]
#         print(first_string)

first_string = input()
second_string = input()

for index in range(len(first_string)):
    left_part = second_string[:index + 1]
    right_part = first_string[index + 1:]
    final_string = left_part + right_part

    if first_string[index] != second_string[index]:
        print(final_string)
