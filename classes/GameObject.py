from classes.screen import screen
from classes.components.Transform import Transform
from classes.components.Texture import Texture
from classes.components.Mesh import *
from pygame import gfxdraw
import pygame

class GameObject:
    def __init__(self, components = []):
        self.components = components
        self.transform = None

        for c in self.components:
            if type(c) == Transform:
                self.transform = c


    def addComponent(self, component):
        self.components.append(component)


    def removeComponent(self, component):
        self.components.remove(component)


    def update(self):
        for c in self.components:
            if type(c) == Mesh:
                # ===== square =====
                if c.meshType == MeshType.SQUARE:
                    pygame.draw.rect(screen, c.color, pygame.Rect(self.transform.pos.x, self.transform.pos.y, self.transform.size.x, self.transform.size.y))

                # ===== circle =====
                elif c.meshType == MeshType.CIRCLE:
                    gfxdraw.aaellipse(screen, int(self.transform.pos.x), int(self.transform.pos.y), int(self.transform.size.x), int(self.transform.size.y), c.color)
                    gfxdraw.filled_ellipse(screen, int(self.transform.pos.x), int(self.transform.pos.y), int(self.transform.size.x) + 1, int(self.transform.size.y) + 1, c.color)

            # ===== textures =====
            # also does a quick check for custom sizes
            elif type(c) == Texture:
                if c.texture.get_size() != (self.transform.size.x, self.transform.size.y):
                    c.texture = pygame.transform.scale(c.texture, (self.transform.size.x, self.transform.size.y))
                    
                screen.blit(c.texture, (self.transform.pos.x, self.transform.pos.y))