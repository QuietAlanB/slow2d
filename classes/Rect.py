from classes.screen import screen
from classes.GameObject import GameObject
import pygame

class Rect(GameObject):
    def __init__(self, pos, size, color):
        super().__init__(pos)
        self.size = size
        self.color = color

    def lastPosUpdate(self):
        super().lastPosUpdate()

    def update(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y))

    