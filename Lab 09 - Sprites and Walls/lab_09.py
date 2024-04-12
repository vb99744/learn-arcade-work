# I got all the images for the candy corn, crate, pumpkin, and player from google images.
# I got the sound from Free Sound

import random
import arcade
from pyglet.math import Vec2

# Constants
SPRITE_SCALING_BOX = 0.05
SPRITE_SCALING_PUMPKIN = 0.04
SPRITE_SCALING_PLAYER = 0.05
SPRITE_SCALING_CANDY_CORN = .03
CANDY_CORN_COUNT = 100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Walls"
PLAYER_MOVEMENT_SPEED = 5

# How many pixels to keep as a minimum margin between the character and the edge of the screen.
VIEWPORT_MARGIN = 220

# how fast the camera pans to the player.
CAMERA_SPEED = 0.5

class MyGame(arcade.Window):
    """ Main window of the game """
    def __init__(self, width, height, title):
        """ Initializer """
        # call the parent class initializer
        super().__init__(width, height, title, resizable=True)

        # sprites lists
        self.player_list = None
        self.wall_list = None
        self.candy_corn_list = None

        # set up the player
        self.player_sprite = None
        self.score = 0

        self.elapsed_ms = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # used in scrolling
        self.view_bottom = 0
        self.view_top = 0

        # track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Load the sound for collecting candy corn
        self.collect_sound = arcade.load_sound("489525__tiidwunduniik__candy-shake.m4a")

    def setup(self):
        """ set up the game and initialize the variables. """

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.candy_corn_list = arcade.SpriteList()

        # score
        self.score = 0

        # create the player
        self.player_sprite = arcade.Sprite("trick or treat.gif", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 388
        self.player_sprite.center_y = 263
        self.player_list.append(self.player_sprite)

        # create the wall
        # this is for the outer edge so the player does not go off-screen
        for x in range(13, 813, 25):
            wall = arcade.Sprite("pumpkin.jpg", SPRITE_SCALING_PUMPKIN)
            wall.center_x = x
            wall.center_y = 588
            self.wall_list.append(wall)

        for x in range(13, 813, 25):
            wall = arcade.Sprite("pumpkin.jpg", SPRITE_SCALING_PUMPKIN)
            wall.center_x = x
            wall.center_y = 13
            self.wall_list.append(wall)

        for y in range(13, 613, 25):
            wall = arcade.Sprite("pumpkin.jpg", SPRITE_SCALING_PUMPKIN)
            wall.center_x = 13
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(13, 613, 25):
            wall = arcade.Sprite("pumpkin.jpg", SPRITE_SCALING_PUMPKIN)
            wall.center_x = 788
            wall.center_y = y
            self.wall_list.append(wall)

         # the wall the player moves around from left to right
        coordinate_list_1 = [[38,88],
                            [63,88],
                            [63,113],
                            [38,113]]
        for coordinate in coordinate_list_1:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 38
        wall.center_y = 213
        self.wall_list.append(wall)

        coordinate_list_2 = [[38, 288],
                            [63, 288],
                            [63, 313],
                            [63, 263],
                            [88, 288]]
        for coordinate in coordinate_list_2:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(38, 117, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 388
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 38
        wall.center_y = 463
        self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 63
        wall.center_y = 438
        self.wall_list.append(wall)

        coordinate_list_3 = [[38, 538],
                             [63, 538],
                             [63, 513]]
        for coordinate in coordinate_list_3:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 88
        wall.center_y = 38
        self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 113
        wall.center_y = 63
        self.wall_list.append(wall)

        for x in range(63, 138, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 163
            self.wall_list.append(wall)

        for y in range(113, 188, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 113
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(113, 169, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 213
            self.wall_list.append(wall)

        coordinate_list_4 = [[138, 263],
                             [138, 288],
                             [163, 263],
                             [163, 288]]
        for coordinate in coordinate_list_4:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(113, 163, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 338
            self.wall_list.append(wall)

        for y in range(363, 413, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 163
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list_5 = [[113, 438],
                             [113, 463],
                             [113, 488],
                             [138, 438],
                             [138, 463],
                             [138, 488]]
        for coordinate in coordinate_list_5:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 113
        wall.center_y = 538
        self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 138
        wall.center_y = 563
        self.wall_list.append(wall)

        for y in range(38, 88, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 163
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(138, 188, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 163
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(163, 213, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 188
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list_6 = [[163, 463],
                             [188, 463],
                             [188, 438],
                             [188, 413]]
        for coordinate in coordinate_list_6:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 163
        wall.center_y = 513
        self.wall_list.append(wall)

        for y in range(538, 588, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 188
            wall.center_y = y
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 213
        wall.center_y = 88
        self.wall_list.append(wall)

        for y in range(238, 338, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 213
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list_7 = [[213, 363],
                             [238, 363],
                             [238,388],
                             [238,413],
                             [238,438],
                             [213,438]]
        for coordinate in coordinate_list_7:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(213, 363, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 488
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 338
        wall.center_y = 463
        self.wall_list.append(wall)

        for x in range(188, 313, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 538
            self.wall_list.append(wall)

        coordinate_list_8 = [[238, 38],
                             [263, 38],
                             [263, 63]]
        for coordinate in coordinate_list_8:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(238, 363, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 138
            self.wall_list.append(wall)

        for x in range(238, 288, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 188
            self.wall_list.append(wall)

        for y in range(38, 113, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 313
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(138, 213, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 313
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list_9 = [[288, 238],
                             [288, 263],
                             [313, 263],
                             [313, 288],
                             [288, 288],
                             [288, 313],
                             [263, 313],
                             [313, 313],
                             [338, 313],
                             [313, 338],
                             [313, 363],
                             [288, 363]]
        for coordinate in coordinate_list_9:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list_10 = [[288, 413],
                              [313, 413],
                              [313, 438]]
        for coordinate in coordinate_list_10:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 338
        wall.center_y = 563
        self.wall_list.append(wall)

        for x in range(363, 413, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 38
            self.wall_list.append(wall)

        for x in range(313, 413, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 88
            self.wall_list.append(wall)

        for y in range(88, 188, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 388
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(313, 388, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 188
            self.wall_list.append(wall)

        for y in range(238, 288, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 363
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(363, 463, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 363
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(363, 463, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 388
            self.wall_list.append(wall)

        for y in range(513, 588, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 388
            wall.center_y = y
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 413
        wall.center_y = 563
        self.wall_list.append(wall)

        for y in range(63, 113, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 438
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(88, 138, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 463
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(488, 563, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 38
            self.wall_list.append(wall)

        for y in range(38, 113, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 538
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(138, 188, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 438
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(438, 538, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 163
            self.wall_list.append(wall)

        for y in range(88, 188, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 513
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(188, 313, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 488
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list_11 = [[413, 213],
                              [413, 238],
                              [438, 238],
                              [438, 213]]
        for coordinate in coordinate_list_11:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list_12 = [[413, 288],
                              [388, 313],
                              [413, 313],
                              [438, 313],
                              [463, 313],
                              [413, 338]]
        for coordinate in coordinate_list_12:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list_13 = [[413, 438],
                              [413, 463],
                              [413, 488],
                              [438, 488],
                              [438, 463],
                              [438, 438]]
        for coordinate in coordinate_list_13:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for y in range(138, 188, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 563
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list_14 = [[688, 38],
                              [688, 63],
                              [688, 88],
                              [713, 88],
                              [713, 63],
                              [713, 38]]
        for coordinate in coordinate_list_14:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(588, 663, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 63
            self.wall_list.append(wall)

        for y in range(63, 138, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 588
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(63, 113, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 763
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(113, 238, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 613
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(663, 763, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 138
            self.wall_list.append(wall)

        for x in range(538, 713, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 213
            self.wall_list.append(wall)

        for y in range(138, 238, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 688
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(138, 213, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 738
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(213, 288, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 538
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(538, 613, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 263
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 588
        wall.center_y = 288
        self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 763
        wall.center_y = 188
        self.wall_list.append(wall)

        for x in range(538, 588, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 313
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 738
        wall.center_y = 238
        self.wall_list.append(wall)

        for y in range(263, 363, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 638
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(688, 763, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 263
            self.wall_list.append(wall)

        for x in range(713, 788, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 313
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 713
        wall.center_y = 338
        self.wall_list.append(wall)

        coordinate_list_15 = [[488, 363],
                              [513, 363],
                              [513, 388],
                              [513, 413],
                              [488, 413]]
        for coordinate in coordinate_list_15:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 488
        wall.center_y = 463
        self.wall_list.append(wall)

        for x in range(513, 588, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 488
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 563
        wall.center_y = 513
        self.wall_list.append(wall)

        for x in range(488, 538, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 513
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 463
        wall.center_y = 538
        self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 488
        wall.center_y = 563
        self.wall_list.append(wall)

        for y in range(363, 413, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 563
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(388, 463, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 613
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(538, 638, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 438
            self.wall_list.append(wall)

        for x in range(663, 713, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 363
            self.wall_list.append(wall)

        for y in range(363, 438, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = 738
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list_16 = [[663, 413],
                              [688, 413],
                              [688, 438],
                              [663, 438],
                              [663, 463],
                              [663, 488],
                              [613, 488],
                              [588, 488],
                              [588, 513]]
        for coordinate in coordinate_list_16:
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(563, 638, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 563
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 713
        wall.center_y = 488
        self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 738
        wall.center_y = 463
        self.wall_list.append(wall)

        wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
        wall.center_x = 763
        wall.center_y = 488
        self.wall_list.append(wall)

        for x in range(663, 788, 25):
            wall = arcade.Sprite("crate.jpg", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 538
            self.wall_list.append(wall)

        # Create the candy corn
        for i in range(CANDY_CORN_COUNT):
            candy_corn = arcade.Sprite("candy_corn.gif", SPRITE_SCALING_CANDY_CORN)

            candy_corn_placed_successfully = False

            while not candy_corn_placed_successfully:
                candy_corn.center_x = random.randrange(SCREEN_WIDTH)
                candy_corn.center_y = random.randrange(SCREEN_HEIGHT)

                wall_hit_list = arcade.check_for_collision_with_list(candy_corn, self.wall_list)

                candy_corn_hit_list = arcade.check_for_collision_with_list(candy_corn, self.candy_corn_list)

                if len(wall_hit_list) == 0 and len(candy_corn_hit_list) == 0:
                    candy_corn_placed_successfully = True

            self.candy_corn_list.append(candy_corn)

        # Create the physics engine.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # set background color
        arcade.set_background_color(arcade.color.PALATINATE_PURPLE)


    def on_draw(self):
        """ Render the screen. """

        # this command has to happen before we start drawing
        self.clear()

        # select the scrolled camera for our sprites.
        self.camera_sprites.use()

        # draw the sprites
        self.wall_list.draw()
        self.candy_corn_list.draw()
        self.player_list.draw()

        # select the (unscrolled) camera for our GUI
        self.camera_gui.use()
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.PALATINATE_BLUE)

        # add score count to the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 13, arcade.color.WHITE, 15)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False

    def on_update(self, delta_time):
        # calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        # call update on all sprites
        self.physics_engine.update()
        self.candy_corn_list.update()

        # generate a list of all sprites that collided with the player
        candy_corn_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.candy_corn_list)

        # loop through each colliding sprite, remove it, and add to the score
        for candy_corn in candy_corn_hit_list:
            candy_corn.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.collect_sound)

        # scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """ Scroll the window to the player """
        position = Vec2(self.player_sprite.center_x - self.width / 2, self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()