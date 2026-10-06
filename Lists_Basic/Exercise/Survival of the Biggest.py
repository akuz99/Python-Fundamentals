numbers = input().split()
numbers = [int(x) for x in numbers]
numbers_to_remove = int(input())


for number in range(numbers_to_remove):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")

