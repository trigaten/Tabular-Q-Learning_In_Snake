import arcade
import Agent
# from AppKit import NSScreen #library that gets screen width and height
# print(NSScreen.mainScreen().frame())

# general set up
SCREEN_WIDTH = 1440#NSScreen.mainScreen().frame().size.width
SCREEN_HEIGHT = 900#NSScreen.mainScreen().frame().size.height
SCREEN_TITLE = "Bouncing Rectangle Example"
# agent set up
boardSize = 2
agent = Agent.Agent(2, "V-Iteration", 0.9)
change = 1000
# performing value iteration
while change > 0.001:
    change = agent.valueIteration()
    print("change " + str(change))

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
    # Draw an rectangle outline
    arcade.draw_text("draw_rect", 243, 3, arcade.color.BLACK, 10)
    arcade.draw_rectangle_outline(295, 100, 45, 65,
                                arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_rectangle_outline(295, 160, 20, 45,
                                arcade.color.BRITISH_RACING_GREEN, 3, 45)

    # Draw a filled in rectangle
    arcade.draw_text("draw_filled_rect", 363, 3, arcade.color.BLACK, 10)
    arcade.draw_rectangle_filled(420, 100, 45, 65, arcade.color.BLUSH)
    arcade.draw_rectangle_filled(420, 160, 20, 40, arcade.color.BLUSH, 45)

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