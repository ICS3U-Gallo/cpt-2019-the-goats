import arcade

import settings

TITLE = '2D Temple Run'
TILE_SCALING = 0.5
'Character Physics'
MOVEMENT_SPEED = 5
JUMP_SPEED = 10
GRAVITY = 0.3
Sprite_scaling = 0.5


class Chapter2View(arcade.View):
    def __init__(self):     
        super().__init__()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        # Player
        self.sprite1 = arcade.Sprite(center_x=100, center_y=100)
        self.sprite1.change_x = 1
        self.sprite1.texture = arcade.make_soft_square_texture(50,
                                                               arcade.color.
                                                               BLACK,
                                                               outer_alpha=255)
        
        self.wall_list = None
        self.physics_engine = None
        self.wall_list = None
        
        # If you have sprite lists, you should create them here,
        # and set them to Noneound1

        self.setup()
    
    def setup(self):
        self.sprite1.center_x = 64
        self.sprite1.center_y = 128
        self.wall_list = arcade.SpriteList()
        for x in range(0, 1250, 64):
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
        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 
                                 TILE_SCALING) 
            wall.position = coordinate
            self.wall_list.append(wall)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.sprite1, 
                                                             self.wall_list)

    def on_draw(self):
        arcade.start_render()  # keep as first line
        self.wall_list.draw()
        self.sprite1.draw()
        # Draw everything below here.def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
    
    def update(self, deltatime):
        self.physics_engine.update()

        if self.sprite1.left < 0:
            self.sprite1.left = 0
        elif self.sprite1.right > settings.WIDTH - 1:
            self.sprite1.right = settings.WIDTH - 1

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
    my_view.director = FakeDirector(close_on_next_view=False)
    window.show_view(my_view)
    arcade.run()
