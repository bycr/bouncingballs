from random import randrange
from typing import Dict, Tuple

import choice

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
random_value = randrange(len(mycolors))
contador = 0

print(mycolors.get(1))

for i in mycolors.values():
    if contador == random_value:
        print(i)
    contador = contador +1

