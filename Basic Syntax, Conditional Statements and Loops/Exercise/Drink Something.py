age = int(input())
answer = ""

if age <= 14:
    answer = "drink toddy"
elif age <= 18:
    answer = "drink coke"
elif age <= 21:
    answer = "drink beer"
elif age > 21:
    answer = "drink whisky"

print(answer)


