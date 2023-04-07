import arcade
import math

FPS = 60

SPRITE_SCALING = 0.3
TILE_SCALING = 1

SCREEN_HEIGHT = 720
SCREEN_WIDTH = int(720 * 16/9)
TITLE = "car v2"

class game(arcade.Window):
    """class de l'appli"""

    def __init__(self, height = SCREEN_HEIGHT, width = SCREEN_WIDTH, title = TITLE):
        """Initializer le jeu"""

        #appel du __init__ de la classe parent
        super().__init__(width, height, title, fullscreen=True, vsync=True, resizable=True, update_rate=1 / FPS)


def main():
    """Fonction Principale"""
    window = game()
    window.setup()
    arcade.run()


main()
