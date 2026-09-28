number_of_lines = int(input())

closed = True
balanced = True

for _ in range(number_of_lines):
    char = input()

    if char == "(":
        if not closed:
            balanced = False
        closed = False

    elif char == ")":
        if closed:
            balanced = False
        closed = True

if not closed:
    balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
