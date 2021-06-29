import pygame as pg

screen = pg.display.set_mode([800, 600])
clock = pg.time.Clock()

done = False

background = pg.image.load("fondo_nebulosa.jpeg").convert()

while not done: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    screen.blit(background, [0, 0])

    pg.display.flip()
    clock.tick(60)

pg.quit()