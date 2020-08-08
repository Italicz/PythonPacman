import pygame, sys
from settings import *
from player import *

pygame.init()
vec = pygame.math.Vector2

######################## SETUP ########################

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width =maze_width//28
        self.cell_height = maze_height//30
        self.player = Player(self, player_start_pos)
        self.walls = []
        self.coins = []

        self.load()
        #self.run()
    
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()

######################## OTHER FUNCTIONS ########################
    
    def draw_text(self, screen, pos, size, colour, font_name, text, centred=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(text, False, colour)
        text_size = text.get_size()
        if centred:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.maze = pygame.image.load('images/maze.png')
        self.maze = pygame.transform.scale(self.maze, (maze_width, maze_height))

        #Opening walls file, creating list with x and y coords of walls
        with open("walls.txt", 'r') as file:
            for yindex, line in enumerate(file):
                for xindex, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xindex, yindex))
                    elif char == "0":
                        self.coins.append(vec(xindex, yindex))


######################## START SCREEN ########################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'    

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(black)
        self.draw_text(self.screen, [width//2, height//2], start_text_size, (170, 140, 60), start_font, 'PUSH SPACE TO START', centred=True)
        self.draw_text(self.screen, [width//2, height//2+100], start_text_size, (0, 140, 60), start_font, 'GOOD LUCK!', centred=True)
        self.draw_text(self.screen, [0,0], start_text_size, (255, 255, 255), start_font, 'HIGH SCORE', centred=False)

        pygame.display.update()

######################## PLAYING SCREEN ########################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                    
    
    def playing_update(self):
        self.player.update()
    
    def playing_draw(self):
        self.screen.fill(black)
        self.screen.blit(self.maze, (top_bottom_buffer//2, top_bottom_buffer//2))
        self.draw_coins()
        #self.draw_grid()
        self.draw_text(self.screen, (width//2-150,5), 20, (255,255,255), start_font, 'HIGH SCORE: 0', centred=False)
        self.draw_text(self.screen, (width//2+100,5), 20, (255,255,255), start_font, 'SCORE: {}'.format(self.player.current_score), centred=False)
        self.player.draw()
        pygame.display.update()
        #self.coins.pop()

    def draw_grid(self):
        for x in range(width//self.cell_width):
            pygame.draw.line(self.maze, grey, (x*self.cell_width, 0), (x*self.cell_width, height))
        for x in range(height//self.cell_height):
            pygame.draw.line(self.maze, grey, (0, x*self.cell_height), (width, x*self.cell_height))

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (195,198,118), (int(coin.x*self.cell_width)+self.cell_width//2+top_bottom_buffer//2, int(coin.y*self.cell_height)+self.cell_height//2+top_bottom_buffer//2), 3)