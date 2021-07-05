
# Creamos las instrucciones que aparecerán tras pulsar una tecla. 

# El juego consiste en esquivar el mayor número de asteroides durante el máximo tiempo posible. 
# La nave sólo se moverá verticalmente, pulsando los cursores superior e inferior. 
# Si alguno de los asteroides choca con la nave, ésta se destruirá y consumirá una vida. 

import pygame as pg 
#import pygame.font


HELP_MESSAGE = "Sobrevive a una peligrosa tormenta de asteroides, desplazándote con el cursor, arriba y abajo"

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

pg.init()
#pg.font.init()



screen = pg.display.set_mode([800, 600])
pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
clock = pg.time.Clock()  # reloj que gestiona la actualización de la pantalla.
done = False

fuente = pg.font.SysFont("Arial", 15)   # fuente para el texto que aparece en pantalla

mostrar_instrucciones = True
pagina_de_instrucciones = 1


background = pg.image.load("Fondo_espacio.jpg").convert()
screen.blit(background, [0, 0])

# Genero el bucle de la página de instrucciones

while not done and mostrar_instrucciones:
    for event in pg.event.get(): 
        if event.type == pg.QUIT: # el usuario clica en cerrar
            done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            pagina_de_instrucciones += 1
            if pagina_de_instrucciones == 3:
                mostrar_instrucciones = False


   
    # Limpia la pantalla y establece el color de fondo:
    #screen.fill(NEGRO)
    

    if pagina_de_instrucciones == 1:
        # Instrucciones de dibujo, página 1
        # 

        texto = fuente.render("Bienvenido/a a The Quest", True, BLANCO)
        pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
        screen.blit(texto, [10, 10])

        texto = fuente.render("Coloniza nuevos planetas, esquivando un campo de asteroides.", True, BLANCO)
        screen.blit(texto, [10, 30])

        texto = fuente.render("Instrucciones del juego", True, BLANCO)
        screen.blit(texto, [10, 50])

        texto = fuente.render("El juego consiste en esquivar el mayor número de asteroides durante el máximo tiempo posible.", True, BLANCO)
        screen.blit(texto, [10, 80])

        texto = fuente.render("La nave sólo se moverá verticalmente, pulsando los cursores superior e inferior.", True, BLANCO)
        screen.blit(texto, [10, 100])

        texto = fuente.render("Si alguno de los asteroides choca con la nave, ésta se destruirá y consumirá una vida.", True, BLANCO)
        screen.blit(texto, [10, 150])

        texto = fuente.render("¡Presiona una tecla para empezar la aventura!", True, BLANCO)
        screen.blit(texto, [10, 180])



    #if pagina_de_instrucciones == 2:
        # Instrucciones de dibujo, página2

     #   texto = fuente.render("Instrucciones del juego", True, BLANCO)
      #  screen.blit(texto, [10, 10])

       # texto = fuente.render("El juego consiste en esquivar el mayor número de asteroides durante el máximo tiempo posible.", True, BLANCO)
        #screen.blit(texto, [10, 50])

        #texto = fuente.render("La nave sólo se moverá verticalmente, pulsando los cursores superior e inferior.", True, BLANCO)
        #screen.blit(texto, [10, 100])


        #texto = fuente.render("Si alguno de los asteroides choca con la nave, ésta se destruirá y consumirá una vida.", True, BLANCO)
        #screen.blit(texto, [10, 150])


        #texto = fuente.render("Página 2", True, BLANCO)
        #screen.blit(texto, [10, 200])

    # Limito a 20 fps:
    clock.tick(20)

    #Actualizo la pantalla con lo realizado:
    pg.display.flip()



pq.quit()