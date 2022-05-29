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
from classes.components.RectCollider import RectCollider
from classes.components.CircleCollider import CircleCollider

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

car = GameObject( [Transform(Vector2(100, 100), Vector2(24, 64), 0), Mesh(MeshType.SQUARE, (255, 0, 0)), RectCollider() ] )
wall1 = GameObject( [Transform(Vector2(100, 100), Vector2(48, 96), 0), Mesh(MeshType.SQUARE, (100, 100, 100)), RectCollider() ] )

gm.addGameObject(car)
gm.addGameObject(wall1)

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

        if pressed[pygame.K_a]: car.transform.rotation += 2
        if pressed[pygame.K_d]: car.transform.rotation -= 2

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