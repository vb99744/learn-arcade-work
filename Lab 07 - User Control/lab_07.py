""" Lab 7 - User Control"""

import arcade

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def cloud(x,y):
    # Draw a cloud
    arcade.draw_circle_filled(x, y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 35, y - 20, 45, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 35, y - 20, 45, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y - 30, 45, arcade.color.WHITE)

def background():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 100, 0, arcade.color.DIRT)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 150, 100, arcade.color.DARK_MOSS_GREEN)
    cloud(200, 480)
    cloud(500, 500)
    cloud(120, 240)
    cloud(400, 280)
    cloud(700, 400)

class Bird:
    def __init__(self, position_x, position_y, size, color):
        self.position_x = position_x
        self.position_y = position_y
        self.size = size
        self.color = color

    def draw(self):
        # draw a bird
        arcade.draw_arc_outline(self.position_x, self.position_y, self.size, self.size, self.color, 0, 180, 5)
        arcade.draw_arc_outline(self.position_x-20, self.position_y, self.size, self.size, self.color, 0, 180, 5)

class Kite:
    def __init__(self, position_x, position_y, change_x, change_y, size, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size
        self.color = color

        # add explosion sound
        self.explosion_sound = arcade.load_sound("explosion.wav")


    def draw(self):
        # draw the kite
        arcade.draw_polygon_filled(((self.position_x, self.position_y),
                                    (self.position_x-15, self.position_y-25),
                                    (self.position_x-40, self.position_y-40),
                                    (self.position_x-25, self.position_y-15),
                                    ),
                                   self.color)
        arcade.draw_line(self.position_x-40, self.position_y-40, self.position_x-55, self.position_y-55, self.color)

    def update(self):
        # move the kite
        self.position_x += self.change_x
        self.position_y += self.change_y

        # keep the kite on the screen and add sound for when it hits the edge of screen
        if self.position_x < self.size:
            self.position_x = self.size
            arcade.play_sound(self.explosion_sound)

        if self.position_x > SCREEN_WIDTH - self.size:
            self.position_x = SCREEN_WIDTH - self.size
            arcade.play_sound(self.explosion_sound)

        if self.position_y < self.size:
            self.position_y = self.size
            arcade.play_sound(self.explosion_sound)

        if self.position_y > SCREEN_HEIGHT - self.size:
            self.position_y = SCREEN_HEIGHT - self.size
            arcade.play_sound(self.explosion_sound)

class MyGame(arcade.Window):
    """ Our Custom Window Class """

    def __init__(self):
        """ Initializer"""
        # call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # add bird sound
        self.bird_soound = arcade.load_sound("bird.wav")

        self.set_mouse_visible(False)

        # set background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # create the bird
        self.bird = Bird(400, 300, 20, arcade.color.BLACK)
        self.target_x = 0
        self.target_y = 0

        self.kite = Kite(50, 50, 0, 0, 50, arcade.color.AFRICAN_VIOLET)

    def on_draw(self):
        arcade.start_render()
        background()

        # draw the bird
        self.bird.draw()

        # update x coord
        if self.bird.position_x < self.target_x:
            self.bird.position_x += 1
        elif self.bird.position_x > self.target_x:
            self.bird.position_x -= 1

        #update y coord
        if self.bird.position_y < self.target_y:
            self.bird.position_y += 1
        elif self.bird.position_y > self.target_y:
            self.bird.position_y -= 1

        self.kite.draw()

    def update(self, delta_time: float):
        self.kite.update()


    def on_key_press(self, key: int, modifiers: int):
        # movement for the kite
        if key == arcade.key.LEFT:
            self.kite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            sarcade.

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # movement for the bird
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.target_x = x
            self.target_y = y

            # add sound when clicking the mouse
            arcade.play_sound(self.bird_soound)



def main():
    window = MyGame()
    arcade.run()

main()