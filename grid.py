from config import SCREEN_SIZE, GRID_SIZE
import pygame
class Grid: 
    def __init__(self): ## size is usually 10x20 ratio
        self.pos = ((SCREEN_SIZE[0] - GRID_SIZE[0]) // 2, 0)
        self.block_size = GRID_SIZE[0] // 10

    def draw(self, screen): 
        pygame.draw.rect(
            screen, 
            (255,0,0), 
            (self.pos[0],self.pos[1],GRID_SIZE[0],GRID_SIZE[1]),
            1
        )
        for x in range(0, GRID_SIZE[0] // self.block_size):
            pygame.draw.line(
                screen, 
                (255,0,0), 
                (self.pos[0] + 30 * x, 0),
                (self.pos[0] + 30 * x, SCREEN_SIZE[1]),
                1
            ) 
