import arcade
import math
import random

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Rooms Example"

MOVEMENT_SPEED = 5


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        super().__init__(filename, sprite_scaling)
        self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.008
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y
        self.circle_angle += self.circle_speed


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        self.wall_list = None
        self.coin_list = None
        self.background = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()
    """ Set up the game and initialize the variables. """
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)
    for i in range(50):
        coin = Coin(":resources:images/animated_characters/zombie/zombie_walk1.png", SPRITE_SCALING)
        coin.circle_center_x = random.randrange(50, SCREEN_WIDTH-50)
        coin.circle_center_y = random.randrange(50, SCREEN_HEIGHT-50)
        coin.circle_radius = random.randrange(10, 50)
        coin.circle_angle = random.random() * 2 * math.pi
        room.coin_list.append(coin)
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()
    """ Set up the game and initialize the variables. """
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")
    for i in range(50):
        coin = Coin(":resources:images/animated_characters/zombie/zombie_walk1.png", SPRITE_SCALING)
        coin.circle_center_x = random.randrange(SCREEN_WIDTH-100)
        coin.circle_center_y = random.randrange(SCREEN_HEIGHT-100)
        coin.circle_radius = random.randrange(10, 50)
        coin.circle_angle = random.random() * 2 * math.pi
        room.coin_list.append(coin)
    return room


class MyGame(arcade.Window):
    """ Main application class. """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_room = 0
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player_sprite = arcade.Sprite("assets/girl.png", 0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.rooms = []
        room = setup_room_1()
        self.rooms.append(room)
        room = setup_room_2()
        self.rooms.append(room)
        self.current_room = 0
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)
        self.rooms[self.current_room].wall_list.draw()
        self.rooms[self.current_room].coin_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()
        self.rooms[self.current_room].coin_list.update()
        if self.game_over:
            self.setup()
            self.game_over = False
        if len(arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].coin_list)) > 0:
            self.game_over = True

        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
