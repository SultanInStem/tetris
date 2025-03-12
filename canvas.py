import pygame
import sys 
from config import SCREEN_SIZE
from grid import Grid
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Tetris")

        self.running = True 
        self.clock = pygame.time.Clock()
        self.fps = 20 
        self.font = pygame.font.SysFont("Arial", 30)
        

        self.grid = Grid()

    def draw_text(self, text, font, text_color, pos): 
        img = font.render(text, True, text_color)
        self.screen.blit(img, pos)



    def update(self): 
        pass 
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False 
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]: 
                    ## rotate tetramino 
                    pass 
                elif keys[pygame.K_LEFT]: 
                    ## move tetramino to the left 
                    pass 
                elif keys[pygame.K_RIGHT]:
                    ## move tetramino to the right  
                    pass 

    def render(self): 
        self.screen.fill((0,0,0))

        # self.draw_text("Hello world", self.font, (255,0,0), (600,400))
        self.grid.draw(self.screen)

        
        pygame.display.flip()
        self.clock.tick(self.fps)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()
