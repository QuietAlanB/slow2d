import math

class CircleCollider:
        def __init__(self):
                self.transform = None
                self.viewMode = False

        def onCollisionStay(self, gameObject):
                if gameObject.getComponent(CircleCollider) != None:
                        dx = (self.transform.pos.x + self.transform.size.x) - (gameObject.transform.pos.x + gameObject.transform.size.x)
                        dy = (self.transform.pos.y + self.transform.size.x) - (gameObject.transform.pos.y + gameObject.transform.size.x)

                        dist = math.sqrt(dx ** 2 + dy ** 2)

                        return dist <= ((self.transform.size.x) + (gameObject.transform.size.x))

                else:
                        return False