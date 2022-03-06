import random
import threading
import time
from collections import namedtuple

import pygame

mycolors = {
    #9 elemetos
    1: (0, 0, 0), #"Negro"
    2: (255, 255, 255), #"Blanco"
    3: (197, 197, 197), #"Gris"
    4: (255, 255, 128), #"Amarillo"
    5: (128, 255, 128), #"Verde"
    6: (128, 0, 128), #"Purpura"
    7: (0, 0, 255), #"Azul"
    8: (255, 0, 0), #"Rojo"
    9: (255, 170, 255) #"Rosa"
}

Colour = namedtuple("Colour", ["red", "green", "blue"])

color_fondo = Colour(red=36, green=188, blue=168)
color_bola = Colour(red=0, green=0, blue=0)
radio = random.randint(10, 20)
ancho = 640
alto = 480

numero_bolas = random.randint(2, 10)
fps = 60

verde = (0, 0, 0)

def circulos(dibuja_circulo):
    random_value = random.randrange(len(mycolors))
    contador = 0
    for i in mycolors.values():
        if contador == random_value:
            print(i)
        contador = contador + 1
    circulos = [{'posx': random.randint(100, ancho), 'posy': random.randint(100, alto),
                 'color': i,
                 'velocidadx': random.randint(-5, 5),
                 'velocidady': random.randint(-5, 5),
                 'espesor': random.randint(0,10)}
                for _ in range(numero_bolas)]
    clock = pygame.time.Clock()

    while dibuja_circulo.is_set():
        pantalla = pygame.Surface((ancho, alto))
        random_value = random.randrange(len(mycolors))
        contador = 0
        for colo in mycolors.values():
            if contador == random_value and contador != 2:
                print(colo)
                pantalla.fill(colo)
                #time.sleep(0.5)
            contador = contador + 1
        #pantalla.fill(color_fondo)
        for circulo in circulos:
            posx = circulo["posx"]
            posy = circulo["posy"]
            color = circulo["color"]
            posx += circulo["velocidadx"]
            posy += circulo["velocidady"]
            espesor = circulo["espesor"]
            if ((posx + radio) > ancho) or ((posx - radio) < -radio):
                circulo["velocidadx"] *= -1
            if ((posy + radio) > alto) or ((posy - radio) < -radio):
                circulo["velocidady"] *= -1
            pygame.draw.circle(pantalla, color, (posx, posy), radio,espesor )
            circulo["posx"] = posx
            circulo["posy"] = posy
        event = pygame.event.Event(pygame.USEREVENT + 1,
                                   {"bitmap": pantalla})
        pygame.event.post(event)
        clock.tick_busy_loop(fps)


def main():
    pygame.init()
    pygame.display.set_caption("Pelota rebota")
    pantalla = pygame.display.set_mode((ancho, alto), pygame.HWSURFACE or pygame.DOUBLEBUF)
    evento_dibujar_cuadro = threading.Event()
    evento_dibujar_cuadro.set()
    hilo = threading.Thread(target=circulos, args=(evento_dibujar_cuadro,), daemon=True)
    hilo.start()

    ventana_circulos = None
    clock = pygame.time.Clock()

    ACTIVO = True
    while ACTIVO:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ACTIVO = False
            elif event.type == pygame.USEREVENT + 1:
                ventana_circulos = event.bitmap
        if ventana_circulos is not None:
            pantalla.blit(ventana_circulos, (0, 0))

        pygame.display.flip()
        clock.tick_busy_loop(fps)

    evento_dibujar_cuadro.clear()

    pygame.quit()


if __name__ == "__main__":
    main()





