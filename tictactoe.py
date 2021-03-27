import tictactoe_utils
import re


def is_invalid(string_to_check):
    return re.match("^\\d\\s\\d$", string_to_check) is None


line = "_________"
matrix = [list(line[0:3]), list(line[3:6]), list(line[6:9])]

tictactoe_utils.print_grid(matrix)

x_move = True
while True:
    user_input = input("Enter the coordinates: ")
    if is_invalid(user_input):
        print("You should enter numbers!")
        continue
    coords = [int(n) for n in user_input.split() if 0 < int(n) < 4]

    if len(coords) != 2:
        print("Coordinates should be from 1 to 3!")
        continue

    if matrix[coords[0] - 1][coords[1] - 1] != '_':
        print("This cell is occupied! Choose another one!")
        continue

    matrix[coords[0] - 1][coords[1] - 1] = 'X' if x_move else 'O'
    x_move = not x_move
    tictactoe_utils.print_grid(matrix)

    state = tictactoe_utils.analyze_state(matrix)
    if state != "Game not finished":
        print(state)
        break
