import arcade

#setting the dimensions (600, 600)
#setting the widow title to "Icecream Cones"
arcade.open_window(600, 600, "Icecream Cones")

# set background color
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

# start drawing
arcade.start_render()

# large cone
arcade.draw_triangle_filled(300, 50, 200, 320, 400, 320, arcade.csscolor.SANDY_BROWN)

# chocolate icecream
arcade.draw_arc_filled(300,320, 200, 200, arcade.csscolor.CHOCOLATE, 0, 180)
arcade.draw_circle_filled(300, 320, 45, arcade.csscolor.CHOCOLATE)
arcade.draw_circle_filled(220, 320, 45, arcade.csscolor.CHOCOLATE)
arcade.draw_circle_filled(380, 320, 45, arcade.csscolor.CHOCOLATE)

# strawberry icecream
arcade.draw_arc_filled(300, 400, 200, 200, arcade.csscolor.LIGHT_PINK, 0, 180)
arcade.draw_circle_filled(300, 380, 45, arcade.csscolor.LIGHT_PINK)
arcade.draw_circle_filled(220, 380, 45, arcade.csscolor.LIGHT_PINK)
arcade.draw_circle_filled(380, 380, 45, arcade.csscolor.LIGHT_PINK)

# cherry and stem
arcade.draw_circle_filled(340, 490, 25, arcade.csscolor.RED)
arcade.draw_line(345,510, 360, 530, arcade.csscolor.GREEN, 5)

# sprinkles
arcade.draw_rectangle_filled(300, 400, 12, 4, arcade.csscolor.CYAN, 4)
arcade.draw_rectangle_filled(320, 360, 12, 4, arcade.csscolor.YELLOW, 12)
arcade.draw_rectangle_filled(360, 350, 12, 4, arcade.csscolor.DEEP_PINK, 45)
arcade.draw_rectangle_filled(250, 420, 12, 4, arcade.csscolor.YELLOW, 60)
arcade.draw_rectangle_filled(240, 450, 12, 4, arcade.csscolor.DEEP_PINK, 58)
arcade.draw_rectangle_filled(380, 400, 12, 4, arcade.csscolor.YELLOW, 23)
arcade.draw_rectangle_filled(345, 450, 12, 4, arcade.csscolor.DEEP_PINK, 30)
arcade.draw_rectangle_filled(225, 379,12, 4, arcade.csscolor.CYAN, 13)
arcade.draw_rectangle_filled(210, 350, 12, 4, arcade.csscolor.DEEP_PINK, 77)
arcade.draw_rectangle_filled(265, 378, 12, 4, arcade.csscolor.DEEP_PINK, 40)
arcade.draw_rectangle_filled(200, 400, 12, 4, arcade.csscolor.YELLOW, -25)
arcade.draw_rectangle_filled(350, 385, 12, 4, arcade.csscolor.CYAN, 35)
arcade.draw_rectangle_filled(400, 365, 12, 4, arcade.csscolor.LIGHT_GREEN, 10)
arcade.draw_rectangle_filled(330, 420, 12, 4, arcade.csscolor.LIGHT_GREEN, 28)
arcade.draw_rectangle_filled(280, 480, 12, 4, arcade.csscolor.LIGHT_GREEN, -45)
arcade.draw_rectangle_filled(305, 460, 12, 4, arcade.csscolor.CYAN, 72)
arcade.draw_rectangle_filled(285, 435, 12, 4, arcade.csscolor.LIGHT_GREEN, 32)
arcade.draw_rectangle_filled(375, 430, 12, 4, arcade.csscolor.CYAN, 50)

# small icecream cone
arcade.draw_polygon_filled(((100, 50),
                            (50, 150),
                            (30, 170),
                            (30, 180),
                            (170, 180),
                            (170, 170),
                            (150, 150),
                            ),
                           arcade.csscolor.SANDY_BROWN)

# vanilla icecream for small cone
arcade.draw_ellipse_filled(100, 180, 160, 50, arcade.csscolor.WHITE)
arcade.draw_arc_filled(100, 180, 130, 130, arcade.csscolor.WHITE, 0, 180)

#finish drawing
arcade.finish_render()

arcade.run()