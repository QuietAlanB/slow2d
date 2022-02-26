import pygame
from vector2 import *
from classes import screen

# ===== pygame variables =====
running = True
clock = pygame.time.Clock()
ticks = 0
framerate = 60
screen = screen.screen

# ===== main loop =====
while running:
    pressed = pygame.key.get_pressed()
    mousePos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)