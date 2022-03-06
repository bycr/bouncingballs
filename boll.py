import pygame
import random
import threading

# medida_ventana
ancho = 800
alto = 600

# datos_circulo
radio = random.randint(1, 10)
fps = 60
verde = (0, 255, 0)
negro = (0, 0, 0)

cantidad = int(input("Ingrese la cantidad de circulos: "))


def circulos(dibujar_circulo):
    circulos = [{'x': random.randint(100, ancho), 'y': random.randint(100, alto),
                 'color': verde,
                 'velocidad_x': random.randint(-5, 5),
                 'velocidad_y': random.randint(-5, 5)}
                for _ in range(cantidad)]

    clock = pygame.time.Clock()

    while dibujar_circulo.is_set():
        ventana = pygame.Surface((ancho, alto))
        for circulo in circulos:
            pos_x = circulo["x"]
            pos_y = circulo["y"]
            color = circulo["color"]
            pos_x += circulo["velocidad_x"]
            pos_y += circulo["velocidad_y"]
            # if pos_y>alto:
            # pos_y=0
            if ((pos_x + radio) > ancho) or ((pos_x - radio) < -radio):
                circulo["velocidad_x"] *= -1
            if ((pos_y + radio) > alto) or ((pos_y - radio) < -radio):
                circulo["velocidad_y"] *= -1
            pygame.draw.circle(ventana, color, (pos_x, pos_y), radio)
            circulo["x"] = pos_x
            circulo["y"] = pos_y
        event = pygame.event.Event(pygame.USEREVENT + 1,
                                   {"bitmap": ventana})

        pygame.event.post(event)
        clock.tick_busy_loop(fps)


def main():
    pygame.init()
    pygame.display.set_caption("Circulos")
    ventana = pygame.display.set_mode((ancho, alto), pygame.HWSURFACE or pygame.DOUBLEBUF)
    evento_dibujar_cuadro = threading.Event()
    evento_dibujar_cuadro.set()
    hilo = threading.Thread(target=circulos, args=(evento_dibujar_cuadro,), daemon=True)
    hilo.start()

    ventana_circulos = None
    clock = pygame.time.Clock()

    # bucle
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.USEREVENT + 1:
                ventana_circulos = event.bitmap
        if ventana_circulos is not None:
            ventana.blit(ventana_circulos, (0, 0))

        pygame.display.flip()
        clock.tick_busy_loop(fps)

    evento_dibujar_cuadro.clear()

    pygame.quit()


if __name__ == "__main__":
    main()