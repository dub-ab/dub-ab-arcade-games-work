"""
As Seen At: Teaching Python 3.6 with Games
http://arcade-book.readthedocs.io/en/latest/

This is a sample program to show how to draw using the Python programming
language and the Arcade library.



Copyright/Attribution Notice: 
Credit "Kenney.nl" or "www.kenney.nl"
"""

# Import the "arcade" library
import arcade


SPOT_SIZE = 3.5
SHADOW_DEPTH = 5
# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example - Scoreboard")

# set the background color 
arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)

# Get ready to draw
arcade.start_render()

# draw home and visitor highlight color
arcade.draw_xywh_rectangle_filled(70, 500, 230, 50, arcade.color.BRICK_RED)
arcade.draw_xywh_rectangle_filled(300, 500, 230, 50, arcade.color.OCEAN_BOAT_BLUE)

arcade.draw_polygon_filled(((200, 550), (400, 550), (350, 500), (250, 500)), arcade.color.OLD_SILVER)
arcade.draw_line(70, 498, 250, 498, arcade.color.PRUNE, SHADOW_DEPTH)
arcade.draw_line(250, 498, 349, 498, arcade.color.ONYX, SHADOW_DEPTH) 
arcade.draw_line(349, 498, 530, 498, arcade.color.PRUSSIAN_BLUE, SHADOW_DEPTH) 

# Draw text 48, 2000, '', ('Calibri', 'Arial'),  True)
arcade.draw_text("Home", 130, 515, arcade.color.WHITE_SMOKE, 20, 2, '', ('Calibri', 'Arial'), True)
arcade.draw_text("Visitor", 410, 515, arcade.color.WHITE_SMOKE, 20, 2000, '', ('Calibri', 'Arial'), True)
arcade.draw_text("vs", 276, 515, arcade.color.WHITE_SMOKE, 36, 2000, '', ('Calibri', 'Arial'), True)
#arcade.draw_line(300, 550, 300, 500, (255,255,255), 1) # reference line

# Draw team logo
red_logo = arcade.load_texture("c:\\VSCode\\dub-ab-arcade-games-work\\Lab 02 - Draw a Picture\\images\\red-parrot.png")
blue_logo = arcade.load_texture("c:\\VSCode\\dub-ab-arcade-games-work\\Lab 02 - Draw a Picture\\images\\blue-hippo.png")
scale = .25
arcade.draw_texture_rectangle(70, 525, scale * red_logo.width, scale * red_logo.height, red_logo, 45)
arcade.draw_texture_rectangle(530, 525, scale * blue_logo.width, scale * blue_logo.height, blue_logo, 315)

# Draw pitch
point_list = ((90, 200), (510, 200), (580, 50), (15, 50))
arcade.draw_polygon_filled(point_list, (45, 133, 15))
arcade.draw_line(15,47, 580, 47, arcade.color.MEDIUM_JUNGLE_GREEN, SHADOW_DEPTH) # pitch shadow

# Draw pitch decoration 
# Draw grass contrast
arcade.draw_polygon_filled(((300, 60), (300, 190), (270, 190), (255, 60)), (91, 164, 51))
arcade.draw_polygon_filled(((210, 60), (235, 190), (205, 190), (165, 60)), (91, 164, 51))
arcade.draw_polygon_filled(((125, 60), (175, 190), (145, 190), (85, 60)), (91, 164, 51))
arcade.draw_polygon_filled(((345, 60), (330, 190), (360, 190), (390, 60)), (91, 164, 51))
arcade.draw_polygon_filled(((430, 60), (390, 190), (420, 190), (470, 60)), (91, 164, 51))
arcade.draw_polygon_filled(((515, 60), (460, 190), (490, 190), (545, 60)), (91, 164, 51))

# Draw pitch lines
arcade.draw_point(300, 125, arcade.color.WHITE_SMOKE, SPOT_SIZE) # center spot
arcade.draw_ellipse_outline(300, 125, 24, 18, arcade.color.WHITE_SMOKE, 2) # center circle

arcade.draw_line(45, 60, 545, 60, arcade.color.WHITE_SMOKE, 2) # bottom sideline
arcade.draw_line(110, 190, 490, 190, arcade.color.WHITE_SMOKE, 2) # top sideline
arcade.draw_line(45, 60, 110, 190, arcade.color.WHITE_SMOKE, 2) # left end zone
arcade.draw_line(490, 190, 545, 60, arcade.color.WHITE_SMOKE, 2) # right end zone
arcade.draw_line(300, 60, 300, 190, arcade.color.WHITE_SMOKE, 2) # center line

arcade.draw_polygon_outline(((59, 85), (100, 170), (165, 170), (130, 85)), arcade.color.WHITE_SMOKE, 2) # Home penalty box
# Home goal box
arcade.draw_point(130, 125, arcade.color.WHITE_SMOKE, SPOT_SIZE) # Home Penalty spot
arcade.draw_arc_outline(145, 125, 20, 13, arcade.color.WHITE_SMOKE, 0, 70, 2) # Home Penalty arch (upper portion)
arcade.draw_arc_outline(145, 125, 20, 13, arcade.color.WHITE_SMOKE, 260, 360, 2) # Home Penalty arc (lower portion)
arcade.draw_arc_outline(145, 125, 20, 13, arcade.color.WHITE_SMOKE, 0, 70, 2)
arcade.draw_polygon_outline(((460, 85), (430, 170), (499, 170), (534, 85)), arcade.color.WHITE_SMOKE, 2) # Visitor penalty box
# Visitor Goal Box
arcade.draw_point(465, 125, arcade.color.WHITE_SMOKE, SPOT_SIZE) # Visitor Penalty spot
#arcade.draw_arc_outline(150, 81, 15, 36, arcade.color.BRIGHT_MAROON, 90, 360)# Visitor Penalty arc

