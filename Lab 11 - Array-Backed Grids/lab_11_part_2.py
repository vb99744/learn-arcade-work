import arcade

# set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# set the width and height of each grid location
WIDTH = 20
HEIGHT = 20

# this sets the margin between each cell
# and on the edges of the screen
MARGIN = 5

# do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

class MyGame(arcade.Window):
    """ Main application class """

    def __init__(self, width, height):
        """ set up the application """
        super().__init__(width, height)
        # create a 2 dimensional array
        self.grid = []
        for row in range(ROW_COUNT):
            # add an empty array that will hold each cell in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0) # append a cell

        arcade.set_background_color(arcade.color.NAVY_BLUE)

    def on_draw(self):
        """ render the screen """

        arcade.start_render()

        # draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.PINK
                else:
                    color = arcade.color.LIME_GREEN

                # do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ called when the user presses a mouse button """

        # cange the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        # make sure we are on-grid. it is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:
            # flip the location between 1 and 0
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

            # call to color cells touching the cell we clicked
            self.test_n_set(row, column)

            # count selected cells in the grid
            total_selected_cells = 0
            for row in self.grid:
                for cell in row:
                    if cell == 1:
                        total_selected_cells += 1
            print(f"Total of {total_selected_cells} cells are selected.")

            # count selected cells in each row
            row_count = 0
            for row in self.grid:
                row_selected_cells = 0
                for cell in row:
                    if cell == 1:
                        row_selected_cells += 1
                print(f"Row {row_count} has {row_selected_cells} cells selected.")

                # print continuous cells selected in each row
                continuous_count = 0
                for cell in row:
                    if cell == 1:
                        continuous_count += 1
                    else:
                        if continuous_count > 2:
                            print(f"There are {continuous_count} continuous cells selected on row {row_count}.")
                        continuous_count = 0

                if continuous_count > 2:
                    print(f"There are {continuous_count} continuous cells selected on row {row_count}.")

                row_count += 1

            # print selected cells in each column
            for column_count in range(COLUMN_COUNT):
                column_selected_cells = 0
                for row in self.grid:
                    if row[column_count] == 1:
                        column_selected_cells += 1
                print(f"Column {column_count} has {column_selected_cells} cells selected.")

    def test_n_set(self, x, y):
        # change the color of the cell user clicked
        self.grid[x][y] = 1 - self.grid[x][y]

        # define the coordinates for the shape
        plus_sign_coordinates = [(x,y),
                                 (x-1, y),
                                 (x+1, y),
                                 (x, y-1),
                                 (x, y+1)]

        # change colors after a cell is clicked on
        for x_coordinate, y_coordinate in plus_sign_coordinates:
            if 0 <= x_coordinate < ROW_COUNT and 0 <= y_coordinate < COLUMN_COUNT:
                self.grid[x_coordinate][y_coordinate] = 1 - self.grid[x_coordinate][y_coordinate]

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()