class Transform:
        def __init__(self, pos, rotation, size):
                self.pos = pos
                self.rotation = rotation
                self.size = size

        def Move(self, x, y):
                self.pos.x += x
                self.pos.y += y

        def Rotate(self, amount):
                self.rotation += amount

        def Scale(self, amount):
                self.size *= amount