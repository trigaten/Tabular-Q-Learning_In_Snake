import arcade
from AppKit import NSScreen #library that gets screen width and height
import numpy
import scipy.cluster.hierarchy as hcluster
print(NSScreen.mainScreen().frame())

SCREEN_WIDTH = NSScreen.mainScreen().frame().size.width
SCREEN_HEIGHT = NSScreen.mainScreen().frame().size.height
SCREEN_TITLE = "Snake"



def on_draw(delta_time):
    """
    Use this function to draw everything to the screen.
    """

    # Start the render. This must happen before any drawing
    # commands. We do NOT need a stop render command.
    arcade.start_render()
    
    arcade.draw_circle_outline(10, 10, 100, arcade.color.AIR_SUPERIORITY_BLUE)


def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK_LEATHER_JACKET)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1/1000)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()