import pygame
from config import SCREEN_SIZE
import sys 

class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_mode("tetris")

        self.running = True 
        self.clock = pygame.time.Clock()
        self.fps = 60 
    def update(self): 
        pass 

    def handle_events(self): 
        pass 
    def render(self): 
        pass 
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()
