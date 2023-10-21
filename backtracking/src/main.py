# Backtracking alghoritm

maze = [[".", ".", ".", "."],
        ["X", "x", "x", "."],
        [".", ".", ".", "."],
        ["x", "x", ".", "."]]

def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)
    return

def solve_maze(maze):
    if len(maze) < 1:
        return None
    if len(maze[0]) < 1:
        return None
    return solve_maze_helper(maze, [], 0, 0)

def solve_maze_helper(maze, sol, pos_row, pos_col):
    # get size of the maze
    num_row = len(maze)
    num_col = len(maze[0])

    # Base case
    #   - robot is already home
    if pos_row == num_row - 1 and pos_col == num_col - 1:
        return sol
    
    # - Robot is out of bounds   
    if pos_row >= num_row or pos_col >= num_col:
        return None

    # - Robor is on an obstacle
    if maze[pos_row][pos_col] == "x":
        return None

    # Recursive case
    # - Robot try going right
    sol.append("r")
    sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col + 1)
    if sol_going_right is not None:
        return sol_going_right
    
    # Going right doesn't work, Backtrack, try going down
    sol.pop()
    sol.append("d")
    sol_going_down = solve_maze_helper(maze, sol, pos_row + 1, pos_col)
    if sol_going_down is not None:
        return sol_going_down

    # No solution, impossible, Backtrack
    sol.pop()
    return None
"""

> solve_maze(maze)
> ['d','d','r','r','d','r']

"""

print_maze(maze)
print(" ")
print(solve_maze(maze))

