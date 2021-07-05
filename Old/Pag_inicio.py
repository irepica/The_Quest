

import pygame as pg 

pg.init()
pantalla = pg.display.set_mode((800, 600))
pg.display.set_caption("Hola")

game_over = False

while not game_over:
    #Gestión de eventos
    for evento in pg.event.get():
        pass

    # Gestión del estado
    print('Hola mundo')

    # Refrescar pantalla
    pantalla.fill((0, 255, 0))
    pg.display.flip()

 