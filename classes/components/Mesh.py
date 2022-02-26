import enum

class MeshType(enum.Enum):
    SQUARE = 0
    CIRCLE = 1

class Mesh:
    def __init__(self, meshType, color):
        self.meshType = meshType
        self.color = color