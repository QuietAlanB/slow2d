from lib.vector2 import Vector2

class Transform:
    def __init__(self, pos, size, rotation):
        self.pos = pos
        self.size = size
        self.rotation = rotation

        self.topLeft = Vector2(self.pos.x, self.pos.x)
        self.topRight = self.pos + Vector2(self.size.x, 0)
        self.bottomLeft = self.pos + Vector2(0, self.size.y)
        self.bottomRight = self.pos + self.size

        self.lastPos = Vector2(self.pos.x, self.pos.y)
    
        self.center = self.size / 2
