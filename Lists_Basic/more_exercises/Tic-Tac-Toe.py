field_1 = input().split()
field_2 = input().split()
field_3 = input().split()



board = [field_1,
         field_2,
         field_3]
winner = "0"

for i in range(3):

    if board[i][0] == board[i][1] == board[i][2] != "0":
        winner = board[i][0]
        break

    elif board[0][i] == board[1][i] == board[2][i] != "0":
        winner = board[0][i]
        break
if winner == "0":
    if board[0][0] == board[1][1] == board[2][2] != "0":
        winner = board[0][0]

    elif board[0][2] == board[1][1] == board[2][0] != "0":
        winner = board[0][2]


if winner == "1":
    print("First player won")
elif winner == "2":
    print("Second player won")
elif winner == "0":
    print("Draw!")






