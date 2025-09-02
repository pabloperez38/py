import pygame
import random
import sys
import time

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Pantalla
ANCHO, ALTO = 1324, 768
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ahorcado Pro")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 200, 0)
AZUL = (0, 0, 255)
GRIS = (200, 200, 200)
AMARILLO = (255, 255, 0)

# Fuentes
fuente_letra = pygame.font.SysFont(None, 40)
fuente_mensaje = pygame.font.SysFont(None, 50)
fuente_puntaje = pygame.font.SysFont(None, 30)

# Sonidos
sonido_acierto = pygame.mixer.Sound("si.wav")
sonido_fallo = pygame.mixer.Sound("no.wav")

# Imagen de fondo
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Palabras
palabras = ["PYTHON", "PROGRAMACION", "COMPUTADORA", "FLASK", "DESARROLLO", "TECLADO", "RATON"]

# Partículas para efecto de acierto
particulas = []

def crear_particulas(x, y):
    for _ in range(15):
        dx = random.randint(-5,5)
        dy = random.randint(-5,5)
        particulas.append([x, y, dx, dy, random.randint(2,5)])

def actualizar_particulas():
    for p in particulas[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[4] -= 0.2
        pygame.draw.circle(pantalla, AMARILLO, (int(p[0]), int(p[1])), int(max(p[4],0)))
        if p[4] <= 0:
            particulas.remove(p)

# Función para iniciar juego
def iniciar_juego():
    palabra = random.choice(palabras)
    return {
        "palabra": palabra,
        "palabra_guiones": ["_"] * len(palabra),
        "intentos": 6,
        "letras_adivinadas": [],
        "jugando": True,
        "inicio_tiempo": time.time(),
        "puntaje": 0
    }

juego = iniciar_juego()

# Letras disponibles
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_rects = []
inicio_x = 50
inicio_y = 450
espacio = 50
for i, letra in enumerate(letras):
    rect = pygame.Rect(inicio_x + i*espacio, inicio_y, 40, 40)
    letras_rects.append((letra, rect))

# Botón reiniciar
boton_reiniciar = pygame.Rect(650, 500, 120, 50)

# Dibujar ahorcado
def dibujar_ahorcado(intentos):
    pygame.draw.line(pantalla, NEGRO, (150, 500), (350, 500), 5)
    pygame.draw.line(pantalla, NEGRO, (250, 500), (250, 100), 5)
    pygame.draw.line(pantalla, NEGRO, (250, 100), (400, 100), 5)
    pygame.draw.line(pantalla, NEGRO, (400, 100), (400, 150), 5)
    
    if intentos <= 5:
        pygame.draw.circle(pantalla, NEGRO, (400, 180), 30, 3)
    if intentos <= 4:
        pygame.draw.line(pantalla, NEGRO, (400, 210), (400, 300), 3)
    if intentos <= 3:
        pygame.draw.line(pantalla, NEGRO, (400, 230), (350, 270), 3)
    if intentos <= 2:
        pygame.draw.line(pantalla, NEGRO, (400, 230), (450, 270), 3)
    if intentos <= 1:
        pygame.draw.line(pantalla, NEGRO, (400, 300), (350, 350), 3)
    if intentos <= 0:
        pygame.draw.line(pantalla, NEGRO, (400, 300), (450, 350), 3)

# Bucle principal
reloj = pygame.time.Clock()
while True:
    pantalla.blit(fondo, (0,0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if juego["jugando"] and evento.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            for letra, rect in letras_rects:
                if rect.collidepoint(mx, my) and letra not in juego["letras_adivinadas"]:
                    juego["letras_adivinadas"].append(letra)
                    if letra in juego["palabra"]:
                        sonido_acierto.play()
                        crear_particulas(rect.x+20, rect.y+20)
                        for i, l in enumerate(juego["palabra"]):
                            if l == letra:
                                juego["palabra_guiones"][i] = letra
                                juego["puntaje"] += 10
                    else:
                        sonido_fallo.play()
                        juego["intentos"] -= 1
            
            if boton_reiniciar.collidepoint(mx, my):
                juego = iniciar_juego()
        
        elif not juego["jugando"] and evento.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if boton_reiniciar.collidepoint(mx, my):
                juego = iniciar_juego()
    
    # Mostrar palabra
    palabra_mostrada = " ".join(juego["palabra_guiones"])
    texto_palabra = fuente_letra.render(palabra_mostrada, True, BLANCO)
    pantalla.blit(texto_palabra, (ANCHO//2 - texto_palabra.get_width()//2, 350))
    
    # Dibujar letras
    for letra, rect in letras_rects:
        if letra in juego["letras_adivinadas"]:
            color = VERDE if letra in juego["palabra"] else ROJO
        else:
            color = BLANCO
        pygame.draw.rect(pantalla, NEGRO, rect)
        pygame.draw.rect(pantalla, color, rect, 2)
        texto = fuente_letra.render(letra, True, color)
        pantalla.blit(texto, (rect.x+5, rect.y+5))
    
    # Dibujar ahorcado
    dibujar_ahorcado(juego["intentos"])
    
    # Partículas
    actualizar_particulas()
    
    # Botón reiniciar
    pygame.draw.rect(pantalla, AZUL, boton_reiniciar)
    texto_reiniciar = fuente_letra.render("Reiniciar", True, BLANCO)
    pantalla.blit(texto_reiniciar, (boton_reiniciar.x+10, boton_reiniciar.y+10))
    
    # Cronómetro
    tiempo_transcurrido = int(time.time() - juego["inicio_tiempo"])
    texto_tiempo = fuente_puntaje.render(f"Tiempo: {tiempo_transcurrido}s", True, BLANCO)
    pantalla.blit(texto_tiempo, (600, 20))
    
    # Puntaje
    texto_puntaje = fuente_puntaje.render(f"Puntaje: {juego['puntaje']}", True, BLANCO)
    pantalla.blit(texto_puntaje, (50, 20))
    
    # Mensaje de fin
    if "_" not in juego["palabra_guiones"]:
        mensaje = fuente_mensaje.render("¡Ganaste!", True, VERDE)
        pantalla.blit(mensaje, (ANCHO//2 - mensaje.get_width()//2, 50))
        juego["jugando"] = False
    elif juego["intentos"] <= 0:
        mensaje = fuente_mensaje.render(f"Perdiste! Palabra: {juego['palabra']}", True, ROJO)
        pantalla.blit(mensaje, (ANCHO//2 - mensaje.get_width()//2, 50))
        juego["jugando"] = False

    pygame.display.flip()
    reloj.tick(60)
