
import sys
import pygame as pg 

def run_game():

    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("The Quest, Tormenta de asteroides")


    # Definimos el color de fondo de la pantalla

    background_color = (240, 250, 230)

    # Creamos el bucle
    while True:
        # Supervisar teclado y movimiento del ratón
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        # fill color
        screen.fill(background_color)
        # visualizar la pantalla
        pg.display.flip()

run_game()

 
###########################
# EVENTOS TECLADO
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            pass
        if event.key == pg.K_RIGHT:
            pass
        if event.key == pg.K_UP:
            pass
        if event.key == pg.K_DOWN:
            pass
    
    if event.type == pg.KEYUP:
        if event.key == pg.K_LEFT:
            pass
        if event.key == pg.K_RIGHT:
            pass
          if event.key == pg.K_UP:
            pass
        if event.key == pg.K_DOWN:
            pass