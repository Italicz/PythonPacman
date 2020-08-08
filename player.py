import pygame
from settings import *
vec = pygame.math.Vector2

class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pixel_pos = vec((self.grid_pos.x*self.app.cell_width)+top_bottom_buffer//2+self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+top_bottom_buffer//2+self.app.cell_height//2)
        self.direction = vec(1,0)
    
    def update(self):
        self.pixel_pos += self.direction

        #Setting the grid positition to the same as the pixel position
        self.grid_pos[0] = (self.pixel_pos[0]-top_bottom_buffer+self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pixel_pos[1]-top_bottom_buffer+self.app.cell_height//2)//self.app.cell_height+1

    def draw(self):
        pygame.draw.circle(self.app.screen, player_colour, (int(self.pixel_pos.x), int(self.pixel_pos.y)), self.app.cell_width//2)

    def move(self, direction):
        self.direction = direction