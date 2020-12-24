
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
board = []
player_pos = [x + g, (y - 1) // 2]  # 0-indexed
time = score = 0
breakFlag = False

for _ in range(x):
    board.append(['*'] * y)

for _ in range(g + 1):
    board.append([' '] * y)

board[player_pos[0]][player_pos[1]] = '@'

if x == 0:
    print('YOU WON!')
    breakFlag = True

# If only I could define these 3 lines as a function
for row in board:
    print(''.join(row))
print('-' * 72)

if breakFlag:
    print('YOUR SCORE: ' + str(score))
else:
    print('Choose your action!')

while True:
    if breakFlag:
        break

    command = input().lower()

    if command == 'exit':
        for row in board:
            print(''.join(row))
        print('-' * 72)
        print('YOUR SCORE: ' + str(score))
        break

    time += 1
    if command == 'fire':
        if board[player_pos[0] - 1][player_pos[1]] == ' ':
            board[player_pos[0] - 1][player_pos[1]] = '|'
            for row in board:
                print(''.join(row))
            print('-' * 72)
            next_row = player_pos[0] - 2
        else:
            next_row = player_pos[0] - 1

        while next_row >= 0 and board[next_row][player_pos[1]] == ' ':
            board[next_row][player_pos[1]] = '|'
            board[next_row + 1][player_pos[1]] = ' '
            for row in board:
                print(''.join(row))
            print('-' * 72)
            next_row -= 1

        if next_row >= 0:
            asteroid_count = 0
            for row in board:
                for col in row:
                    if col == '*':
                        asteroid_count += 1
                        if asteroid_count == 2:
                            break

            board[next_row][player_pos[1]] = ' '
            if board[next_row + 1][player_pos[1]] == '|':
                board[next_row + 1][player_pos[1]] = ' '
            score += 1

            if asteroid_count == 1:
                print('YOU WON!')
                for row in board:
                    print(''.join(row))
                print('-' * 72)
                print('YOUR SCORE: ' + str(score))
                break

        else:
            board[0][player_pos[1]] = ' '

    elif command == 'left':
        if player_pos[1] > 0:
            board[player_pos[0]][player_pos[1] - 1] = '@'
            board[player_pos[0]][player_pos[1]] = ' '
            player_pos[1] -= 1

    elif command == 'right':
        if player_pos[1] < y - 1:
            board[player_pos[0]][player_pos[1] + 1] = '@'
            board[player_pos[0]][player_pos[1]] = ' '
            player_pos[1] += 1

    if time % 5 == 0:
        if '*' in board[player_pos[0] - 1]:
            print('GAME OVER')
            for row in board:
                print(''.join(row))
            print('-' * 72)
            print('YOUR SCORE: ' + str(score))
            break
        else:
            for row_index in range(player_pos[0] - 1, 0, -1):
                board[row_index] = board[row_index - 1].copy()
            board[0] = [' '] * y

    for row in board:
        print(''.join(row))
    print('-' * 72)

    print('Choose your action!')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
