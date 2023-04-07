import arcade
import math

SPRITE_SCALING = 0.3
TILE_SCALING = 1

SCREEN_HEIGHT = 720
SCREEN_WIDTH = round(16/9 * SCREEN_HEIGHT)
SCREEN_TITLE = "drift"
CAMERA_SPEED = 0.15
FPS = 60

class Game(arcade.Window):
    """Main application class"""

    def __init__(self, width, height, title):
        """Initializer"""

        #call the parent class initializer
        super().__init__(width, height, title, fullscreen = True, vsync = True, resizable = True, update_rate = 1/FPS)

        #get window size
        width, height = self.get_size()

        #set viewport
        self.set_viewport(0, width, 0, height)