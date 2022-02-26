import pygame
from vector2 import *

# ===== imports from classes folder =====
from classes.screen import screen
from classes.Rect import Rect
from classes.GameManager import GameManager

# ===== pygame variables =====
running = True
clock = pygame.time.Clock()
tick = 0
framerate = 60
gm = GameManager()

r = Rect(Vector2(0, 0), Vector2(100, 100), (255, 255, 255))

gm.addGameObject(r)

# ===== main loop =====
while running:
    gm.lastPosUpdate()

    pressed = pygame.key.get_pressed()
    mousePos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    gm.update()

    pygame.display.update()
    clock.tick(60)
    tick += 1