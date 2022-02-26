import time
import tracemalloc
import pygame
from classes.GameObject import GameObject
from lib.vector2 import *

# ===== imports from classes folder =====
from classes.screen import screen
from classes.components.Mesh import *
from classes.GameManager import GameManager
from classes.components.Transform import Transform
from classes.components.Texture import Texture

# ===== pygame variables =====
running = True
clock = pygame.time.Clock()
tick = 0
framerate = 60
gm = GameManager()

# ===== keep this variable false unless you need to test your fps =====
frameTest = False
curTime = None

g = GameObject( [Transform(Vector2(0, 0), Vector2(20, 20)), Mesh(MeshType.SQUARE, (255, 0, 0))] )
gm.addGameObject(g)

if frameTest:
    curTime = time.time()

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

    if frameTest and tick == framerate:
        break

    pygame.display.update()
    clock.tick(60)
    tick += 1

if frameTest:
    avgFramerate = abs(int(framerate / (curTime - time.time())))

    if avgFramerate < 20:
        print(f"======= [FPS test] =======\nExtreme lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    if avgFramerate < 30:
        print(f"======= [FPS test] =======\nHuge lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    elif avgFramerate < 40:
        print(f"======= [FPS test] =======\nDecent lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    elif avgFramerate < 50:
        print(f"======= [FPS test] =======\nModerate lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    else:
        print(f"[FPS test] Little to no lag detected\nApprox Framerate: {avgFramerate}")

    print(f"Test ran for: {round(abs(curTime - time.time()), 2)} seconds")