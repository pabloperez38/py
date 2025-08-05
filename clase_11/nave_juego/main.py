import pygame
import random
from config import WIDTH, HEIGHT, FPS, COLOR_FONDO, COLOR_TEXTO
from nave import Nave
from enemigo import Enemigo
from utils import colision

pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Naves - POO")
reloj = pygame.time.Clock()

fuente = pygame.font.SysFont("Arial", 28)

def dibujar_texto(texto, x, y):
    img = fuente.render(texto, True, COLOR_TEXTO)
    pantalla.blit(img, (x, y))

def main():
    nave = Nave()
    enemigos = []
    puntuacion = 0
    corriendo = True
    spawn_timer = 0

    while corriendo:
        reloj.tick(FPS)
        pantalla.fill(COLOR_FONDO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    nave.disparar()

        teclas = pygame.key.get_pressed()
        nave.mover(teclas)
        nave.dibujar(pantalla)

        # Generar enemigos
        spawn_timer += 1
        if spawn_timer > 40:
            enemigos.append(Enemigo())
            spawn_timer = 0

        # Mover y dibujar enemigos
        for enemigo in enemigos[:]:
            enemigo.mover()
            enemigo.dibujar(pantalla)
            if not enemigo.vivo:
                enemigos.remove(enemigo)
            # Colisión con nave
            if colision((nave.x, nave.y, nave.ancho, nave.alto), (enemigo.x, enemigo.y, enemigo.ancho, enemigo.alto)):
                nave.vidas -= 1
                enemigos.remove(enemigo)
                if nave.vidas <= 0:
                    corriendo = False

        # Colisiones disparo-enemigo
        for disparo in nave.disparos[:]:
            for enemigo in enemigos[:]:
                if colision((disparo.x - disparo.radio, disparo.y - disparo.radio, disparo.radio*2, disparo.radio*2), (enemigo.x, enemigo.y, enemigo.ancho, enemigo.alto)):
                    nave.disparos.remove(disparo)
                    enemigos.remove(enemigo)
                    puntuacion += 10
                    break

        dibujar_texto(f"Puntos: {puntuacion}", 10, 10)
        dibujar_texto(f"Vidas: {nave.vidas}", 10, 40)
        pygame.display.flip()

    # Pantalla de Game Over
    pantalla.fill(COLOR_FONDO)
    dibujar_texto("GAME OVER", WIDTH//2 - 100, HEIGHT//2 - 40)
    dibujar_texto(f"Puntaje final: {puntuacion}", WIDTH//2 - 120, HEIGHT//2)
    pygame.display.flip()
    pygame.time.wait(2500)
    pygame.quit()

if __name__ == "__main__":
    main() 