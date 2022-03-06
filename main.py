import time
import math
import pygame
from lib.vector2 import *

# ===== imports from classes folder =====
from classes.screen import screen
from classes.components.Mesh import *
from classes.GameManager import GameManager
from classes.components.Transform import Transform
from classes.components.Texture import Texture
from classes.components.Text import *
from classes.GameObject import GameObject
from classes.components.Collider import Collider

pygame.init()

# ===== pygame variables =====
running = True
clock = pygame.time.Clock()
tick = 0
framerate = 60
gm = GameManager()

# ===== keep this variable false unless you need to test your fps =====
frameTest = False
curTime = None

g = GameObject( [Transform(Vector2(100, 100), Vector2(128, 64), 0), Mesh(MeshType.SQUARE, (255, 0, 0)) ] )
#a = GameObject( [ Transform(Vector2(100, 300), Vector2(128, 64), 0), Mesh(MeshType.SQUARE, (0, 255, 0)), Collider() ] )
a = GameObject( [ Transform(Vector2(100, 300), Vector2(128, 64), 0), Collider() ] )
a.getComponent(Collider).viewMode = True
#t = GameObject( [ Transform(Vector2(400, 300), Vector2(128, 64), 0), Text("hello", (255, 255, 0), Font("res/srccodelight.ttf", 40)) ] )

gm.addGameObject(g)
gm.addGameObject(a)
#gm.addGameObject(t)

if frameTest:
    curTime = time.time()

# ===== main loop =====
while running:
    gm.lastUpdate()

    if frameTest and tick == framerate:
        break

    pressed = pygame.key.get_pressed()
    mousePos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    mousePressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pressed[pygame.K_w]: g.transform.pos.y -= 3
    if pressed[pygame.K_a]: g.transform.pos.x -= 3
    if pressed[pygame.K_s]: g.transform.pos.y += 3
    if pressed[pygame.K_d]: g.transform.pos.x += 3

    if pressed[pygame.K_r]: 
        g.transform.rotation += 2

    if a.getComponent(Collider).onCollisionStay(g):
        print(f"ok: {tick}")

    screen.fill((0, 0, 0))
    gm.update()

    pygame.display.update()
    clock.tick(60)
    tick += 1


# ===== frame testing stuff =====
if frameTest:
    avgFramerate = abs(int(framerate / (curTime - time.time())))

    if avgFramerate < 20:
        print(f"======= [FPS test] =======\nExtreme lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    elif avgFramerate < 30:
        print(f"======= [FPS test] =======\nLarge lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    elif avgFramerate < 40:
        print(f"======= [FPS test] =======\nDecent lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    elif avgFramerate < 50:
        print(f"======= [FPS test] =======\nModerate lag detected (Info below)\nAmount of GameObjects: {len(gm.gameObjects)}\nApprox Framerate: {avgFramerate}")

    else:
        print(f"[FPS test] Little to no lag detected\nApprox Framerate: {avgFramerate}")

    print(f"Test ran for: {round(abs(curTime - time.time()), 2)} seconds")