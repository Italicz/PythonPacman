import pygame
from settings import *
vec = pygame.math.Vector2

class Player:
    def __init__(self, app, pos):
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pixel_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.stored_direction = None
        self.allowed_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 3
    
    def update(self):
        if self.allowed_to_move:
            self.pixel_pos += self.direction*self.speed

        if self.time_to_move():
          if self.stored_direction !=None:
            self.direction = self.stored_direction
          self.allowed_to_move = self.can_move()

        #Setting the grid positition to the same as the pixel position
        self.grid_pos[0] = (self.pixel_pos[0]-top_bottom_buffer+self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pixel_pos[1]-top_bottom_buffer+self.app.cell_height//2)//self.app.cell_height+1

        if self.on_coin():
            self.eat_coin()

    def time_to_move(self):
      if int(self.pixel_pos.x+top_bottom_buffer//2) % self.app.cell_width == 0:
        if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
          return True
      if int(self.pixel_pos.y+top_bottom_buffer//2) % self.app.cell_height == 0:
        if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
          return True   
      return False

    def draw(self):
        pygame.draw.circle(self.app.screen, player_colour, (int(self.pixel_pos.x), int(self.pixel_pos.y)), self.app.cell_width//2)

        for x in range(self.lives):
          pygame.draw.circle(self.app.screen, player_colour, (35 + 20*x, height -15), 7)

    def get_pix_pos(self):
      return vec((self.grid_pos[0]*self.app.cell_width)+top_bottom_buffer//2+self.app.cell_width//2, (self.grid_pos[1]*self.app.cell_height) + top_bottom_buffer//2+self.app.cell_height//2)
      print(self.grid_pos, self.pixel_pos)

    def on_coin(self):
        if self.grid_pos in self.app.coins:
            return True
        return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 100

    def move(self, direction):
        self.stored_direction = direction

    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True