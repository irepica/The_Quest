
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

#######################################


if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.changespeed(-3)
            if event.key == pg.K_RIGHT:
                player.changespeed(3)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.changespeed(3)
            if event.key == pg.K_RIGHT:
                player.changespeed(-3)



##########################################


# Creamos las instrucciones que aparecerán tras pulsar una tecla. 

# El juego consiste en esquivar el mayor número de asteroides durante el máximo tiempo posible. 
# La nave sólo se moverá verticalmente, pulsando los cursores superior e inferior. 
# Si alguno de los asteroides choca con la nave, ésta se destruirá y consumirá una vida. 

import pygame as pg 


HELP_MESSAGE = "Sobrevive a una peligrosa tormenta de asteroides, desplazándote con el cursor, arriba y abajo"


class Help(pg.escena.Base):
    "Pantalla con las instrucciones del juego."

    def__init__(self)
        pg.escena.Base.__init__(self)

    def iniciar(self)
        pg.fondos.Fondo("The_Quest/fondo_estrellado.jpeg")
        self.crear_texto_ayuda()
        self.pulsa_tecla_escape_conectar(self.cuando_pulsa_tecla)
    
    def crear_texto_ayuda(self):
        pg.actores.Texto("Help", y=200)
        pg.actores.Texto(HELP_MESSAGE, y=150)
        pg.avisar("Pulsa ESC para volver")
    
    def cuando_pulsa_tecla(self, *k, **kw):
        import Pag_inicio
        pg.cambiar_escena(Pag_inicio.)




##########################################################