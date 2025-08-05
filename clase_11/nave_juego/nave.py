import pygame
from config import WIDTH, HEIGHT, COLOR_NAVE
from disparo import Disparo

class Nave:
    def __init__(self):
        self.ancho = 50
        self.alto = 30
        self.x = WIDTH // 2 - self.ancho // 2
        self.y = HEIGHT - self.alto - 10
        self.velocidad = 7
        self.vidas = 3
        self.disparos = []
        self.cooldown = 0

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x < WIDTH - self.ancho:
            self.x += self.velocidad

    def disparar(self):
        if self.cooldown == 0:
            disparo = Disparo(self.x + self.ancho // 2, self.y)
            self.disparos.append(disparo)
            self.cooldown = 15

    def actualizar_disparos(self, pantalla):
        for disparo in self.disparos[:]:
            disparo.mover()
            if disparo.y < 0:
                self.disparos.remove(disparo)
            else:
                disparo.dibujar(pantalla)
        if self.cooldown > 0:
            self.cooldown -= 1

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_NAVE, (self.x, self.y, self.ancho, self.alto))
        self.actualizar_disparos(pantalla) 