"""
This is a sample program to show how to draw using functions
"""

import arcade
import random

SHADOW_DEPTH = 5
SPOT_SIZE = 3.5
FACE = [
    arcade.color.ALMOND,
    arcade.color.LION,
    arcade.color.OTTER_BROWN,
    arcade.color.OLD_BURGUNDY
    ]
SHIRT = [
    arcade.color.PASTEL_PURPLE, 
    arcade.color.ALABAMA_CRIMSON,
    arcade.color.PASTEL_RED,
    arcade.color.PASTEL_VIOLET
    ]
PANT = [
    arcade.color.MIDNIGHT_BLUE,
    arcade.color.OUTER_SPACE,
    arcade.color.NEW_CAR
    ]    

def draw_team_marque():
    """
    Draw home and visitor marque
    """

    arcade.draw_xywh_rectangle_filled(70, 500, 230, 50, arcade.color.BRICK_RED)
    arcade.draw_xywh_rectangle_filled(300, 500, 230, 50, arcade.color.OCEAN_BOAT_BLUE)

    arcade.draw_polygon_filled(((200, 550), (400, 550), (350, 500), (250, 500)), arcade.color.OLD_SILVER)
    arcade.draw_line(70, 498, 250, 498, arcade.color.PRUNE, SHADOW_DEPTH)
    arcade.draw_line(250, 498, 349, 498, arcade.color.ONYX, SHADOW_DEPTH) 
    arcade.draw_line(349, 498, 530, 498, arcade.color.PRUSSIAN_BLUE, SHADOW_DEPTH) 

    arcade.draw_text("Home", 130, 515, arcade.color.WHITE_SMOKE, 20, 2, '', ('Calibri', 'Arial'), True)
    arcade.draw_text("Visitor", 410, 515, arcade.color.WHITE_SMOKE, 20, 2000, '', ('Calibri', 'Arial'), True)
    arcade.draw_text("vs", 276, 515, arcade.color.WHITE_SMOKE, 36, 2000, '', ('Calibri', 'Arial'), True)

    # Draw team logo
    red_logo = arcade.load_texture("c:\\VSCode\\dub-ab-arcade-games-work\\Lab 02 - Draw a Picture\\images\\red-parrot.png")
    blue_logo = arcade.load_texture("c:\\VSCode\\dub-ab-arcade-games-work\\Lab 02 - Draw a Picture\\images\\blue-hippo.png")
    scale = .25
    arcade.draw_texture_rectangle(70, 525, scale * red_logo.width, scale * red_logo.height, red_logo, 45)
    arcade.draw_texture_rectangle(530, 525, scale * blue_logo.width, scale * blue_logo.height, blue_logo, 315)

def draw_pitch():
    """
    Draw and decorate the pitch
    """
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

def draw_home_score(home_score):
    """
    Draw and decorate the home numeric score board

    Where:
    :``home_score``: is the number of points to show (str)
    Returns:
    None
    Raises:
    None
    """
    home_score_frame = ((165, 400), (235, 400), (235, 470), (165, 470)) # a 70 x 70 box
    arcade.draw_polygon_filled(home_score_frame, arcade.color.OLD_SILVER)
    home_score_frame_shadow = ((165, 400), (235, 400), (235, 405), (170, 405))
    arcade.draw_polygon_filled(home_score_frame_shadow, arcade.color.ONYX)
    arcade.draw_line(235, 400, 235, 470, arcade.color.ONYX, SHADOW_DEPTH)
    arcade.draw_text(home_score, 185, 415, arcade.color.WHITE_SMOKE, 48, 2000, '', ('Calibri', 'Arial'), True)

def draw_visitor_score(visitor_score):
    """
    Draw and decorate the visitor numeric score board

    Where:
    :``visitor_score``: is the number of points to show (str)
    Returns:
    None
    Raises:
    None    
    """
    visitor_score_frame = ((370, 400), (440, 400), (440, 470), (370, 470))
    arcade.draw_polygon_filled(visitor_score_frame, arcade.color.OLD_SILVER, )
    visitor_score_frame_shadow = ((370, 400), (440, 400), (440, 405), (375, 405))
    arcade.draw_polygon_filled(visitor_score_frame_shadow, arcade.color.ONYX)
    arcade.draw_line(440, 400, 440, 470, arcade.color.ONYX, SHADOW_DEPTH)
    arcade.draw_text("2", 390, 415, arcade.color.WHITE_SMOKE, 48, 2000, '', ('Calibri', 'Arial'),  True)

def draw_person(position_x, position_y):
    """
    This function draws an abstraction of a person.
    """
    face_color = random.choice(FACE)
    shirt_color = random.choice(SHIRT)
    pant_color = random.choice(PANT)

    # arcade.draw_point(position_x, position_y, face_color, 5)
    # arcade.draw_point(position_x, position_y - 5, shirt_color, 5)
    # arcade.draw_point(position_x, position_y - 10, pant_color, 5)
    arcade.draw_point(position_x, position_y, face_color, 3)
    arcade.draw_point(position_x, position_y - 3, shirt_color, 3)
    arcade.draw_point(position_x, position_y - 6, pant_color, 3)

def draw_stands(quantity_of_people):
    """
    Draw the stands

    Where:
        ``quantity_of_people`` is the number of people to draw (int) \
    Returns:
        None
    Raises:
        None
    """
    arcade.draw_line(90, 220, 145, 350, arcade.color.BLACK, 2) # Left stand wall
    arcade.draw_line(145, 350, 455, 350, arcade.color.BLACK, 2) # back stand wall
    arcade.draw_line(455, 350, 510, 220, arcade.color.BLACK, 2) # right stand wall    
    
    for q in range(quantity_of_people):

        x_location = random.randint(50, 550)
        y_location = random.randint(225, 350)

        draw_person(x_location, y_location)

    arcade.draw_triangle_filled( 40, 100,  40, 355, 145, 355, arcade.color.DARK_IMPERIAL_BLUE)
    arcade.draw_triangle_filled(560, 100, 560, 355, 455, 355, arcade.color.DARK_IMPERIAL_BLUE)
    arcade.draw_rectangle_filled(300, 211, 420, 20, arcade.color.OLD_SILVER, 0)


def main():
    """ 
    This is the main function that we call to run the program.
    """
    
    # Open up a window.
    # From the "arcade" library, use a function called "open_window"
    # Set the and dimensions (width and height)
    arcade.open_window(600, 600, "Drawing Example - Scoreboard with Functions")

    # set the background color 
    arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)
    # Get ready to draw
    arcade.start_render()

    draw_team_marque()
    draw_pitch()
    draw_xyhw_rectangle_rounded_corners(50, 485, 500, 100, 50, arcade.color.ARYLIDE_YELLOW, 5)
    draw_home_score("3")
    draw_visitor_score("2")
    draw_stands(7000)

    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
if __name__ == "__main__":
    main()