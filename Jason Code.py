import arcade

import settings

TITLE = 'Run For Your Life'
TILE_SCALING = 0.5
CHARACTER_SCALING = 1
SPRITE_NATIVE_SIZE = 1
ENEMY_SIZE = 2
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * CHARACTER_SCALING)
'Character Physics'
MOVEMENT_SPEED = 2.3
JUMP_SPEED = 9
GRAVITY = 0.3

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100


class Chapter2View(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.GINGER)
        # Sprite List
        self.player_list = None
        self.enemy_list = None
        self.wall_list = None
        self.finish_list = None
        # Player
        self.sprite1 = None
        self.physics_engine = None
        self.game_over = False
        # Enemy
        self.enemy = None
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        self.setup()

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.finish_list = arcade.SpriteList()
        # flag
        flag = arcade.Sprite(":resources:images/items/flagGreen2.png", 
                             CHARACTER_SCALING)
        flag.center_x = 5200
        flag.center_y = 130
        self.finish_list.append(flag)

        # PLayer
        self.sprite1 = arcade.Sprite("assets/girl.png", CHARACTER_SCALING)
        self.sprite1.center_x = 150
        self.sprite1.center_y = 100
        # Ground
        for x in range(0, 12500, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png",
                                 TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96],
                           [256, 96],
                           [768, 96]]
        coordinate_list_2 = [[3000, 96], [2000, 96], [1000, 96]]
        coordinate_list_3 = [[1500, 96], [3353, 96], [2412, 96]]
        coordinate_list_4 = [[1290, 96], [2500, 96], [3226, 96]]
        coordinate_list_5 = [[3597, 96], [4000, 96], [4302, 96]]
        coordinate_list_6 = [[4500, 96], [4729, 96], [4900, 96]]
        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
        for coordinates in coordinate_list_2:
            wall = arcade.Sprite(":resources:images/tiles/brickGrey.png",
                                 TILE_SCALING)
            wall.position = coordinates
            self.wall_list.append(wall)
        for coordinates in coordinate_list_3:
            wall = arcade.Sprite(":resources:images/tiles/brickGrey.png",
                                 TILE_SCALING)
            wall.position = coordinates
            self.wall_list.append(wall)
        for coordinates in coordinate_list_4:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 TILE_SCALING)
            wall.position = coordinates
            self.wall_list.append(wall)
        for coordinates in coordinate_list_5:
            wall = arcade.Sprite(":resources:images/tiles/brickGrey.png",
                                 TILE_SCALING)
            wall.position = coordinates
            self.wall_list.append(wall)
        for coordinates in coordinate_list_6:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 TILE_SCALING)
            wall.position = coordinates
            self.wall_list.append(wall)

        # Enemy
        enemy = arcade.Sprite(":resources:images/pinball/pool_cue_ball.png", 
                              ENEMY_SIZE)
        enemy.center_x = 34
        enemy.center_y = 120
        enemy.change_x = 2
        self.enemy_list.append(enemy)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.sprite1,
                                                             self.wall_list)

    def on_draw(self):
        arcade.start_render()  # keep as first line
        self.wall_list.draw()
        self.sprite1.draw()
        self.enemy_list.draw()
        self.finish_list.draw()
        # Draw everything below here.def update(self, delta_time):

    def update(self, delta_time):
        self.physics_engine.update()
        self.enemy_list.update()
        if self.sprite1.left < 0:
            self.sprite1.left = 0
        elif self.sprite1.right > settings.WIDTH + 1:
            self.sprite1.right > settings.WIDTH + 1

        changed = False
        # Player
        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.sprite1.left < left_boundary:
            self.view_left -= left_boundary - self.sprite1.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + settings.WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.sprite1.right > right_boundary:
            self.view_left += self.sprite1.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + settings.HEIGHT - TOP_VIEWPORT_MARGIN
        if self.sprite1.top > top_boundary:
            self.view_bottom += self.sprite1.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.sprite1.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.sprite1.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                settings.WIDTH + self.view_left,
                                self.view_bottom,
                                settings.HEIGHT + self.view_bottom)
        if len(arcade.check_for_collision_with_list(self.sprite1, 
                                                    self.finish_list)) > 0:
            self.director.next_view()
        if len(arcade.check_for_collision_with_list(self.sprite1, 
                                                    self.enemy_list)) > 0:
            self.game_over = True
    
        if self.game_over:
            self.setup()
            self.game_over = False

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.sprite1.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.sprite1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.sprite1.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.sprite1.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.sprite1.change_x = 0


if __name__ == "__main__":
    """This section of code will allow you to run your View
    independently from the main.py file and its Director.
    You can ignore this whole section. Keep it at the bottom
    of your code.
    It is advised you do not modify it unless you really know
    what you are doing.
    """
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter2View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
