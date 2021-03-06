# Tic-Tac-Toe https://hyperskill.org/projects/73

## Stage 1
Your first task in this project is to print the game grid in the console output. Use what you’ve learned about the `print()` function to print three lines, each containing three characters (X’s and O’s) to represent a game of tic-tac-toe where all fields of the grid have been filled in.

## Stage 2
In this stage, you will write a program that:

1. Reads a string of 9 symbols from the input and displays them to the user in a 3x3 grid. The grid can contain only `X`, `O` and `_` symbols.
2. Outputs a line of dashes `---------` above and below the grid, adds a pipe `|` symbol to the beginning and end of each line of the grid, and adds a space between all characters in the grid.

## Stage 3
In this stage, your program should:

1. Take a string entered by the user and print the game grid as in the previous stage.
2. Analyze the game state and print the result. Possible states:
* `Game not finished` when neither side has three in a row but the grid still has empty cells.
* `Draw` when no side has a three in a row and the grid has no empty cells.
* `X wins` when the grid has three X’s in a row.
* `O wins` when the grid has three O’s in a row.
* `Impossible` when the grid has three X’s in a row as well as three O’s in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).

In this stage, we will assume that either X or O can start the game.

You can choose whether to use a space or underscore _ to print empty cells.

# Stage 4
The program should work as follows:

1. Get the 3x3 grid from the input as in the previous stages.
2. Output this 3x3 grid as in the previous stages.
3. Prompt the user to make a move.
4. The user should input 2 numbers that represent the cell where they want to place their X. (the 9 symbols representing the field will be the first line of input, and the 2 coordinate numbers will be the second line of input)
5. Analyze user input and show messages in the following situations:  
`This cell is occupied!` Choose another one! if the cell is not empty.  
`You should enter numbers!` if the user enters non-numeric symbols in the coordinates input.  
`Coordinates should be from 1 to 3!` if the user enters coordinates outside the game grid.
6. Update the grid to include the user's move and print the updated grid to the console.

The program should also check the user’s input. If the input is unsuitable, the program should tell the user why their input was wrong, and prompt them to enter coordinates again.

To summarize, you need to output the game grid based on the first line of input, and then ask the user to enter a move. Keep asking until the user enters coordinates that represent an empty cell on the grid, update the grid to include that move, and then output it to the console. You should output the field only 2 times: once before the user’s move, and once after the user has entered a legal move.

*Do not delete the code* you already wrote that analyzes the game state; you will need it in the final step of this project.

## Stage 5

In this stage, you should write a program that:

1. Prints an empty grid at the beginning of the game.
2. Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
3. Ends the game when someone wins or there is a draw.

You need to output the final result at the end of the game.

Good luck!