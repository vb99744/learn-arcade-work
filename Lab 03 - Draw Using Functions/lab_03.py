import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def ocean_floor():
    """ Draw the sand and rocks """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 150,0, arcade.color.SAND)

    # furthest rocks
    arcade.draw_polygon_filled(((0, 150),
                                (0, 300),
                                (200, 280),
                                (230, 250),
                                (330, 320),
                                (370, 320),
                                (450, 270),
                                (600, 300),
                                (600, 150),
                                ),
                               (10, 210, 235))
    arcade.draw_polygon_filled(((0, 150),
                                (0, 400),
                                (100, 400),
                                (120, 300),
                                (160, 330),
                                (200, 300),
                                (220, 200),
                                (240, 150),
                                (350, 150),
                                (360, 170),
                                (430, 220),
                                (440, 280),
                                (450, 300),
                                (480, 300),
                                (500, 450),
                                (600, 470),
                                (600, 150),
                                ),
                               (0, 200, 225))

    # closest rocks
    arcade.draw_polygon_filled(((0, 150),
                                (0, 350),
                                (40, 350),
                                (60, 330),
                                (60, 300),
                                (50, 280),
                                (80, 270),
                                (90, 260),
                                (110, 230),
                                (100, 210),
                                (130, 180),
                                (140, 170),
                                (170, 150),
                                ),
                               (109, 105, 122))
    arcade.draw_polygon_filled(((600, 150),
                                (600, 380),
                                (570, 400),
                                (550, 370),
                                (560, 360),
                                (560, 300),
                                (540, 260),
                                (540, 220),
                                (520, 190),
                                (420, 160),
                                (400, 150),
                                ),
                               (109, 105, 122))

def fish(x,y):
    """ draw a group of three fish """
    arcade.draw_triangle_filled(x-13, y, x-20, y+10, x-20, y-10, arcade.color.YELLOW)
    arcade.draw_ellipse_filled(x, y, 30, 20, arcade.color.ORANGE)

    arcade.draw_triangle_filled(x-13, y+50, x-20, y+60, x-20, y+40, arcade.color.YELLOW)
    arcade.draw_ellipse_filled(x, y+50, 30, 20, arcade.color.ORANGE)

    arcade.draw_triangle_filled(x-63, y+25, x-70, y+35, x-70, y+15, arcade.color.YELLOW)
    arcade.draw_ellipse_filled(x-50, y+25, 30, 20, arcade.color.ORANGE)

def starfish(x,y):
    """ draw pink starfish """
    arcade.draw_circle_filled(x, y, 10, arcade.color.PINK)
    arcade.draw_triangle_filled(x, y+20, x-10, y+5, x+10, y+5, arcade.color.PINK)
    arcade.draw_triangle_filled(x+10, y+5, x+30, y, x+10, y-5, arcade.color.PINK)
    arcade.draw_triangle_filled(x, y-10, x+15, y-25, x+10, y-5, arcade.color.PINK)
    arcade.draw_triangle_filled(x, y-10, x-15, y-25, x-10, y-5, arcade.color.PINK)
    arcade.draw_triangle_filled(x-10, y+5, x-30, y, x-10, y-5, arcade.color.PINK)

def stingray(x,y):
    """ draw a stingray """
    arcade.draw_polygon_filled(((x+10, y+20),
                                (x-5, y+25),
                                (x-40, y+5),
                                (x-20, y-15),
                                (x-40, y-45),
                                (x-15, y-20),
                                (x+10, y-40),
                                (x+25, y),
                                (x+15, y+20),
                                ),
                               arcade.color.BLUE_GRAY)
    arcade.draw_ellipse_filled(x, y, 35, 50, arcade.color.BLUE_GRAY,45)

def shark(x,y):
    arcade.draw_ellipse_filled(x, y, 200, 50, arcade.color.ASH_GREY)
    arcade.draw_triangle_filled(x+20, y+50, x-30, y+20, x+30, y+20, arcade.color.ASH_GREY)
    arcade.draw_triangle_filled(x+80, y, x+150, y+30, x+150, y-30, arcade.color.ASH_GREY)

def main() :
    arcade.open_window(600, 600, "Ocean Life")
    arcade.set_background_color((28, 230, 254))
    arcade.start_render()

    ocean_floor()
    fish(500, 320)
    fish(220, 500)
    fish(100, 200)
    fish(350, 200)
    fish(160, 500)
    starfish(130, 50)
    starfish(570, 280)
    starfish(400, 100)
    starfish(50, 180)
    shark(420, 460)
    stingray(250, 300)
    stingray(400, 450)
    stingray(100, 380)
    stingray(550, 550)
    shark(250, 400)

    # finish
    arcade.finish_render()
    arcade.run()

# call the main function to get the program started
main()