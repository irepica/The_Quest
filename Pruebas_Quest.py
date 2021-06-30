

import pygame as pg

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")

clock = pg.time.Clock()

done = False

background = pg.image.load("fondo_nebulosa.jpeg").convert()
player = pg.image.load("nave.png").convert()  # introducimos la nave en la pantalla
player.set_colorkey([255, 255, 255])  # Con este código eliminamos el color blanco de fondo de la nave

while not done: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
# Para poder moverlo con el mouse, hemos de obtener las coordenadas del mouse

    mouse_pos = pg.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]



    screen.blit(background, [0, 0])
    screen.blit(player, [x, y])


    pg.display.flip()
    clock.tick(60)

pg.quit()


