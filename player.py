import pygame
from settings import *
vec = pygame.math.Vector2

class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pixel_pos = vec((self.grid_pos.x*self.app.cell_width)+top_bottom_buffer//2+self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+top_bottom_buffer//2+self.app.cell_height//2)
        print(self.grid_pos, self.pixel_pos)
    
    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, player_colour, (int(self.pixel_pos.x), int(self.pixel_pos.y)), self.app.cell_width//2)