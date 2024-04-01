import random
import arcade

# constants
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_KEY = 0.05
KEY_COUNT = 10
SPRITE_SCALING_GHOST = 0.2
GHOST_COUNT = 15
MOVEMENT_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(arcade.Sprite):
    def update(self):
        # move player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # check for out-of-bounds
        if  self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH -1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Ghost(arcade.Sprite):
    # create bad sprite class
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # move the ghost
        self.center_y -= 1

        # reset ghost when it hits the bottom
        if self.top < 0:
            self.reset_pos()

class Key(arcade.Sprite):
    # create good sprite class
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        # move the keys
        self.center_x += self.change_x
        self.center_y += self.change_y

        # create the boundary so the key bounce back
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Lab")

        # load the sound for bad sprite collect
        self.ghost_collect_sound = arcade.load_sound("ghost_collect.wav")

        # load the sound for good sprite collect
        self.key_collect_sound = arcade.load_sound("key_collect.wav")

        # variables that will hold sprit lists.
        self.payler_list = None
        self.key_list = None
        self.ghost_list = None

        # Set up the player info
        self. player_sprite = None
        self.score = 0

        # set background
        arcade.set_background_color(arcade.color.PERIWINKLE)

    def setup(self):
        # sprite lists
        self.player_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = Player("trick or treat.gif", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        for i in range(GHOST_COUNT):
            ghost = Ghost("ghost.gif", SPRITE_SCALING_GHOST)

            # position the ghost
            ghost.center_x = random.randrange(SCREEN_WIDTH)
            ghost.center_y = random.randrange(SCREEN_HEIGHT)

            # add the ghost to the lists
            self.ghost_list.append(ghost)

        for i in range(KEY_COUNT):
            key = Key("key.gif", SPRITE_SCALING_KEY)

            # position the key
            key.center_x = random.randrange(SCREEN_WIDTH)
            key.center_y= random.randrange(SCREEN_HEIGHT)
            key.change_x = random.randrange(-3, 4)
            key.change_y = random.randrange(-3,4)

            # add key to the lists
            self.key_list.append(key)

    def on_draw(self):
        arcade.start_render()

        self.key_list.draw()
        self.ghost_list.draw()
        self.player_list.draw()

        # Place text for score and the game ends the final score
        if len(self.key_list) > 0:
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 15)
        else:
            output = "Game Over"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 50, SCREEN_HEIGHT / 2, arcade.color.RED, 40)
            output = f"Score: {self.score}"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 25, (SCREEN_HEIGHT / 2) - 50, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        self.player_list.update()

    def on_key_press(self, key: int, modifiers: int):
        # move the player with keyboard
        if len(self.key_list) > 0:
            if key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED
            elif key == arcade.key.UP:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0


    def update(self, delta_time):
        # keep updating until all good sprites are gone
        if len(self.key_list) > 0:
            self.key_list.update()
            self.ghost_list.update()

            # create the list for good sprites and add to the score
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.key_list)
            for key in hit_list:
                key.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.key_collect_sound)

            # create the list for bad sprites and subtract from the score
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.ghost_list)
            for ghost in hit_list:
                ghost.reset_pos()
                self.score -= 1
                arcade.play_sound(self.ghost_collect_sound)


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()