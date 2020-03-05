import arcade
import Combinatorics
# from AppKit import NSScreen #library that gets screen width and height
# print(NSScreen.mainScreen().frame())

SCREEN_WIDTH = 1440#NSScreen.mainScreen().frame().size.width
SCREEN_HEIGHT = 900#NSScreen.mainScreen().frame().size.height
SCREEN_TITLE = "Bouncing Rectangle Example"
p = 0

# def drawMap(map, squareSize):
#     for x in range(len(map)):
#         for y in range(len(map[0])):
#             print("hi")
#             arcade.draw_circle_outline(x*squareSize, y*squareSize, squareSize, arcade.color.AIR_SUPERIORITY_BLUE)
#             arcade.draw_circle_outline(100, 100, 100, arcade.color.AIR_SUPERIORITY_BLUE)

def on_draw(delta_time):
    """
    Use this function to draw everything to the screen.
    """
    global p
    # drawMap(map, 50)
    # Start the render. This must happen before any drawing
    # commands. We do NOT need a stop render command.
    arcade.start_render()
    map = Combinatorics.makeBoard(4)
    for x in range(len(map)):
        for y in range(len(map[0])):
            print("hi")
            arcade.draw_circle_outline(p+x*100, y*100, 100, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_circle_outline(100, 100, 100, arcade.color.AIR_SUPERIORITY_BLUE)
    p+=10
    # arcade.draw_circle_outline(100, 100, 100, arcade.color.AIR_SUPERIORITY_BLUE)

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