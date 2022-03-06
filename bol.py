import random

import pygame
from collections import namedtuple
from random import randint

Colour = namedtuple("Colour", ["red", "green", "blue"])

color_fondo = Colour(red=36, green=188, blue=168)
color_bola = Colour(red=255, green=253, blue=65)
radio = 20
ancho = 640
alto = 480

pygame.init()

pygame.display.set_caption("Pelota rebota")

clock = pygame.time.Clock()
pantalla = pygame.display.set_mode([ancho, alto])

numero_bolas = random.randint(2, 10)


def main():
    posicion_bola = [(random.randint(0, ancho) // 2), (random.randint(0, alto) // 2)]
    velocidad_bola = [randint(-5, 5), randint(-5, 5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pantalla.fill(color_fondo)
        pygame.draw.circle(pantalla, color_bola, posicion_bola, radio, 0)
        pygame.display.update()

        # Compruebe si hay colisiones izquierda y derecha
        if posicion_bola[0] - radio < 0:
            velocidad_bola[0] = -velocidad_bola[0]
        elif posicion_bola[0] + radio > pantalla.get_width():
            velocidad_bola[0] = -velocidad_bola[0]

        # Compruebe si hay colisiones superiores e inferiores
        if posicion_bola[1] - radio < 0:
            velocidad_bola[1] = -velocidad_bola[1]
        elif posicion_bola[1] + radio > pantalla.get_height():
            velocidad_bola[1] = -velocidad_bola[1]

        posicion_bola[0] += velocidad_bola[0]
        posicion_bola[1] += velocidad_bola[1]

        clock.tick(60)


main()





