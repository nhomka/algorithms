from Maze import Maze

PART_OF_PATH = "O"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"

def search_from(maze, start_row, start_column):
    # try each of the four directions from this point until we find a way out or get stuck.

    #Base cases -
    # 1. We have run into an obstacle.
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # 2. We have foudn a square that has already been explored.
    if (maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END):
        return False
    # 3. We have found an outside edge with no obstacle (an exit)
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)
    # Otherwise, use lofical short circuiting to try each direction in turn (if needed).
    found = (search_from(maze, start_row + 1, start_column)
         or  search_from(maze, start_row - 1, start_column)
         or  search_from(maze, start_row, start_column - 1)
         or  search_from(maze, start_row, start_column + 1))

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found

my_maze = Maze("Recursion\maze2.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)