import turtle

PART_OF_PATH = "O"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"

class Maze:

    def __init__(self, maze_filename):
        rows = 0
        cols = 0
        self.maze_list = []
        maze_file = open(maze_filename, "r")
        
        for line in maze_file:
            row_list = []
            col = 0
            for char in line[:-1]:
                row_list.append(char)
                if char == "S":
                    self.start_row = rows
                    self.start_col = col
                col += 1
            rows += 1
            self.maze_list.append(row_list)
            cols = len(row_list)
        
        self.rows = rows
        self.cols = cols
        self.x_translate = -cols / 2
        self.y_translate = rows / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(cols - 1) / 2 - .5,
                                    -(rows - 1) / 2 - .5,
                                    (cols - 1) / 2 + .5,
                                    (rows - 1) / 2 + .5,)

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows):
            for x in range(self.cols):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, -y + self.y_translate, "orange")
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)
    
    def is_exit(self, row, col):
        return ( row == 0
              or row == self.rows - 1
              or col == 0
              or col == self.cols - 1)
    
    def __getitem__(self, index):
        return self.maze_list[index]