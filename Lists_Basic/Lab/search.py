n = int(input())
word = input()

strings = [input() for _ in range(n)]

filtered_strings = []

for index in strings:
    if word in index:
        filtered_strings.append(index)

print(strings)
print(filtered_strings)




