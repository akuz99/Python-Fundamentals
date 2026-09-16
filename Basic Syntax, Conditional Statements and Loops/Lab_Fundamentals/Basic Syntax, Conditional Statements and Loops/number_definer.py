number = float(input())
solution = 0
detail = 0
new_solution = 0

if number == 0:
    solution = "zero"

elif number > 0:
    solution = "positive"

else:
    solution = "negative"

if number != 0:
    if abs(number) < 1:
        detail = "small"
    elif abs(number) > 1000000:
        detail = "large"
    else:
        detail = ""

    solution = f"{detail} {solution}".strip()


print(solution)

