import pygame
import random
from config import WIDTH, COLOR_ENEMIGO

class Enemigo:
    def __init__(self):
        self.ancho = 40
        self.alto = 25
        self.x = random.randint(0, WIDTH - self.ancho)
        self.y = random.randint(-150, -40)
        self.velocidad = random.randint(2, 5)
        self.vivo = True

    def mover(self):
        self.y += self.velocidad
        if self.y > 650:
            self.vivo = False

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_ENEMIGO, (self.x, self.y, self.ancho, self.alto)) 