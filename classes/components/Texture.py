import pygame

class Texture:
    def __init__(self, imagePath):
        self.texture = pygame.image.load(imagePath)