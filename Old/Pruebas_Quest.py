
import pygame as pg
import random

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


#Definimos la primera clase --> Asteroide
class Meteor(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Ast75.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()  # Variable para poder posicionar al sprite

#Definimos la clase Player, que es la nave
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Nave_95.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect() 


pg.init()

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
clock = pg.time.Clock()
done = False
score = 0


meteor_list = pg.sprite.Group()
all_sprite_list = pg.sprite.Group()

for i in range(50): # Creamos 50 asteroides
    meteor = Meteor()
    meteor.rect.x = random.randrange(800)
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)


player = Player()
all_sprite_list.add(player)

background = pg.image.load("Fondo_espacio.jpg").convert()

while not done: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    #Para mover la nave con el ratón
    pg.mouse.set_visible(0)
    mouse_pos = pg.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]

    # Para crear el movimiento de derecha a izqda de los asteroides
    for meteor in meteor_list:
        meteor.rect.x += -1

    meteor_hit_list = pg.sprite.spritecollide(player, meteor_list, True)

    for meteor in meteor_hit_list:
        score += 1
        print(score)


    screen.blit(background, [0, 0])

    all_sprite_list.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()
