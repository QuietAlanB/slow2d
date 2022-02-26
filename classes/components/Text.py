import pygame

class Font:
    def __init__(self, fileName, size):
        self.name = fileName
        self.size = size
        self.font = pygame.font.Font(fileName, size)

class Text:
    def __init__(self, string, color, font, lineSpacing = 10):
        self.string = str(string).split("\n")
        self.lines = len(self.string)
        self.color = color
        self.font = font
        self.lineSpacing = lineSpacing