from pygame.math import Vector2 as vec

#Screen settings
width, height = 610, 670
fps = 60
start_text_size = 30
start_font = 'lithograph'
top_bottom_buffer = 50
maze_width, maze_height = width-top_bottom_buffer, height-top_bottom_buffer

cols = 28
rows = 30

#Colour settings
black = (0,0,0)
red = (208, 22, 22)
grey = (107,107,107)
player_colour = (247,255,0)

#Player settings
player_start_pos = vec(13,23)

#Ghost settings