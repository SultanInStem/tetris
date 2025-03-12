from config import SCREEN_SIZE, GRID_SIZE
import pygame
class Grid: 
    def __init__(self): ## size is usually 10x20 ratio
        pass

    def draw(self, screen): 
        pygame.draw.rect(
            screen, 
            (255,0,0), 
            (100,100,GRID_SIZE[0],GRID_SIZE[1]),
            0
        )