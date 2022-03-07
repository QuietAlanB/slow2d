from classes.components.Collider import Collider
from classes.components.Text import Text
from classes.screen import screen
from classes.components.Transform import Transform
from classes.components.Texture import Texture
from classes.components.Mesh import *
from pygame import gfxdraw
import math
import pygame

from lib.vector2 import Vector2

class GameObject:
    def __init__(self, components = []):
        self.components = components
        self.transform = None

        for c in self.components:
            if type(c) == Transform:
                self.transform = c

            if type(c) == Collider:
                c.transform = self.transform


    # ===== add component =====
    def addComponent(self, component):
        self.components.append(component)

    # ===== remove component =====
    def removeComponent(self, component):
        self.components.remove(component)


    # ===== get component =====
    def getComponent(self, component):
        for c in self.components:
            if type(c) == component:
                return c

        return None


    # ===== last update =====
    def lastUpdate(self):
        self.transform.lastPos = Vector2(self.transform.pos.x, self.transform.pos.y)


    # ===== update =====
    def update(self):
        for c in self.components:
            if type(c) == Mesh:
                # ===== square =====
                if c.meshType == MeshType.SQUARE:
                    s = pygame.Surface((self.transform.size.x , self.transform.size.y), pygame.SRCALPHA)

                    pygame.draw.rect(s, c.color, pygame.Rect(0, 0, self.transform.size.x, self.transform.size.y))

                    rotated_image = pygame.transform.rotozoom(s, self.transform.rotation, 1)
                    new_rect = rotated_image.get_rect(center = s.get_rect(center = (self.transform.pos.x, self.transform.pos.y)).center)

                    # === all coordinate adjustments ===

                    # === all coordinate adjustments ===
                    angle = self.transform.rotation
                    angle -= angle * 2

                    self.transform.topRight.x = self.transform.center.x + ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                    self.transform.topRight.y = self.transform.center.y + ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                    self.transform.topLeft.x = self.transform.center.x - ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                    self.transform.topLeft.y = self.transform.center.y - ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                    self.transform.bottomLeft.x = self.transform.center.x - ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                    self.transform.bottomLeft.y = self.transform.center.y - ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                    self.transform.bottomRight.x = self.transform.center.x + ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                    self.transform.bottomRight.y = self.transform.center.y + ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                    # === draw ===
                    screen.blit(rotated_image, (new_rect))

                # ===== circle =====
                elif c.meshType == MeshType.CIRCLE:
                    s = pygame.Surface((self.transform.size.x * 2, self.transform.size.y * 2), pygame.SRCALPHA)

                    gfxdraw.aaellipse(s, int(self.transform.size.x), int(self.transform.size.y), int(self.transform.size.x), int(self.transform.size.y), c.color)
                    gfxdraw.filled_ellipse(s, int(self.transform.size.x), int(self.transform.size.y), int(self.transform.size.x), int(self.transform.size.y), c.color)

                    rotated_image = pygame.transform.rotozoom(s, self.transform.rotation, 1)
                    new_rect = rotated_image.get_rect(center = s.get_rect(center = (self.transform.pos.x, self.transform.pos.y)).center)

                    # === all coordinate adjustments ===
                    self.transform.topLeft = Vector2(new_rect.topleft[0], new_rect.topleft[1] )
                    self.transform.topRight = Vector2(new_rect.topright[0], new_rect.topright[1] )
                    self.transform.bottomLeft = Vector2(new_rect.bottomleft[0], new_rect.bottomleft[1] )
                    self.transform.bottomRight = Vector2(new_rect.bottomright[0], new_rect.bottomright[1] )

                    # === draw ===
                    screen.blit(rotated_image, (new_rect))


            # ===== textures =====
            # also does a quick check for custom sizes
            elif type(c) == Texture:
                if c.texture.get_size() != (self.transform.size.x, self.transform.size.y):
                    c.texture = pygame.transform.scale(c.texture, (self.transform.size.x, self.transform.size.y))

                rotated_image = pygame.transform.rotozoom(c.texture, self.transform.rotation, 1)
                new_rect = rotated_image.get_rect(center = c.texture.get_rect(center = (self.transform.pos.x, self.transform.pos.y)).center)

                # === all coordinate adjustments ===
                self.transform.topLeft = Vector2(new_rect.topleft[0], new_rect.topleft[1] )
                self.transform.topRight = Vector2(new_rect.topright[0], new_rect.topright[1] )
                self.transform.bottomLeft = Vector2(new_rect.bottomleft[0], new_rect.bottomleft[1] )
                self.transform.bottomRight = Vector2(new_rect.bottomright[0], new_rect.bottomright[1] )

                # === draw ===
                screen.blit(rotated_image, (new_rect))


            # ===== text =====
            elif type(c) == Text:
                if type(c.string) == str:
                    c.string = c.string.split()

                c.lines = len(c.string)

                yPosOffset = 0

                for line in c.string:
                    line = c.font.font.render(line, True, c.color)
                    screen.blit(line, (self.transform.pos.x, self.transform.pos.y + yPosOffset))
                    
                    yPosOffset += c.font.size + c.lineSpacing


            # ===== collider =====
            elif type(c) == Collider:
                c.transform = self.transform

                s = pygame.Surface((self.transform.size.x , self.transform.size.y), pygame.SRCALPHA)

                if c.viewMode:
                    pygame.draw.rect(s, (0, 200, 0), pygame.Rect(0, 0, self.transform.size.x - 1, self.transform.size.y - 1), 1)

                rotated_image = pygame.transform.rotozoom(s, self.transform.rotation, 1)
                new_rect = rotated_image.get_rect(center = s.get_rect(center = (self.transform.pos.x, self.transform.pos.y)).center)

                # === all coordinate adjustments ===
                angle = self.transform.rotation
                angle -= angle * 2

                self.transform.topRight.x = self.transform.center.x + ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                self.transform.topRight.y = self.transform.center.y + ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                self.transform.topLeft.x = self.transform.center.x - ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                self.transform.topLeft.y = self.transform.center.y - ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                self.transform.bottomLeft.x = self.transform.center.x - ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                self.transform.bottomLeft.y = self.transform.center.y - ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                self.transform.bottomRight.x = self.transform.center.x + ((self.transform.size.x / 2) * math.cos(angle * math.pi/180)) + ((self.transform.size.y / 2) * math.sin(angle * math.pi/180)) + self.transform.pos.x - self.transform.size.x / 2
                self.transform.bottomRight.y = self.transform.center.y + ((self.transform.size.x / 2) * math.sin(angle * math.pi/180)) - ((self.transform.size.y / 2) * math.cos(angle * math.pi/180)) + self.transform.pos.y - self.transform.size.y / 2

                # === draw ===
                if c.viewMode:
                    screen.blit(rotated_image, new_rect)