class GameManager:
    def __init__(self):
        self.gameObjects = []

    # ===== update function =====
    def update(self):
        for gameObject in self.gameObjects:
            gameObject.update()

    # ===== game object list functions =====
    def addGameObject(self, object):
        self.gameObjects.append(object)

    def addGameObjects(self, objects):
        for obj in objects:
            self.gameObjects.append(obj)

    def removeGameObject(self, object):
        self.gameObjects.remove(object)

    def removeGameObjects(self, objects):
        for obj in objects:
            self.gameObjects.remove(obj)