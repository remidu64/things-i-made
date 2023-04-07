import decimal
import arcade
from math import *
from decimal import Decimal as Dec

decimal.getcontext().prec = 7

SPRITE_SCALING = 1
TILE_SCALING = 1.4
CAMERA_SCALE = 1.5

SCREEN_HEIGHT = 720
SCREEN_WIDTH = round(SCREEN_HEIGHT * (16 / 9))  # No need to specify screen width with this
SCREEN_TITLE = "Test collisions"
FPS = 60  # Why would you set it lower ?


def sign(x):  # A simple thing to find the sign of a number
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class Player(arcade.Sprite):
    """Player class"""

    def __init__(self, size, texture):
        super().__init__(texture, size)
        self.center_x = 0
        self.center_y = 0

        self.speed = 0
        self.change_x = 0
        self.change_y = 0


class Game(arcade.Window):
    """Main application class"""

    def __init__(self, width, height, title):
        """Initialize the game"""

        """Call the parent initializer function"""
        super().__init__(width, height, title, fullscreen=True, vsync=True, resizable=True, update_rate=1 / FPS)
        width = 1
        height = 1
        self.set_viewport(0, width, 0, height)

        """Scene object and scene info"""
        self.size_x = None
        self.size_y = None
        self.scene = None
        self.tilemap = None
        self.wall = None

        """GUI"""
        self.GUI = None

        "Main Camera"
        self.camera = None
        self.camera_position = None

        """Player"""
        self.player = None
        self.check = None

        """Key presses and mouse presses"""
        self.z = None
        self.s = None
        self.q = None
        self.d = None
        self.space = None
        self.shift = None

        """Pause flag"""
        self.pause = None

        """Physics"""
        self.physics = None

        """Things"""
        self.gravity = None
        self.fps = None
        self.count = None
        self.grounded = None
        self.step = None

    def setup(self):
        """Set up the game and initialize the variables"""

        """Camera"""
        self.camera = arcade.Camera(self.width, self.height)
        self.GUI = arcade.Camera(self.width, self.height)

        """Setup map"""

        map_path = "assets/collisions.tmj"

        layer_options = {"Walls": {"use_spatial_hash": True}}

        self.tilemap = arcade.load_tilemap(map_path, TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tilemap)

        self.size_x = self.tilemap.width * self.tilemap.tile_width * TILE_SCALING
        self.size_y = self.tilemap.height * self.tilemap.tile_height * TILE_SCALING

        # Setup Player
        self.player = Player(SPRITE_SCALING, "assets/player.png")
        self.player.center_x = 640
        self.player.center_y = 1000
        self.check = Player(SPRITE_SCALING, "assets/player.png")
        self.scene.add_sprite("Player", self.player)

        # Pause
        self.pause = False

        # things
        self.gravity = True
        self.wall = self.scene["Walls"]
        self.fps = 0
        self.count = 0
        self.grounded = False
        self.step = 0
        self.camera.scale = CAMERA_SCALE

    def drawd(self, text, x, y):  # a function to draw some text without having to specify some things
        arcade.draw_text(text, x, self.height - y, arcade.color.WHITE, 30)

    def on_draw(self):
        """Render the screen."""

        # This command has to happen before we start drawing
        self.clear()

        # Draw the scene
        self.camera.use()
        self.scene.draw()
        arcade.draw_line(self.player.center_x, self.player.center_y, self.player.center_x + self.player.change_x * 3,
                         self.player.center_y + self.player.change_y * 3, (255, 255, 255), 3)
        # Draw GUI things
        self.GUI.use()
        self.drawd(f"speed x: {Dec(self.player.change_x).quantize(Dec('1E-1'))}", 10, 30)
        self.drawd(f"speed y: {Dec(self.player.change_y).quantize(Dec('1E-1'))}", 10, 60)
        self.drawd(f"fps: {self.fps}", 10, 90)

    def on_key_press(self, key, modifiers):
        """Key presses"""

        if key == arcade.key.Z:
            self.z = True
        elif key == arcade.key.S:
            self.s = True
        elif key == arcade.key.D:
            self.d = True
        elif key == arcade.key.Q:
            self.q = True
        elif key == arcade.key.LSHIFT:
            self.shift = True

        # Pause the game
        elif key == arcade.key.SPACE:
            self.pause = not self.pause

        """key to quit the game"""
        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.Z:
            self.z = False
        elif key == arcade.key.S:
            self.s = False
        elif key == arcade.key.D:
            self.d = False
        elif key == arcade.key.Q:
            self.q = False
        elif key == arcade.key.LSHIFT:
            self.shift = False

    def center_camera(self, sprite):
        self.camera_position = sprite.center_x - (self.width / 2), sprite.center_y - (self.height / 2)
        self.camera.move_to(self.camera_position)

    def on_update(self, delta_time: float):
        """ Movement and game logic """

        # Manage user input
        if self.z:
            if self.shift:
                self.player.change_y += 5
            else:
                self.player.change_y += 0.6

        if self.q:
            if self.shift:
                self.player.change_x -= 5
            else:
                self.player.change_x -= 0.6

        if self.s:
            if self.shift:
                self.player.change_y -= 5
            else:
                self.player.change_y -= 0.6

        if self.d:
            if self.shift:
                self.player.change_x += 5
            else:
                self.player.change_x += 0.6

        # Calculate the speed and use it to calculate how many steps we should take to handle the physics
        self.player.speed = int(sqrt((self.player.change_x ** 2 + self.player.change_y ** 2)))
        self.step = int(self.player.speed / 20) + 1

        if not self.pause:  # SPAGHETTI CODE ALERT

            if abs(self.player.change_y) < 0.1:  # Bellow 0.1 speed you don't really notice the square moving
                self.player.change_y = 0

            if abs(self.player.change_x) < 0.1:
                self.player.change_x = 0

            for i in range(self.step):  # The physics is calculated in steps so that the player cannot go thru walls

                # Gravity
                if self.gravity and not self.grounded:
                    self.player.change_y -= 0.9 / self.step

                # check y collision

                self.player.center_y += self.player.change_y / self.step

                hit = arcade.check_for_collision_with_list(self.player,
                                                           self.wall)  # Did the player hit something whilst moving
                # on the Y axis ?

                if self.grounded:

                    if abs(self.player.change_y) > 1:  # If you're too fast you obviously leave the ground
                        self.grounded = False
                    self.check.center_x = self.player.center_x
                    self.check.center_y = self.player.center_y - 2  # Place an invisible sprite the size of the player
                    # 2 units bellow it.

                    if not arcade.check_for_collision_with_list(self.check,
                                                                self.wall):  # Check collision between the check and
                        # the ground
                        self.grounded = False

                if hit:

                    while arcade.check_for_collision_with_list(self.player,
                                                               self.wall):  # Move the player out of the obstacle
                        self.player.center_y -= sign(self.player.change_y)

                    if not self.grounded:

                        if abs(self.player.change_y) < 2 and (
                                sign(self.player.change_y) == -1 or sign(
                            self.player.change_y) == 0):  # If you're slow and you hit the ground, you'll stay on it
                            self.grounded = True
                            self.player.change_y = 0

                    self.player.change_y /= -1.2
                    self.player.change_x /= 1.15  # Apply some friction

                if self.grounded:
                    self.player.change_x /= 1.0175  # Slide on the ground

                # check x collision
                self.player.center_x += self.player.change_x / self.step
                hit = arcade.check_for_collision_with_list(self.player, self.wall)
                if hit:
                    while arcade.check_for_collision_with_list(self.player, self.wall):
                        self.player.center_x -= sign(self.player.change_x)

                    self.player.change_x /= -1.01

            if self.player.center_x > self.size_x:  # Loop around the terrain
                self.player.center_x = 0

            if self.player.center_x < 0:
                self.player.center_x = self.size_x

        # center camera on player
        self.center_camera(self.player)

        self.count += 1  # Calculate FPS based on delta time
        if self.count == FPS // 3:
            self.fps = int(1 / delta_time)
            self.count = 0


def main():
    """ Main function """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


main()