# Draw corner arcs
arcade.draw_arc_outline(45, 60, 20, 10, arcade.color.WHITE_SMOKE, 0, 75, 2) # lower left corner 
arcade.draw_arc_outline(110, 190, 10, 10, arcade.color.WHITE_SMOKE, 245, 360, 2) # upper left corner 
arcade.draw_arc_outline(490, 190, 10, 10, arcade.color.WHITE_SMOKE, 180, 300, 2) # upper right corner 
arcade.draw_arc_outline(545, 60, 20, 10, arcade.color.WHITE_SMOKE, 100, 180, 2) # lower right corner 

def draw_xyhw_rectangle_rounded_corners(left, top, width, height, radius, color, border):
    """
    Draw a rectangle with rounded corners by specifying left, \
    and top edge locations, width, height and radius.
    
    Where:
        :``left``: is the left_side (float), 
        :``top``: is the top_side: (float), 
        :``width``: is the width: (float), 
        :``height``: is the height: (float), 
        :``radius``: is the radius: (float), 
        :``color``: is the color: typing.Union[typing.Tuple[int, int, int], \
        typing.List[int], typing.Tuple[int, int, int, int]], 
        :``border``: is the border_width: (float = 1)
    Returns:
        None
    Raises:
        None
    """
    arcade.draw_line( (left + radius),            top, ((left + width) - radius),                       top, color, border)  # top 
    arcade.draw_line( (left + radius), (top - height), ((left + width) - radius),            (top - height), color, border)  # bottom   
    arcade.draw_line(            left, (top - radius),                      left, ((top - height) + radius), color, border)  # left side    
    arcade.draw_line(  (left + width), (top - radius),            (left + width), ((top - height) + radius), color, border)  # right side 

    arcade.draw_arc_outline( ((left + width) - radius),            (top - radius),  radius,  radius, color,   0,  90, border)  # upper right corner
    arcade.draw_arc_outline(           (left + radius),            (top - radius),  radius,  radius, color,  90, 180, border)  # upper left corner
    arcade.draw_arc_outline(           (left + radius), ((top - height) + radius),  radius,  radius, color, 180, 270, border)  # lower left corner
    arcade.draw_arc_outline( ((left + width) - radius), ((top - height) + radius),  radius,  radius, color, 270, 360, border)  # lower right corner

# Draw Scoreboard
# arcade.draw_line(       100, 325, 500, 325, arcade.color.ARYLIDE_YELLOW, 5)            # bottom
# arcade.draw_arc_outline(500, 325,  50,  50, arcade.color.ARYLIDE_YELLOW, 270, 360, 5)  # lower right corner
# arcade.draw_line(       550, 320, 550, 355, arcade.color.ARYLIDE_YELLOW, 5)            # visitor side
# arcade.draw_arc_outline(500, 375,  50,  50, arcade.color.ARYLIDE_YELLOW, 0, 90, 5)     # upper right corner
# arcade.draw_line(       500, 425, 100, 425, arcade.color.ARYLIDE_YELLOW, 5)            # top
# arcade.draw_arc_outline(100, 375,  50,  50, arcade.color.ARYLIDE_YELLOW, 90, 180, 5)   # upper left corner
# arcade.draw_line(        50, 375,  50, 325, arcade.color.ARYLIDE_YELLOW, 5)            # home side
# arcade.draw_arc_outline(100, 325,  50,  50, arcade.color.ARYLIDE_YELLOW, 180, 270, 5)  # lower left corner
draw_xyhw_rectangle_rounded_corners(50, 485, 500, 100, 50, arcade.color.ARYLIDE_YELLOW, 5)

# Draw home score 
home_score_frame = ((165, 400), (235, 400), (235, 470), (165, 470)) # a 70 x 70 box
arcade.draw_polygon_filled(home_score_frame, arcade.color.OLD_SILVER)
home_score_frame_shadow = ((165, 400), (235, 400), (235, 405), (170, 405))
arcade.draw_polygon_filled(home_score_frame_shadow, arcade.color.ONYX)
arcade.draw_line(235, 400, 235, 470, arcade.color.ONYX, SHADOW_DEPTH)
arcade.draw_text('3', 185, 415, arcade.color.WHITE_SMOKE, 48, 2000, '', ('Calibri', 'Arial'), True)

# Draw visitor score
visitor_score_frame = ((370, 400), (440, 400), (440, 470), (370, 470))
arcade.draw_polygon_filled(visitor_score_frame, arcade.color.OLD_SILVER, )
visitor_score_frame_shadow = ((370, 400), (440, 400), (440, 405), (375, 405))
arcade.draw_polygon_filled(visitor_score_frame_shadow, arcade.color.ONYX)
arcade.draw_line(440, 400, 440, 470, arcade.color.ONYX, SHADOW_DEPTH)
arcade.draw_text("2", 390, 415, arcade.color.WHITE_SMOKE, 48, 2000, '', ('Calibri', 'Arial'),  True)



# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
