word = input()
capitals = []

for index, item in enumerate(word):
    if item.isupper():
        capitals.append(index)

print(capitals)

# word = input()
# capitals = []
#
# index = 0
#
# for item in word:
#     if item.isupper():
#         capitals.append(index)
#
#     index += 1
#
#
# print(capitals)

