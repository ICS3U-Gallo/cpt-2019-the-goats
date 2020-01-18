import arcade
import math
import random

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 100
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Rooms Example"
MOVEMENT_SPEED = 5


class Zombie(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.02
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y
        self.circle_angle += self.circle_speed


class Room:
    def __init__(self):
        self.wall_list = None
        self.zombie_list = None
        self.finish_list = None
        self.background = None


def setup_room_1():
    room = Room()
    room.wall_list = arcade.SpriteList()
    room.zombie_list = arcade.SpriteList()
    room.finish_list = arcade.SpriteList()
    finish = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING/10)
    finish.center_x = 0
    finish.center_y = 0
    room.finish_list.append(finish)
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5 and y != SPRITE_SIZE * 6) or x == 0:
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)
    for i in range(50):
        zombie = Zombie(":resources:images/animated_characters/zombie/zombie_walk1.png", SPRITE_SCALING)
        zombie.circle_center_x = random.randrange(100, SCREEN_WIDTH-50)
        zombie.circle_center_y = random.randrange(110, SCREEN_HEIGHT-50)
        zombie.circle_radius = random.randrange(10, 50)
        zombie.circle_angle = random.random() * 2 * math.pi
        room.zombie_list.append(zombie)
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
    return room


def setup_room_2():
    room = Room()
    room.wall_list = arcade.SpriteList()
    room.zombie_list = arcade.SpriteList()
    room.finish_list = arcade.SpriteList()
    finish = arcade.Sprite(":resources:images/tiles/doorClosed_top.png", SPRITE_SCALING)
    finish.center_x = 700
    finish.center_y = 300
    room.finish_list.append(finish)
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5 and y != SPRITE_SIZE * 6) or x != 0:
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")
    for i in range(60):
        zombie = Zombie(":resources:images/animated_characters/zombie/zombie_walk1.png", SPRITE_SCALING)
        zombie.circle_center_x = random.randrange(SCREEN_WIDTH-100)
        zombie.circle_center_y = random.randrange(SCREEN_HEIGHT-100)
        zombie.circle_radius = random.randrange(10, 50)
        zombie.circle_angle = random.random() * 2 * math.pi
        room.zombie_list.append(zombie)
    return room


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_room = 0
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.game_over = False
        self.score = 0

    def setup(self):
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
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)
        self.rooms[self.current_room].wall_list.draw()
        self.rooms[self.current_room].zombie_list.draw()
        self.rooms[self.current_room].finish_list.draw()
        self.player_list.draw()
        output = "Fails: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.rooms[self.current_room].zombie_list.update()
        if self.game_over:
            self.setup()
            self.score += 1
            self.game_over = False
        finish_list = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].finish_list)
        if len(finish_list) > 0:
            self.director.next_view()
        death_list = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].zombie_list)
        if len(death_list) > 0:
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
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
