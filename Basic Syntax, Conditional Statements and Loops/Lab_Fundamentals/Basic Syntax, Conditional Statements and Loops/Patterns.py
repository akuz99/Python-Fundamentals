number = int(input())

for i in range(1, number + 1):
    for j in range(0, i):
        print("*", end="")

    print()

for i in range(number - 1, 0, -1):
    for j in range(0, i):
        print("*", end="")

    print()

# # number = int(input())
#
# for increasing in range(1, number + 1):
#     print("*" * increasing)
# for decreasing in range(number - 1, 0, -1):
#     print("*" * decreasing)