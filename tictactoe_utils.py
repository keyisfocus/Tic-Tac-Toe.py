def print_grid(matrix):
    print("---------")
    print(f"| {' '.join(matrix[0])} |")
    print(f"| {' '.join(matrix[1])} |")
    print(f"| {' '.join(matrix[2])} |")
    print("---------")


def analyze_state(matrix):
    flat_matrix = [n for row in matrix for n in row]
    x_count = flat_matrix.count('X')
    o_count = flat_matrix.count('O')
    if abs(x_count - o_count) > 1:
        return "Impossible"

    x_won = False
    o_won = False
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            if matrix[i][0] == 'X':
                x_won = True
            elif matrix[i][0] == 'O':
                o_won = True
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] == 'X':
                x_won = True
            elif matrix[0][i] == 'O':
                o_won = True
        if (matrix[0][0] == matrix[1][1] == matrix[2][2]
                or matrix[0][2] == matrix[1][1] == matrix[2][0]):
            if matrix[1][1] == 'X':
                x_won = True
            elif matrix[1][1] == 'O':
                o_won = True

    if x_won and o_won:
        return "Impossible"
    elif x_won:
        return "X wins"
    elif o_won:
        return "O wins"

    if '_' in flat_matrix:
        return "Game not finished"
    else:
        return "Draw"
