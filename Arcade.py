import arcade
import time

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

# Set the background color to white.
# For a list of named colors see:
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
arcade.set_background_color(arcade.color.WHITE)

radiusLeft = 36
diminui = True
while True:

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()

    # Draw the face
    x = 300
    y = 300
    radius = 200
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

    # Draw the right eye
    x = 370
    y = 350
    radius = 36
    arcade.draw_ellipse_filled(x, y, radius, 36, arcade.color.BLACK)

    # Draw the left eye
    x = 230
    y = 350
    #radius = 36
    arcade.draw_ellipse_filled(x, y, 36, radiusLeft, arcade.color.BLACK)
    if diminui:
        radiusLeft -= 1
    else:
        radiusLeft += 1   
    if radiusLeft == 0:
        diminui = False 
    elif radiusLeft == 36:
        diminui = True       

    # Draw the smile
    x = 300
    y = 280
    width = 120
    height = 100
    start_angle = 190
    end_angle = 350
    arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

    # Finish drawing and display the result
    #arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()

