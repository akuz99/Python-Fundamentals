number = int(input())
case = True

for i in range(2, number - 1):
    if number % i == 0:
        case = False
        break

print(case)