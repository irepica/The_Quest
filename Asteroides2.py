import pygame as pg
import random



BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)



#Definimos la primera clase --> Asteroide
class Meteor(pg.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.speed_x = random.randint(-5,-1)

        randAst = random.randint(1,3)
        if randAst == 1:        
            self.image = pg.image.load("Ast75.png").convert() # self.image es el nombre de la variable asteroide
        elif randAst == 2:
            self.image = pg.image.load("Ast50.png").convert() # self.image es el nombre de la variable asteroide
        elif randAst == 3:
            self.image = pg.image.load("Ast25.png").convert() # self.image es el nombre de la variable asteroide

        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()  # Variable para poder posicionar al sprite
    
    def update(self):
        self.rect.x += self.speed_x



#Definimos la clase Player, que es la nave
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Nave_95.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect() 
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 300   #posicion inicial de la nave, centrada en altura

    def changespeed(self, x):  
        self.speed_x += x
        
    def update(self):
        self.rect.y += self.speed_x
        player.rect.x = 10
    
    def resetSpeed(self):
        self.speed_x = 0
        

    #def update(self):
        #pass


def menuInicio():
    iniciar = False  
    #window.fill(black)
    #myfont=pg.font.SysFont("Britannic Bold", 40)
    
    #nlabel=myfont.render("Welcome Start Screen", 1, (255, 0, 0))    #texto

    fuente = pg.font.SysFont("Arial", 15)   # fuente para el texto que aparece en pantalla
    background = pg.image.load("Fondo_espacio.jpg").convert()
    screen.blit(background, [0, 0])
    
    texto = fuente.render("Bienvenido/a a The Quest", True, BLANCO)
    pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
    screen.blit(texto, [10, 10])

    texto = fuente.render("Coloniza nuevos planetas, esquivando un campo de asteroides.", True, BLANCO)
    screen.blit(texto, [10, 30])

    texto = fuente.render("Instrucciones del juego", True, BLANCO)
    screen.blit(texto, [10, 50])

    

    texto = fuente.render("Presiona una tecla para empezar la aventura!", True, BLANCO)
    screen.blit(texto, [10, 180])
    pg.display.flip()


    while (iniciar==False):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key==pg.K_SPACE:
                iniciar=True


pg.init()

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
clock = pg.time.Clock()
done = False
score = 0

fuente = pg.font.SysFont("Arial", 15)   # fuente para el texto que aparece en pantalla

num_fotogramas = 0
tasa_fotogramas = 60
instante_de_partida = 90
masMet = instante_de_partida - 3
menuInicio()

meteor_list = pg.sprite.Group()
all_sprite_list = pg.sprite.Group()



for i in range(10): # Creamos 50 asteroides
    meteor = Meteor()
    #meteor.rect.x = random.randrange(800)
    meteor.rect.x = 700 #TOdos empiezan en el margen derecho
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)


player = Player()
all_sprite_list.add(player)

background = pg.image.load("Fondo_espacio.jpg").convert()
screen.blit(background, [0, 0])

pg.key.set_repeat(5,100) # Para acelerar la nave al mantener pulsado el cursor

while not done: 
    #control tiempo
    screen.blit(background, [0, 0])
    segundos_totales = instante_de_partida - (num_fotogramas // tasa_fotogramas)

    if segundos_totales < 0:
        segundos_totales = 0

    # Dividimos por 60 para obtener los minutos totales:

    minutos = segundos_totales // 60

    segundos = segundos_totales % 60

    segundos5 = segundos_totales % 60

    # Usamos el formato de cadenas de texto para formatear los ceros del principio

    texto_salida = "Time: {0:02} : {1:02}".format(minutos, segundos)

    # Volcamos en la pantalla:
    texto = fuente.render(texto_salida, True, BLANCO)
    screen.blit(texto, [10, 20])

    num_fotogramas += 1

    # Limitamos a 20fps:
    #clock.tick(20)
    
    #Se añaden nuevos asteroides cada 3 segundos
    if segundos_totales < masMet:
       masMet -= 3
       for i in range(10): # Creamos 10 asteroides
            meteor = Meteor()
            #meteor.rect.x = random.randrange(800)
            meteor.rect.x = 700 #TOdos empiezan en el margen derecho
            meteor.rect.y = random.randrange(600)

            meteor_list.add(meteor)
            all_sprite_list.add(meteor) 
        
        
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

# EVENTOS TECLADO movimiento nave

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.changespeed(-2)
            elif event.key == pg.K_DOWN:
                player.changespeed(2)
    
        elif event.type == pg.KEYUP:
            player.resetSpeed() #parar la nave
      

    all_sprite_list.update()

    meteor_hit_list = pg.sprite.spritecollide(player, meteor_list, True)

    for meteor in meteor_hit_list:
        score += 1
        print(score)



    #screen.blit(background, [0, 0])

    all_sprite_list.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()