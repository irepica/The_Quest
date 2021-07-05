import pygame as pg 
#import pygame.font


HELP_MESSAGE = "Sobrevive a una peligrosa tormenta de asteroides, desplazándote con el cursor, arriba y abajo"

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

pg.init()
#pg.font.init()


screen = pg.display.set_mode([800, 600])
pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
clock = pg.time.Clock()  # reloj que gestiona la actualización de la pantalla.
done = False

fuente = pg.font.SysFont("Arial", 15)   # fuente para el texto que aparece en pantalla

num_fotogramas = 0
tasa_fotogramas = 20
instante_de_partida = 90

while not done: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    background = pg.image.load("Fondo_espacio.jpg").convert()
    screen.blit(background, [0, 0])


    #El temporizador avanza

    #segundos_totales = num_fotogramas // tasa_fotogramas
    
    #minutos = segundos_totales // 60

    #segundos = segundos_totales % 60

    # Usamos el formato de cadenas de texto para formatear los ceros del principio

    #texto_salida = "Time: {0:02} : {1:02}".format(minutos, segundos)

    # Volcamos en la pantalla:
    #texto = fuente.render(texto_salida, True, BLANCO)
    #screen.blit(texto, [0, 20])

    # El temporizador retrocede
    # El temporizador avanza

    # Calculamos los segundos totales
    segundos_totales = instante_de_partida - (num_fotogramas // tasa_fotogramas)

    if segundos_totales < 0:
        segundos_totales = 0

    # Dividimos por 60 para obtener los minutos totales:

    minutos = segundos_totales // 60

    segundos = segundos_totales % 60

    # Usamos el formato de cadenas de texto para formatear los ceros del principio

    texto_salida = "Time: {0:02} : {1:02}".format(minutos, segundos)

    # Volcamos en la pantalla:
    texto = fuente.render(texto_salida, True, BLANCO)
    screen.blit(texto, [10, 20])

    num_fotogramas += 1

    # Limitamos a 20fps:
    clock.tick(20)

    pg.display.flip()

pg.quit()

