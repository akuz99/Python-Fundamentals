word = input()

word = word.lower()

counter = 0
words = ["sand", "water", "fish", "sun"]

for item in words:
    counter += word.count(item)

print(counter)


#counter = sum(word.count(item) for item in words)
