import pygame as pg
import random

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ALTURA_PANTALLA = 600
ANCHO_PANTALLA = 800


#Definimos la primera clase --> Asteroide
class Meteor(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Ast75.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()  # Variable para poder posicionar al sprite

    def update(self):
        self.rect.y += 1

        if self.rect.y > ALTURA_PANTALLA:
            self.rect.y = -10
            self.rect.x = random.randrange(ANCHO_PANTALLA)


#Definimos la clase Player, que es la nave
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Nave_95.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect() 

class Game(object):
    def __init__(self):
        self.score = 0

        self.meteor_list = pg.sprite.Group()
        self.all_sprites_list = pg.sprite.Group()

        for i in range(50): # Creamos 50 asteroides
            meteor = Meteor()
            meteor.rect.x = random.randrange(800)
            meteor.rect.y = random.randrange(600)

            self.meteor_list.add(meteor)
            self.all_sprites_list.add(meteor)


        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True
        
        return False

    def run_logic(self):
        self.all_sprites_list.update()

        meteor_hit_list = pg.sprites.spritecollide(self.player, self.meteor_list, True)

        for meteor in meteor_hit_list:
            self.scrore += 1
            print(self.score)

    def display_frame(self, screen):
        screen.fill(BLANCO)
        self.all_sprites_list.draw(screen)
        pg.display.flip()


def main():
    pg.init()

    screen = pg.display.set_mode([ANCHO_PANTALLA, ALTURA_PANTALLA])

    done = False
    clock = pg.time.Clock()

    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pg.quit()
    

if __name__ == "__main__":
    main()