import pygame, random
from settings import *
vec = pygame.math.Vector2

class Enemy:
    def __init__(self,app,pos, number):
        self.app = app
        self.grid_pos = pos
        self.starting_pos = [pos.x, pos.y]
        self.pixel_pos = self.get_pixel_pos()
        self.radius = int(self.app.cell_width//2)
        self.number = number
        self.colour = self.set_colour()
        self.direction = vec(0, 0)
        self.personality = self.set_personality()
        self.target = None
        self.speed = self.set_speed()
        self.lives = 3
        print(self.personality)

    def get_pixel_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+top_bottom_buffer//2+self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+top_bottom_buffer//2+self.app.cell_height//2)

    def update(self):
        self.target = self.set_target()
        if self.target != self.grid_pos:
          self.pixel_pos += self.direction*self.speed
          if self.time_to_move():
            self.move()
        self.grid_pos[0] = (self.pixel_pos[0]-top_bottom_buffer+self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pixel_pos[1]-top_bottom_buffer+self.app.cell_height//2)//self.app.cell_height+1

    def set_speed(self):
      if self.personality in ["speedy", "scared"]:
        speed = 2
      else:
        speed = 1
      return speed

    def set_target(self):
      if self.personality == "speedy" or self.personality == "slow":
        return self.app.player.grid_pos
      else:
        if self.app.player.grid_pos[0] > cols // 2 and self.app.player.grid_pos[1] > rows // 2:
          return vec(1, 1)
        if self.app.player.grid_pos[0] > cols // 2 and self.app.player.grid_pos[1] < rows // 2:
          return vec(1, rows-2)
        if self.app.player.grid_pos[0] < cols // 2 and self.app.player.grid_pos[1] > rows // 2:
          return vec(cols-2, 1)
        else:
          return vec(cols-2, rows-2)

    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour, (int(self.pixel_pos.x), int(self.pixel_pos.y)), self.radius)

    def time_to_move(self):
      if int(self.pixel_pos.x+top_bottom_buffer//2) % self.app.cell_width == 0:
        if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
          return True
      if int(self.pixel_pos.y+top_bottom_buffer//2) % self.app.cell_height == 0:
        if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
          return True   
      return False

    def move(self):
      if self.personality == "random":
        self.direction = self.get_random_direction()
      if self.personality == "slow":
        self.direction = self.get_path_direction(self.target)
      if self.personality == "speedy":
        self.direction = self.get_path_direction(self.target)
      if self.personality == "scared":
        self.direction = self.get_path_direction(self.target)

    def get_path_direction(self, target):
      next_cell = self.find_next_cell_in_path(target)
      xdir = next_cell[0] - self.grid_pos[0]
      ydir = next_cell[1] - self.grid_pos[1]
      return vec(xdir, ydir)

    def find_next_cell_in_path(self, target):
      path = self.BFS([int(self.grid_pos.x), int(self.grid_pos.y)], [int(target[0]), int(target[1])])
      return path[1]

    def BFS(self, start, target):
      grid = [[0 for x in range(28)] for x in range(30)]
      for cell in self.app.walls:
        if cell.x < 28 and cell.y < 30:
          grid[int(cell.y)][int(cell.x)] = 1
      queue = [start]
      path = []
      visited = []
      while queue:
        current = queue[0]
        queue.remove(queue[0])
        visited.append(current)
        if current == target:
          break
        else:
          neighbours = [[0, -1],[1, 0],[0, 1],[-1, 0]]
          for neighbour in neighbours:
            if neighbour[0] + current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
              if neighbour[1] + current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                if next_cell not in visited:
                  if grid[next_cell[1]][next_cell[0]] != 1:
                    queue.append(next_cell)
                    path.append({"Current": current, "Next": next_cell})
      shortest = [target]
      while target != start:
        for step in path:
          if step["Next"] == target:
            target = step["Current"]
            shortest.insert(0, step["Current"])
      return shortest

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