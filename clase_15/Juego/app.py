import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake 🐍")

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Configuración del Snake
tamano_bloque = 20
velocidad_snake = 10

# Fuente
fuente = pygame.font.SysFont("bahnschrift", 25)

# Función para mostrar puntaje
def mostrar_puntaje(puntaje):
    valor = fuente.render("Puntos: " + str(puntaje), True, blanco)
    ventana.blit(valor, [10, 10])

# Juego principal
def juego():
    game_over = False
    game_close = False

    # Posición inicial
    x = ancho / 2
    y = alto / 2
    x_cambio = 0
    y_cambio = 0

    # Cuerpo del snake
    snake_lista = []
    snake_longitud = 1

    # Comida inicial
    comida_x = round(random.randrange(0, ancho - tamano_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - tamano_bloque) / 20.0) * 20.0

    reloj = pygame.time.Clock()

    while not game_over:

        while game_close:
            ventana.fill(negro)
            mensaje = fuente.render("Perdiste 😢  Presiona C para continuar o Q para salir", True, rojo)
            ventana.blit(mensaje, [ancho / 6, alto / 3])
            mostrar_puntaje(snake_longitud - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_cambio = -tamano_bloque
                    y_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x_cambio = tamano_bloque
                    y_cambio = 0
                elif event.key == pygame.K_UP:
                    y_cambio = -tamano_bloque
                    x_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y_cambio = tamano_bloque
                    x_cambio = 0

        # Bordes de la pantalla
        if x >= ancho or x < 0 or y >= alto or y < 0:
            game_close = True

        x += x_cambio
        y += y_cambio
        ventana.fill(negro)

        # Dibujar comida
        pygame.draw.rect(ventana, rojo, [comida_x, comida_y, tamano_bloque, tamano_bloque])

        # Dibujar snake
        snake_cabeza = []
        snake_cabeza.append(x)
        snake_cabeza.append(y)
        snake_lista.append(snake_cabeza)
        if len(snake_lista) > snake_longitud:
            del snake_lista[0]

        # Colisión con sí mismo
        for bloque in snake_lista[:-1]:
            if bloque == snake_cabeza:
                game_close = True

        for bloque in snake_lista:
            pygame.draw.rect(ventana, verde, [bloque[0], bloque[1], tamano_bloque, tamano_bloque])

        mostrar_puntaje(snake_longitud - 1)
        pygame.display.update()

        # Comer comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ancho - tamano_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto - tamano_bloque) / 20.0) * 20.0
            snake_longitud += 1

        reloj.tick(velocidad_snake)

    pygame.quit()
    quit()

# Ejecutar juego
juego()
