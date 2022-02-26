import pygame
from classes.GameObject import GameObject
from lib.vector2 import *

# ===== imports from classes folder =====
from classes.screen import screen
from classes.components.Mesh import *
from classes.GameManager import GameManager
from classes.components.Transform import Transform

# ===== pygame variables =====
running = True
clock = pygame.time.Clock()
tick = 0
framerate = 60
gm = GameManager()

g = GameObject( [Transform(Vector2(0, 0), Vector2(10, 10)), Mesh(MeshType.CIRCLE, (255, 0, 0))] )

gm.addGameObject(g)

# ===== main loop =====
while running:
    pressed = pygame.key.get_pressed()
    mousePos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pressed[pygame.K_w]: g.transform.pos.y -= 3
    if pressed[pygame.K_a]: g.transform.pos.x -= 3
    if pressed[pygame.K_s]: g.transform.pos.y += 3
    if pressed[pygame.K_d]: g.transform.pos.x += 3

    screen.fill((0, 0, 0))
    gm.update()

    pygame.display.update()
    clock.tick(60)
    tick += 1