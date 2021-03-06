"""
Sprite Follow player 2

This calculates a 'vector' towards the player and randomly updates it based
on the player's location. This is a bit more complex, but more interesting
way of following the player.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_follow_simple_2
"""

import random
import arcade
import math
import os

# first round of enemies
SPRITE_SCALING_COIN = 1
COIN_COUNT = 30
COIN_SPEED = 2

# second round of enemies
BULLET_SPEED = 20
BULLET_SCALLING = 0.5

# player
MOVEMENT_SPEED = 5
SPRITE_SCALING_player = 1

# player laser/bullet
SPRITE_SCALING_LASER = 0.3
LASER_SPEED = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Follow player Simple Example 2"

#setup of first round enemies
class Coin(arcade.Sprite):


    #first round of enemies following player
    def follow_sprite(self, player_sprite):

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * COIN_SPEED
            self.change_y = math.sin(angle) * COIN_SPEED


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # background
        arcade.set_background_color(arcade.color.BLACK_LEATHER_JACKET)

        # second round of enemies when they shoot
        self.frame_count = 0

        # count of enemies in the first round
        self.count = 0

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.coin1_list = None
        self.laser_list = None
        self.bullet_list = None
        self.plants_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # aim
        self.aim_x = 500
        self.aim_y = 500

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.coin1_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.plants_list = arcade.SpriteList()

        # number of enemies
        self.count = 0

        # Score
        self.score = 0


        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("girl.png", SPRITE_SCALING_player)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range (5):

            # set up the plants
            self.plants = arcade.Sprite(":resources:images/tiles/bush.png", 0.5)
            self.plants.center_x = random.randrange(0, SCREEN_WIDTH)
            self.plants.center_y = random.randrange(0, SCREEN_HEIGHT//2)
            self.plants_list.append(self.plants)


        # first round of enemies
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(":resources:images/animated_characters/zombie/zombie_idle.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(0, SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

            self.count = self.count + 1

        #second round of enemies
        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk6.png", 0.5)
        self.coin1.center_x = 120
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 120
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 400
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 600
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 300
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk6.png", 0.5)
        self.coin1.center_x = 120
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height - 50
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 120
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height - 50
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 400
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height - 50
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 600
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height - 50
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)

        self.coin1 = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk4.png", 0.5)
        self.coin1.center_x = SCREEN_WIDTH - 300
        self.coin1.center_y = SCREEN_HEIGHT - self.coin1.height - 50
        self.coin1.angle = 180
        self.coin1_list.append(self.coin1)


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        # water
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 1000, 200, arcade.color.BLUE, 0)

        #other objects sprites
        self.coin_list.draw()
        self.player_list.draw()
        self.laser_list.draw()
        self.bullet_list.draw()
        self.plants_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # aim
        arcade.draw_circle_outline(self.aim_x, self.aim_y, 25, arcade.color.YELLOW, 2, 20)

        #second round of enemies spawn when first round of enemy count = 0
        if self.count == 0:
            self.coin1_list.draw()

    def on_key_press(self, key, modifiers):

        #player movement
        if key == arcade.key.W or key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        #player movement
        if key == arcade.key.W or key == arcade.key.S or key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D or key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        #updates of objects
        self.player_sprite.update()
        self.laser_list.update()
        self.plants_list.update()

        #prevents lagging, applies with the code under,
        #so basically every 60 frame, the second round of enemies will shoot
        self.frame_count += 1

        #spawns second round of enemies when first round is all killed
        if self.count == 0:

            # the setup of the second round of enemies
            for coin1 in self.coin1_list:

                # First, calculate the angle to the player. We could do this
                # only when the bullet fires, but in this case we will rotate
                # the enemy to face the player each frame, so we'll do this
                # each frame.

                # Position the start at the enemy's current location
                start_x = coin1.center_x
                start_y = coin1.center_y

                # Get the destination location for the bullet
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Do math to calculate how to get the bullet to the destination.
                # Calculation the angle in radians between the start points
                # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Set the enemy to face the player.
                coin1.angle = math.degrees(angle) - 90

                # Shoot every 60 frames change of shooting each frame
                if self.frame_count % 60 == 0:
                    bullet = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_fall.png", BULLET_SCALLING)
                    bullet.center_x = start_x
                    bullet.center_y = start_y

                    # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                    # and change_y. Velocity is how fast the bullet travels.
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    self.bullet_list.append(bullet)

        # prevent lagging
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()

        # first round of enemies getting killed or enemies killing player
        for coin in self.coin_list:
            coin.follow_sprite(self.player_sprite)
        for coin in self.coin_list:
            laser_in_contact = coin.collides_with_list(self.laser_list)
            player_in_contact = coin.collides_with_list(self.player_list)
            if laser_in_contact:
                coin.kill()
                self.count = self.count - 1
                self.score += 1
                for laser in laser_in_contact:
                    laser.kill()
            elif player_in_contact:
                self.player_sprite.center_x = 50
                self.player_sprite.center_y = 50

        # when first round enemies all die, second round enemies spawn
        if self.count == 0:
            self.coin1_list.update()

        #second round of enemies getting killed or enemies killing player
        for coin1 in self.coin1_list:
            laser_in_contact = coin1.collides_with_list(self.laser_list)
            if laser_in_contact:
                coin1.kill()
                self.score += 1
        for bullet in self.bullet_list:
            player_in_contact = bullet.collides_with_list(self.player_list)
            if player_in_contact:
                self.player_sprite.center_x = 50
                self.player_sprite.center_y = 50

        # bushes can block all bullets and lasers
        for laser in self.laser_list:
            plants_in_contact = laser.collides_with_list(self.plants_list)
            if plants_in_contact:
                laser.kill()

        for bullet in self.bullet_list:
            plants_in_contact = bullet.collides_with_list(self.plants_list)
            if plants_in_contact:
                bullet.kill()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse moves.
        """
        # Create player bullet called laser
        laser_sprite = arcade.Sprite(":resources:images/tiles/rock.png", SPRITE_SCALING_LASER)

        # Position the bullet at the player's current location
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        laser_sprite.center_x = start_x
        laser_sprite.center_y = start_y

        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need
        # to add in self.view_bottom and self.view_left.
        dest_x = x
        dest_y = y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        laser_sprite.angle = math.degrees(angle)
        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        laser_sprite.change_x = math.cos(angle) * LASER_SPEED
        laser_sprite.change_y = math.sin(angle) * LASER_SPEED

        # Add the bullet to the appropriate lists
        self.laser_list.append(laser_sprite)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.aim_x = x
        self.aim_y = y


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
