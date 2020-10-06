import pygame, random
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
        self.direction = vec(1, 0)
        self.personality = self.set_personality()
        print(self.personality)

    def get_pixel_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+top_bottom_buffer//2+self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+top_bottom_buffer//2+self.app.cell_height//2)

    def update(self):
        self.pixel_pos += self.direction
        if self.time_to_move():
          self.move()
        self.grid_pos[0] = (self.pixel_pos[0]-top_bottom_buffer+self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pixel_pos[1]-top_bottom_buffer+self.app.cell_height//2)//self.app.cell_height+1

    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour, (int(self.pixel_pos.x), int(self.pixel_pos.y)), self.radius)

    def time_to_move(self):
      if int(self.pixel_pos.x+top_bottom_buffer//2) % self.app.cell_width == 0:
        if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
          return True
      if int(self.pixel_pos.y+top_bottom_buffer//2) % self.app.cell_height == 0:
        if self.direction == vec(0, 1) or self.direction == vec(0, -1):
          return True   
      return False

    def move(self):
      if self.personality == "random":
        self.direction = self.get_random_direction()

    def get_random_direction(self):
      while True:
        number = random.randint(-2, 1)
        if number == -2:
          x_dir, y_dir = 1,0
        elif number == -1:
          x_dir, y_dir = 0,1
        elif number == 0:
          x_dir, y_dir = -1,0
        else:
          x_dir, y_dir = 0,-1
        next_pos = vec(self.grid_pos.x + x_dir, self.grid_pos.y + y_dir)
        if next_pos not in self.app.walls:
          break
      return vec(x_dir, y_dir)

    def set_colour(self):
        if self.number == 0:
            return (255,0,0)
        if self.number == 1:
            return (255,111,0)
        if self.number == 2:
            return (226,132,220)
        if self.number == 3:
            return (0,247,255)

    def set_personality(self):
      if self.number == 0:
        return "speedy"
      elif self.number == 1:
        return "slow"
      elif self.number == 2:
        return "random"
      else:
        return "scared"