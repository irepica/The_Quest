import pygame as pg
import random
import sqlite3
from datetime import datetime


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)



#Definimos la primera clase --> Asteroide
class Meteor(pg.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.speed_x = random.randint(-10,-1)

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
        self.angle = 0
        self.change_angle = 0

    def changespeed(self, y):  
        self.speed_y += y
        
    def update(self):
          
        if self.speed_y > 0:
            if (self.rect.y + self.speed_y) <= 550:
                self.rect.y += self.speed_y
            else:
                self.rect.y = 550

        if self.speed_y < 0:
            if (self.rect.y + self.speed_y) >= 5:
                self.rect.y += self.speed_y
            else:
                self.rect.y = 5
               
        player.rect.x = 10

    def resetSpeed(self):
        self.speed_y = 0
    
    def borrar (self):
        self.kill()
 
     
    

class Explosion(pg.sprite.Sprite):
    def __init__(self,center):
        
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Explosion120.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect() 
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        self.frame += 1
        if self.frame == 5:
            self.kill()


#Definimos la clase Planeta fin de nivel
class Planeta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Planeta2.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect() 
        self.speed_x = -3
        self.speed_y = 0
        self.rect.x = 800
        self.rect.y = 0   #posicion inicial de la nave, centrada en altura

    def changespeed(self, y):  
        self.speed_y += y
        
    def update(self):
        if self.rect.x >600:  
                self.rect.x += self.speed_x

    def resetSpeed(self):
        self.speed_y = 0
      



def menuInicio(baseD):
    iniciarMenu = False  
    #window.fill(black)
    #myfont=pg.font.SysFont("Britannic Bold", 40)
    
    #nlabel=myfont.render("Welcome Start Screen", 1, (255, 0, 0))    #texto

    fuente = pg.font.SysFont("Arial", 15)   # fuente para el texto que aparece en pantalla
    background = pg.image.load("Fondo_espacio.jpg").convert()
    screen.blit(background, [0, 0])
    
    texto = fuente.render("Bienvenido/a a The Quest", True, BLANCO)
    pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
    screen.blit(texto, [10, 50])

    texto = fuente.render("Coloniza nuevos planetas, esquivando un campo de asteroides", True, BLANCO)
    screen.blit(texto, [10, 80])

    texto = fuente.render("Instrucciones del juego", True, BLANCO)
    screen.blit(texto, [10, 450])

    texto = fuente.render("Esquiva a los asteroides y aterriza en el nuevo mundo.", True, BLANCO)
    screen.blit(texto, [10, 480])

    texto = fuente.render("Para ello, pulsa los cursores superior e inferior, y que la habilidad te acompañe", True, BLANCO)
    screen.blit(texto, [10, 500])

    texto = fuente.render("Dispones de 3 vidas para ello!", True, BLANCO)
    screen.blit(texto, [10, 110])

    texto = fuente.render("Presiona la tecla 'espacio' y empieza la aventura!", True, BLANCO)
    screen.blit(texto, [400, 550])
    
    #SQL
    baseD.execute("select * from tablaPuntos") #recuperar lista ordenada por los puntos
    listaBD = baseD.fetchall()
    print(listaBD)
     
  

    texto = fuente.render("RECORDS", True, BLANCO)
    
    fila = 50
    screen.blit(texto, [500, fila])
    for row in listaBD:
        fila +=20
        print(row[0])
        print(row[1])
        texto = fuente.render("FECHA: " + row[0] + " Puntos: " + str(row[1]) , True, BLANCO)
        screen.blit(texto, [500, fila])


    pg.display.flip()


    


    while (iniciarMenu == False):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                iniciarMenu = True
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key==pg.K_SPACE:
                iniciarMenu = True


pg.init()

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
clock = pg.time.Clock()
done = False
score = 0

#vidas = 3

inicio = True

#nivel = 1

fuente = pg.font.SysFont("Arial", 15)   # fuente para el texto que aparece en pantalla

num_fotogramas = 0
tasa_fotogramas = 30
#instante_de_partida = 90
#masMet = instante_de_partida - 3

#puntos = 0

#meteor_list = pg.sprite.Group()
#all_sprite_list = pg.sprite.Group()

##SQLITE
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table tablaPuntos (nombre, puntos)")
# This is the qmark style:
#cur.execute("insert into tablaPuntos values (?, ?)", ("C", 1972))

#cur.execute("insert into tablaPuntos values ("Pepe", 20)")

# And this is the named style:


sound = pg.mixer.Sound("explota.wav") #Variable para añadir sonido de explosión

background = pg.image.load("Fondo_espacio.jpg").convert()
screen.blit(background, [0, 0])

pg.key.set_repeat(5,100) # Para acelerar la nave al mantener pulsado el cursor

while not done: 
    
    #Llamada a menu inicio
    while inicio == True:
        menuInicio(cur)
        inicio = False
        #Inicio variables
        puntos = 0
        instante_de_partida = 10
        masMet = instante_de_partida - 3 #Cada cuanto se generan mas meteoritos (segundos)
        meteor_list = pg.sprite.Group()
        all_sprite_list = pg.sprite.Group()
        vidas = 3
        nivel = 1
        finNivel = False
        cronometro = 0
        mostPlaneta = 0
        muerto = False
        numMeteoritos = 2
        reiniciar = False
        victoria = False
        
        for i in range(2): # Creamos 2 asteroides
            meteor = Meteor()
            #meteor.rect.x = random.randrange(800)
            meteor.rect.x = 700 #TOdos empiezan en el margen derecho
            meteor.rect.y = random.randint(50,580)
            meteor_list.add(meteor)
            all_sprite_list.add(meteor)
        player = Player()
        all_sprite_list.add(player)


    #control tiempo
    screen.blit(background, [0, 0])
    
    if finNivel == False and mostPlaneta == False and muerto == False:
        #segundos_totales = instante_de_partida - (num_fotogramas // tasa_fotogramas)
        segundos_totales = instante_de_partida - (cronometro // tasa_fotogramas)
        cronometro += 1
        if segundos_totales <0:
            segundos_totales = 0
           
        if segundos_totales == 0:
            mostPlaneta = True
            finNivel = True
            plan = Planeta()
            all_sprite_list.add(plan)
            cronometro = 0
            #Programar FIN DE PARTIDA!!!
            #if nivel < 3:
             #   nivel += 1
                #instante_de_partida += 10
                #masMet = instante_de_partida -3
            #else:
                #Fin de partida
            #Texto fin de nivel
 
    if finNivel == True and mostPlaneta == True:
        if mostPlaneta == True:
            cronometro += 1
            tiempoEspera = 3* tasa_fotogramas
            if cronometro >= tiempoEspera:
                mostPlaneta = False
    
    if finNivel == True and mostPlaneta == False:
        if nivel <3:
            texto_salida = 'Nivel ' + str(nivel) + ' Finalizado!! PRESIONA ESPACIO PARA CONTINUAR' 
            texto = fuente.render(texto_salida, True, BLANCO)
            screen.blit(texto, [150,200])   
        else:
            texto_salida = 'Enhorabuena!! Has conseguido ' + str(puntos) + ' puntos!! PRESIONA ENTER PARA CONTINUAR' 
            texto = fuente.render(texto_salida, True, BLANCO)
            screen.blit(texto, [150,300])
            victoria = True   

    
  
    
      

    # Dividimos por 60 para obtener los minutos totales:
    if muerto == False:
        minutos = segundos_totales // 60

        segundos = segundos_totales % 60

        segundos5 = segundos_totales % 60

    # Usamos el formato de cadenas de texto para formatear los ceros del principio

    texto_salida = "Time: {0:02} : {1:02}".format(minutos, segundos)

    # Volcamos en la pantalla:
    texto = fuente.render(texto_salida, True, BLANCO)
    screen.blit(texto, [400,10])

    num_fotogramas += 1

    
    #Se añaden nuevos asteroides cada 3 segundos
    if segundos_totales < masMet and finNivel == False:
        masMet -= 3
        puntos +=10 + (3*nivel)
        for i in range(numMeteoritos): # Creamos 2 asteroides
            meteor = Meteor()
            #meteor.rect.x = random.randrange(800)
            meteor.rect.x = 700 #TOdos empiezan en el margen derecho
            meteor.rect.y = random.randint(50,580)

            meteor_list.add(meteor)
            all_sprite_list.add(meteor) 
    
    
    #Pintar marcador
    texto_salida = '  Puntos ' + str(puntos) + '                   Nivel ' + str(nivel)
    texto = fuente.render(texto_salida, True, BLANCO)
    screen.blit(texto, [20,10])   
    
    if finNivel == False:
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
    else:
        player.resetSpeed()
      

    all_sprite_list.update()
    if finNivel == False:
        meteor_hit_list = pg.sprite.spritecollide(player, meteor_list, True)

        for meteor in meteor_hit_list:
            score += 1
            print(score)
            vidas -= 1
            sound.play()
            expl = Explosion(player.rect.center)
            all_sprite_list.add(expl)

        if vidas == 3:
            naveVidas = pg.image.load("Nave_vidas.png").convert()
            naveVidas.set_colorkey(NEGRO)
            screen.blit(naveVidas, [500, 0])
            screen.blit(naveVidas, [530, 0])
            screen.blit(naveVidas, [560, 0])
        
        elif vidas == 2:
            naveVidas = pg.image.load("Nave_vidas.png").convert()
            naveVidas.set_colorkey(NEGRO)
            screen.blit(naveVidas, [500, 0])
            screen.blit(naveVidas, [530, 0])
        
        elif vidas == 1:
            naveVidas = pg.image.load("Nave_vidas.png").convert()
            naveVidas.set_colorkey(NEGRO)
            screen.blit(naveVidas, [500, 0])
        elif vidas == 0:
            muerto = True
    
    if muerto == True:
        texto_salida = 'GAME OVER PRESIONE ENTER PARA CONTINUAR' 
        texto = fuente.render(texto_salida, True, BLANCO)
        screen.blit(texto, [150,200])

    all_sprite_list.draw(screen)
    pg.display.flip()
    clock.tick(tasa_fotogramas)
 
    
    if muerto == True or victoria == True:
        reiniciar = True
       
    if reiniciar == True:
         #APRETEMOS ESPACIO PARA CONTINUAR
        while (reiniciar == True):
             for event in pg.event.get():
                if event.type == pg.QUIT:
                    reiniciar = False 
                # EVENTOS TECLADO movimiento nave
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        reiniciar = False
                        inicio = True
                        all_sprite_list.empty()
                        
                        #guardar puntuacion
                        now=datetime.now()
                        date_timeSQL = now.strftime("%d/%m/%Y , %H:%M:%S")
                        cur.execute("insert into tablaPuntos values (?, ?)", (date_timeSQL,puntos))
                        print(date_timeSQL)
                        cur.execute("select * from tablaPuntos") #recuperar lista ordenada por los puntos
                        print(cur.fetchall())   


    if finNivel == True and mostPlaneta == False and muerto == False and victoria == False:
         #APRETEMOS ESPACIO PARA CONTINUAR
        while (finNivel == True):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finNivel = False 
                # EVENTOS TECLADO movimiento nave
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        instante_de_partida = 10
                        cronometro = 0
                        masMet = instante_de_partida - 3 #Cada cuanto se generan mas meteoritos (segundos)
                        all_sprite_list.empty()   
                        nivel += 1
                        finNivel = False
                        numMeteoritos += 3
                        
                        for i in range(numMeteoritos): # Creamos 2 asteroides
                            meteor = Meteor()
                            #meteor.rect.x = random.randrange(800)
                            meteor.rect.x = 700 #TOdos empiezan en el margen derecho
                            meteor.rect.y = random.randrange(600)
                            meteor_list.add(meteor)
                            all_sprite_list.add(meteor)    
                                
                        player = Player()
                        all_sprite_list.add(player)

pg.quit()
