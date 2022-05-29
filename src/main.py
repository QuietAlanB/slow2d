import pygame
from screen import screen

running = True
clock = pygame.time.Clock()

while running:
        for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                        running = False

        pygame.display.update()
        clock.tick(60)