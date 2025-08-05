import pygame
from config import COLOR_DISPARO

class Disparo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 5
        self.velocidad = 10

    def mover(self):
        self.y -= self.velocidad

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, COLOR_DISPARO, (self.x, self.y), self.radio) 