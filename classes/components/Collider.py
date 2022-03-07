import pygame
from classes.screen import screen


class Collider:
    def __init__(self):
        self.transform = None
        self.viewMode = False

    def onCollisionStay(self, gameObject):
        axes = [self.transform.topRight - self.transform.topLeft, 
        self.transform.topRight - self.transform.bottomRight, 
        gameObject.transform.topLeft - gameObject.transform.bottomLeft, 
        gameObject.transform.topLeft - gameObject.transform.topRight]

        axesTrue = [False, False, False, False]

        for i in range(4):
            projSelfTR1 = axes[i] * (self.transform.topRight.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))
            projSelfTL1 = axes[i] * (self.transform.topLeft.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))
            projSelfBR1 = axes[i] * (self.transform.bottomRight.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))
            projSelfBL1 = axes[i] * (self.transform.bottomLeft.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))

            projOtherTR1 = axes[i] * (gameObject.transform.topRight.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))
            projOtherTL1 = axes[i] * (gameObject.transform.topLeft.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))
            projOtherBR1 = axes[i] * (gameObject.transform.bottomRight.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))
            projOtherBL1 = axes[i] * (gameObject.transform.bottomLeft.dot(axes[i]) / (axes[i].x ** 2 + axes[i].y ** 2))

            projSelfAx1 = [projSelfTR1.dot(axes[i]), projSelfTL1.dot(axes[i]), projSelfBR1.dot(axes[i]), projSelfBL1.dot(axes[i])]
            projOtherAx1 = [projOtherTR1.dot(axes[i]), projOtherTL1.dot(axes[i]), projOtherBR1.dot(axes[i]), projOtherBL1.dot(axes[i])]

            maxSelfAx1 = max(projSelfAx1)
            maxOtherAx1 = max(projOtherAx1)

            minSelfAx1 = min(projSelfAx1)
            minOtherAx1 = min(projOtherAx1)

            if minOtherAx1 <= maxSelfAx1 and maxOtherAx1 >= minSelfAx1:
                continue
            else:
                return False

        return True
        
