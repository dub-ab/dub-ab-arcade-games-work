"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example - Scoreboard")

# set the background color 
arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a circles outline centered at (140, 550) and (460, 550) 
# with a radius of 18 and a line width of 3.
arcade.draw_circle_outline(70, 550, 30, arcade.color.OLD_SILVER, 3)
arcade.draw_circle_outline(530, 550, 30, arcade.color.OLD_SILVER, 3)

arcade.draw_line(70, 576, 530, 576, arcade.color.OLD_SILVER, 3)
arcade.draw_line(70, 525, 530, 525, arcade.color.OLD_SILVER, 3)


# draw rectangle highlighting home and visistor
arcade.draw_circle_filled(70, 550, 29, arcade.color.BRICK_RED)
arcade.draw_xywh_rectangle_filled(70, 525, 230, 50, arcade.color.BRICK_RED)
arcade.draw_xywh_rectangle_filled(300, 525, 230, 50, arcade.color.OCEAN_BOAT_BLUE)

# Draw text starting at (10, 450) with a size of 20 points.
arcade.draw_text("Home", 130, 540, arcade.color.WHITE_SMOKE, 20)
arcade.draw_text("Visitor", 420, 540, arcade.color.WHITE_SMOKE, 20)

# Draw pitch
point_list = ((100, 200), (500, 200), (575, 50), (25, 50))
arcade.draw_polygon_filled(point_list, (45, 133, 15))
arcade.draw_rectangle_filled(300,47, 550, 5, arcade.color.MEDIUM_JUNGLE_GREEN)

# Draw pitch decoration 
# draw grass contrast
arcade.draw_polygon_filled(((300, 60), (300, 190), (270, 190), (255, 60)), (91, 164, 51))
arcade.draw_polygon_filled(((210, 60), (235, 190), (205, 190), (165, 60)), (91, 164, 51))
arcade.draw_polygon_filled(((125, 60), (175, 190), (145, 190), (85, 60)), (91, 164, 51))



# draw pitch stripes
arcade.draw_line(45, 60, 545, 60, arcade.color.WHITE_SMOKE, 2) # bottom sideline
arcade.draw_line(110, 190, 490, 190, arcade.color.WHITE_SMOKE, 2) # top sideline
arcade.draw_line(45, 60, 110, 190, arcade.color.WHITE_SMOKE, 2) # left end zone
arcade.draw_line(490, 190, 545, 60, arcade.color.WHITE_SMOKE, 2) # right end zone
arcade.draw_line(300, 60, 300, 190, arcade.color.WHITE_SMOKE, 2) # center line

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
