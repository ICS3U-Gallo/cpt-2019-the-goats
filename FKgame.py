"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Battle Zudor"
MOVEMENT_SPEED = 3
enemy_hp_bar = 430
hp_bar = 0
box_width_left = 210
box_width_right = 430
box_hight_up = 250
box_hight_down = 50
hp_bar = 180
health = 50
enemy_health = 50
gravity_blue = 0
red_char = 1
Self_home_x = 300
Self_home_y = 300
MOVEMENT_SPEED_ENEMY_1 = 2
attack_pattern = 1
#Attack scenes
class GUI:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_lrtb_rectangle_outline(box_width_left, box_width_right, box_hight_up, box_hight_down, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_outline(210, 430, 290, 270, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(210, enemy_hp_bar, 290, 270, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_outline(30, 180, 170, 120, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_outline(30, 180, 210, 190, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(30, hp_bar, 210, 190, arcade.color.WHITE)
        arcade.text.draw_text('GREEN for HP, BLUE is Safe', 35, 120, arcade.color.WHITE, 40, 700)
        arcade.text.draw_text(f'HP Bar: {health}/50', 30, 220, arcade.color.WHITE, 15, 700)
        arcade.text.draw_text(f'Zodars HP Bar: {enemy_health}/50', 210, 300, arcade.color.WHITE, 15, 950)
    def on_key_press(self, key, modifiers):
        pass

    
    def update(rest):
        pass
    
    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > box_width_right - self.radius:
            self.position_x = box_width_right - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius
 
        if self.position_y > box_hight_up - self.radius:
            self.position_y = box_hight_up - self.radius
            enemy_health = enemy_health - 1
        
        if self.position_x < box_width_left + self.radius:
            self.position_x = box_width_left + self.radius
        if self.position_y < box_hight_down + self.radius:
            self.position_y = box_hight_down + self.radius

class Enemy1:
    def __init__(self, position_x_1, position_y_1, change_x_1, change_y_1, radius_1, color_1):

        # Take the parameters of the init function above, and create instance variables out of them.
        change_x_1 = MOVEMENT_SPEED_ENEMY_1
        change_y_1 = MOVEMENT_SPEED_ENEMY_1
        self.position_x_enemy = position_x_1
        self.position_y_enemy = position_y_1
        self.change_x_enemy = change_x_1
        self.change_y_enemy = change_y_1
        self.radius = radius_1
        self.color = color_1
        Enemy_list_1 = []
        

    
    def draw(self):
        arcade.draw_circle_filled(self.position_x_enemy, self.position_y_enemy, self.radius, self.color)

    def on_key_press(self, key, modifiers):
        pass

    
    def update(rest):
        pass
    
    def update(self):
        # Move the ball
        self.position_y_enemy += self.change_y_enemy
        self.position_x_enemy += self.change_x_enemy

        

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x_enemy < self.radius:
            self.position_x_enemy = self.radius

        if self.position_x_enemy > box_width_right - self.radius:
            self.position_x_enemy =  box_width_right - self.radius
            self.change_x_enemy = -MOVEMENT_SPEED_ENEMY_1


        if self.position_y_enemy < self.radius:
            self.position_y_enemy = self.radius
 
        if self.position_y_enemy > box_hight_up - self.radius:
            self.position_y_enemy =  box_hight_up - self.radius
            self.change_y_enemy = -MOVEMENT_SPEED_ENEMY_1
        
        if self.position_x_enemy < box_width_left + self.radius:
            self.position_x_enemy = box_width_left + self.radius
            self.change_x_enemy = MOVEMENT_SPEED_ENEMY_1
        if self.position_y_enemy < box_hight_down + self.radius:
            self.position_y_enemy = box_hight_down + self.radius
            self.change_y_enemy = MOVEMENT_SPEED_ENEMY_1


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

        # Create our ball
        if red_char == 1:
            self.ball = GUI(320, 150, 0, 0, 8, arcade.color.RED)
            
        else:
            self.ball = GUI(320, 150, 0, -10, 8, arcade.color.PURPLE_HEART)
        if attack_pattern == 1:
            self.enemy_ball_1 = Enemy1(320, 100, 0, 0, 8, arcade.color.WHITE)
            self.enemy_ball_2 = Enemy1(370, 150, 0, 0, 8, arcade.color.WHITE)   
            self.enemy_ball_3 = Enemy1(320, 200, 0, 0, 8, arcade.color.WHITE)
            self.enemy_ball_4 = Enemy1(270, 150, 0, 0, 8, arcade.color.WHITE)
            self.enemy_ball_5 = Enemy1(320, 230, 0, 0, 8, arcade.color.WHITE)
            self.enemy_ball_6 = Enemy1(410, 150, 0, 0, 8, arcade.color.WHITE)   
            self.enemy_ball_7 = Enemy1(320, 70, 0, 0, 8, arcade.color.WHITE)
            self.enemy_ball_8 = Enemy1(230, 150, 0, 0, 8, arcade.color.WHITE)
            

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        if attack_pattern == 1:
            self.enemy_ball_1.draw()
            self.enemy_ball_2.draw()
            self.enemy_ball_3.draw()
            self.enemy_ball_4.draw()
            self.enemy_ball_5.draw()
            self.enemy_ball_6.draw()
            self.enemy_ball_7.draw()
            self.enemy_ball_8.draw()
        else:
            pass

    def on_update(self, delta_time):
        self.ball.update()
        self.enemy_ball_1.update()
        self.enemy_ball_2.update()
        self.enemy_ball_3.update()
        self.enemy_ball_4.update()
        self.enemy_ball_5.update()
        self.enemy_ball_6.update()
        self.enemy_ball_7.update()
        self.enemy_ball_8.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            if red_char == 0:
                pass
            elif red_char != 0:
                self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            if red_char == 0:
                pass
            elif red_char != 0:
                self.ball.change_x = MOVEMENT_SPEED

        elif key == arcade.key.UP or key == arcade.key.W:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A or key == arcade.key.RIGHT or key == arcade.key.D:
            self.ball.change_x = 0
        
        elif key == arcade.key.UP or key == arcade.key.W or key == arcade.key.DOWN or key == arcade.key.S:
            if red_char == 0:
                self.ball.change_y = -10
            elif red_char != 0:
                self.ball.change_y = 0
            


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
