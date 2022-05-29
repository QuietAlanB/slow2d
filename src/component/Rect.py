import pygame
from screen import screen
import math

class Rect:
        def __init__(self, color):
                self.color = color

        def update(self, transform):
                s = pygame.Surface((transform.size.x , transform.size.y), pygame.SRCALPHA)

                pygame.draw.rect(
                        s, 
                        self.color, 
                        pygame.Rect(0, 0, transform.size.x, transform.size.y)
                        )

                rotated_image = pygame.transform.rotozoom(s, transform.rotation, 1)
                new_rect = rotated_image.get_rect(center = s.get_rect(center = (transform.pos.x, transform.pos.y)).center)

                # === all coordinate adjustments ===
                angle = transform.rotation
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