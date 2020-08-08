import pygame
from settings import *
vec = pygame.math.Vector2

class Enemy:
    def __init__(self,app,pos, number):
        self.app = app
        self.grid_pos = pos
        self.pixel_pos = self.get_pixel_pos()
        self.radius = int(self.app.cell_width//2)
        self.number = number
        self.colour = self.set_colour()

    def get_pixel_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+top_bottom_buffer//2+self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+top_bottom_buffer//2+self.app.cell_height//2)

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour, (int(self.pixel_pos.x), int(self.pixel_pos.y)), self.radius)

    def set_colour(self):
        if self.number == 0:
            return (255,0,0)
        if self.number == 1:
            return (255,111,0)
        if self.number == 2:
            return (226,132,220)
        if self.number == 3:
            return (0,247,255)