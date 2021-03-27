import tictactoe_utils

line = input("Enter cells: ")
matrix = [list(line[0:3]), list(line[3:6]), list(line[6:9])]

print("---------")
print(f"| {' '.join(line[0:3])} |")
print(f"| {' '.join(line[3:6])} |")
print(f"| {' '.join(line[6:9])} |")
print("---------")

print(tictactoe_utils.analyze_state(matrix))
