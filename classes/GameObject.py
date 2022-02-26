from vector2 import Vector2

class GameObject:
    def __init__(self, pos):
        self.lastPos = pos
        self.pos = pos

    def lastPosUpdate(self):
        self.lastPos = Vector2(self.pos.x, self.pos.y)