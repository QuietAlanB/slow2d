from classes.GameObject import GameObject
from pygame import gfxdraw
from classes.screen import screen

class Circle(GameObject):
    def __init__(self, pos, radius, color):
        super().__init__(pos)
        self.radius = radius
        self.color = color

    def lastPosUpdate(self):
        super().lastPosUpdate()

    def update(self):
        gfxdraw.aacircle(screen, int(self.pos.x), int(self.pos.y), int(self.radius), self.color)
        gfxdraw.filled_circle(screen, int(self.pos.x), int(self.pos.y), int(self.radius), self.color)