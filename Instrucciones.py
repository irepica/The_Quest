
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