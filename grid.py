from config import SCREEN_SIZE, GRID_SIZE, BLOCK_SIZE
import pygame
class Grid: 
    def __init__(self): ## size is usually 10x20 ratio
        self.pos = ((SCREEN_SIZE[0] - GRID_SIZE[0]) // 2, 0)

    def draw(self, screen): 
        pygame.draw.rect(
            screen, 
            (255,0,0), 
            (self.pos[0],self.pos[1],GRID_SIZE[0],GRID_SIZE[1]),
            1
        )

        for x in range(0, GRID_SIZE[0] // BLOCK_SIZE): 
            pygame.draw.line(
                screen, 
                (255,0,0), 
                (self.pos[0] + BLOCK_SIZE * x, 0), 
                (self.pos[0] + BLOCK_SIZE * x, GRID_SIZE[1]), 
                1
            )
        for y in range (0, GRID_SIZE[1] // BLOCK_SIZE): 
            pygame.draw.line(
                screen, 
                (0,255,0), 
                (self.pos[0], self.pos[1] + BLOCK_SIZE * y),
                (self.pos[0] + GRID_SIZE[0], self.pos[1] + BLOCK_SIZE * y),
                1
            )
