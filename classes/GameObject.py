from vector2 import Vector2

class GameObject:
    def __init__(self, pos):
        self.lastPos = pos
        self.pos = pos
        self.components = []

        # TODO:
        # make components and give each an update function
        # and just update them

    def lastPosUpdate(self):
        self.lastPos = Vector2(self.pos.x, self.pos.y)