def calculate(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        if b > 0:
            return a / b

operator_ = input()
first_num = int(input())
second_num = int(input())
result = calculate(first_num, second_num, operator_)
print(int(result))
