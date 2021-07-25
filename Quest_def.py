import pygame as pg
import random
import sqlite3
import sys
import time
from sqlite3 import Error
from datetime import datetime

from pygame.constants import KEYDOWN, KEYUP


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE =(0, 255, 255)
DARKGREEN = (34, 139, 34)
GREY = (213, 216, 220)


SCREENWIDTH = 800
SCREENHEIGHT = 600


#Defino la primera clase --> Asteroide
class Meteor(pg.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.speed_x = random.randint(-10,-1)


        #Creo 3 asteroides de diferente tamaño

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



#Defino la clase Player, que es la nave
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Nave_95.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect() 
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 300   #posicion inicial de la nave, centrada en altura
        self.angle = 0
        self.change_angle = 0
        self.rotacionNave = 0
        self.imagenOriginal = self.image.copy()
        self.Aterrizar = False
        self.rect.x = 10

    def changespeed(self, y):  
        self.speed_y += y
            
    def update(self):
        #Mediante límites, controlo que la nave no desaparezca de la pantalla

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
               
        if self.Aterrizar == True:
            
            if self.rect.y >= 310: 
                self.speed_y= -7
            elif self.rect.y <= 290:
                self.speed_y= 7
            else:
                self.speed_y=0
                #self.rect.x += 20
            self.rect.x += 7
            
            '''
            if self.rect.x >510:
                self.speed_x=0
                self.Aterrizar = False
            '''
            


    def resetSpeed(self):
        if self.Aterrizar == False:
            self.speed_y = 0  # Paro la nave 
    
    def borrar (self):
        self.kill()

    def rotarNave (self, angle):
        #while (self.rotacionNave < 180):        
            #if self.rotacionNave < 180:
        #self.rotacionNave += 1
        #self.angle +=3
        self.angle = angle
        self.image = pg.transform.rotate(self.imagenOriginal , self.angle)
        #playerCopia = self.image.copy()
        x,y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        #self.surf = pg.transform.rotate(playerCopia, self.angle)
        #self.rect = self.surf.get_rect(center=self.rect.center)    
        

        ##playerCopia = pg.transform.rotate(playerCopia, self.rotacionNave)
            
        ##screen.blit(playerCopia, (self.rect.x, self.rect.y))
            
        #self.image = playerCopia
            #pg.display.update()  

    def aterrizar (self):
        self.Aterrizar = True
        if self.rect.x >=525:
            self.Aterrizar = False
            return True


 
     
    

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

    def update(self): # Para borrar el objeto de la explosión
        self.frame += 1
        if self.frame == 5:
            self.kill()


#Defino la clase Planeta fin de nivel
class Planeta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Planeta2.png").convert() # self.image es el nombre de la variable asteroide
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect() 
        self.speed_x = -6
        self.speed_y = 0
        self.rect.x = 800
        self.rect.y = 50   #posicion inicial de la nave, centrada en altura

    def changespeed(self, y):  
        self.speed_y += y
        
    def update(self):  # Para generar el movimiento del planeta
        if self.rect.x >600:  
                self.rect.x += self.speed_x

    def resetSpeed(self):
        self.speed_y = 0


# Defino la clase del nombre del jugador

class enterName:
    def getKeyPress(self):
        devuelve = 1
        while (devuelve == 1):
            for event in pg.event.get():
                if event.type == KEYUP:
                    if event.key >=32 and event.key <=126:
                    #return event.key
                        devuelve = 0
                        return event.unicode
                        
                #else:
                    #return False
                #    return ""
        return ""  
    def getCharacter(self):
        salir = False
        #while (salir == False):
            # Comprobación por si el jugador ha tecleado teclas tipo (Shift, Alt, Ctrl)
        keyinput = pg.key.get_pressed()

        character = "NULL"

            # Get all the "Events" that have ocurred
        pg.event.pump()
        keyPress = self.getKeyPress()
        pg.event.clear()

            # If the user presses a key on the keyboard, then get the character
            # Is the user presses the shift key while pressing another character then capitalise it
            #if keyPress >= 32 and keyPress <= 126:
            #if keyPress == 2:
            #    if keyinput[K_LSHIFT]:
            #       keyPress -= 32
        if keyPress != "":
            #character = chr(keyPress)
            character = keyPress
            salir = True
            keyPress=""

        return character
      



def menuInicio(baseD):
    iniciarMenu = False  
    
    #fuente = pg.font.SysFont("Arial", 15)   # fuente para el texto que aparece en pantalla
    fuente = pg.font.Font("fuentes/titulo.otf", 42)   # fuente para el texto que aparece en pantalla
    background = pg.image.load("nebula.jpeg").convert()
    screen.blit(background, [0, 0])
    
    texto = fuente.render("Bienvenido/a a The Quest", True, BLANCO)
    pg.display.set_caption("The Quest, Sobrevive a la Tormenta de Asteroides")
    screen.blit(texto, [25, 20])

    fuente = pg.font.Font("fuentes/texto.otf", 19)

    texto = fuente.render("Coloniza nuevos planetas, esquivando un campo de asteroides", True, BLANCO)
    screen.blit(texto, [10, 100])

    texto = fuente.render("Instrucciones del juego:", True, BLANCO)
    screen.blit(texto, [10, 410])

    texto = fuente.render("Esquiva a los asteroides y aterriza en el nuevo mundo", True, BLANCO)
    screen.blit(texto, [10, 440])

    texto = fuente.render("Pulsa los cursores superior e inferior, para mover la nave ", True, BLANCO)
    screen.blit(texto, [10, 465])

    texto = fuente.render("Dispones de 3 vidas para ello!", True, BLANCO)
    screen.blit(texto, [10, 140])

    texto = fuente.render("Presiona la tecla 'espacio' y empieza la aventura!", True, BLANCO)
    screen.blit(texto, [200, 550])
    
    
    pg.display.flip()

    while (iniciarMenu == False):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #iniciarMenu = True
                pg.QUIT
                sys.exit(0)
            elif event.type == pg.KEYDOWN and event.key==pg.K_SPACE:
                iniciarMenu = True


#Función para preguntar el nombre al jugador

def ask(question):
    current_string = ""
    #ask (question) -> answer
    intNombre = enterName()
    display_box(question + ": " + current_string)
    #while 1:
    for x in [1,1,1]:
        current_string += str(intNombre.getCharacter())
        # show the full string while typing
        display_box(question + ": " + current_string)
    pg.time.wait(1000)
    return current_string # this is the answer


# The display_box puts the name entry box on screen and updates while typing

def display_box(message):
    "Print a message in a box in the middle of the screen"
    left = (SCREENWIDTH / 2) - 156
    top = ( SCREENHEIGHT / 2) + 4 
    
    pg.draw.rect(screen, GREY, (left, top, 320, 200))
    fuente = pg.font.Font("fuentes/texto.otf", 12)
    screen.blit(fuente.render("¡Nuevo record conseguido!", True, NEGRO), 
                    (left + 80, top + 35))

    #screen.blit(fuente.render("'Por favor, introduce las iniciales de tu nombre", True, VERDE)
     #               (left + 80, TOP + 50))

    screen.blit(fuente.render("Pulsa ENTER para finalizar.", True, NEGRO),
                     (left + 51, top + 160))

    #pg.draw.rect(screen, NEGRO, (left + 39, top + 110, 240, 20))
    pg.draw.rect(screen, NEGRO, (left + 39, top + 110, 90, 20))
    pg.draw.rect(screen, BLANCO, (left + 38, top + 108, 90, 24), 1)

    if len(message) !=0:
        screen.blit(fuente.render(message, True, BLANCO), (left+42, top + 111))

    pg.display.flip()

def mostrarRecords(baseD, tipo):
    baseD.execute("select * from tablaPuntos") #recuperar lista ordenada por los puntos
    listaBD = baseD.fetchall()
    #print(listaBD)
    fuente = pg.font.Font("fuentes/texto.otf", 18) 
    texto = fuente.render("TABLA DE RECORDS", True, BLANCO)
    if tipo == "muerte":
        columna = 280
        fila = 400
    else:
        columna = 280
        fila = 5
    screen.blit(texto, [columna, fila])
    
    for row in listaBD:  # Muestro en la pantalla inicial los records acumulados en la base de datos
        fila +=20
        #print(row[0])
        #print(row[1])
        #texto = fuente.render("Jugador/a: " + row[1] +     " Puntos: " + str(row[2]) , True, BLANCO)
        texto = fuente.render(row[1] + "  " + str(row[2]) , True, BLANCO)
        screen.blit(texto, [columna+50, fila])    

def nuevoRecord(baseD, puntos):
    baseD.execute("select count(*) from tablaPuntos")
    numFilas = int(baseD.fetchone()[0])

 
    if numFilas > 0:
        baseD.execute("select puntos from tablaPuntos order by puntos ") #recuperar lista ordenada por los puntos
        minPuntos = baseD.fetchone()[0]
        baseD.execute("select id from tablaPuntos order by puntos ") #recuperar lista ordenada por los puntos
        idBorrar = baseD.fetchone()[0]
        QUERYBORRAR = "delete from tablaPuntos where id =" + str(idBorrar)
             
    if numFilas < 3:
        nombre=ask("nombre")
        baseD.execute("insert into tablaPuntos values (?,?,?)", (numFilas+1,nombre,puntos))
        
    elif minPuntos <= puntos:
        nombre=ask("nombre")
        baseD.execute(QUERYBORRAR)
        baseD.execute("insert into tablaPuntos values (?,?,?)", (idBorrar,nombre,puntos))
        
def fondoJuego():
    background = pg.image.load("Fondo_espacio.jpg").convert()
    screen.blit(background, [0, 0])




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

#############################################
##SQLITE
#########################################

con = sqlite3.connect("mydatabase.db")
cur = con.cursor()
cur.execute("create table if not exists tablaPuntos (id, nombre, puntos)")


sound = pg.mixer.Sound("explota.wav") #Variable para añadir sonido de explosión

#background = pg.image.load("Fondo_espacio.jpg").convert()
#screen.blit(background, [0, 0])

pg.key.set_repeat(5,100) # Para acelerar la nave al mantener pulsado el cursor

nombre = ""

while not done:
        
    #Llamada a menu inicio
    while inicio == True:
        background = pg.image.load("nebula.jpeg").convert()
        screen.blit(background, [0, 0])
        menuInicio(cur)
        
        #Inicio variables
        inicio = False
        juego = True
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
        naveRotando = False
        contarGiro = 0
        aterrizar = False
        duraNivel=10
        segundos_totales = duraNivel
        pausaJuego = False
        inicioNivel = True
        faseFinal = False
       
        

    while juego == True:
        fondoJuego()
        fuente = pg.font.Font("fuentes/texto.otf", 18)
        if inicioNivel == True:
            for i in range(2): # Creamos 2 asteroides
                meteor = Meteor()
                #meteor.rect.x = random.randrange(800)
                meteor.rect.x = 700 #TOdos empiezan en el margen derecho
                meteor.rect.y = random.randint(50,580)
                meteor_list.add(meteor)
                all_sprite_list.add(meteor)
            inicioNivel = False
            player = Player()
            all_sprite_list.add(player)    
        
        
        
        #+meteoritos
        if segundos_totales < masMet and pausaJuego == False:
            masMet -= 3
            puntos +=10 + (3*nivel)
            for i in range(numMeteoritos): # Creamos 2 asteroides
                meteor = Meteor()
                #meteor.rect.x = random.randrange(800)
                meteor.rect.x = 700 #TOdos empiezan en el margen derecho
                meteor.rect.y = random.randint(50,580)

                meteor_list.add(meteor)
                all_sprite_list.add(meteor)

        # Dividimos por 60 para obtener los minutos totales:
        #if pausaJuego == False:
        minutos = segundos_totales // 60
        segundos = segundos_totales % 60
        segundos5 = segundos_totales % 60

        # Usamos el formato de cadenas de texto para formatear los ceros del principio
        texto_salida = "Time: {0:02} : {1:02}".format(minutos, segundos)

        # Volcamos en la pantalla:
        texto = fuente.render(texto_salida, True, BLANCO)
        screen.blit(texto, [300,10])
        num_fotogramas += 1 

        #Pintar marcador
        texto_salida = '  Puntos ' + str(puntos) + '      Nivel ' + str(nivel)
        texto = fuente.render(texto_salida, True, BLANCO)
        screen.blit(texto, [5,10])   
        
        #Movemos la nave durante al nivel
        if pausaJuego == False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

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
        
        #gestión de colisiones
        if pausaJuego == False:
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
            juego = False
            #compruebo records y pido inciales
            nuevoRecord(cur, puntos)
            con.commit()
            #mostrarRecords(cur)
        
        

        all_sprite_list.draw(screen)
        pg.display.flip()
        clock.tick(tasa_fotogramas)


        #Control fin de nivel, se para la nave, se muestra el planeta
        #if finNivel == False and mostPlaneta == False and muerto == False:
        if pausaJuego == False:
            #segundos_totales = instante_de_partida - (num_fotogramas // tasa_fotogramas)
            segundos_totales = instante_de_partida - (cronometro // tasa_fotogramas)
            cronometro += 1
            if segundos_totales <0:
                segundos_totales = 0
            
            if segundos_totales == 0:
                mostPlaneta = True
                pausaJuego = True
                naveRotando = True
                plan = Planeta()
                all_sprite_list.add(plan)
                cronometro = 0
              
   
        if mostPlaneta == True:
            cronometro += 1
            tiempoEspera = 3* tasa_fotogramas
            if cronometro >= tiempoEspera:
                mostPlaneta = False
                #naveRotando = True
    
    
    
        #if finNivel == True and mostPlaneta == False and naveRotando == True:
        if naveRotando == True:
            if contarGiro < 177:
                contarGiro +=3
                player.rotarNave(contarGiro)
            elif contarGiro >= 177:
                #naveRotando = False
                aterrizar = True
                
            #if aterrizar == True and player.aterrizar():
            if player.aterrizar():
                naveRotando = False
                aterrizar = False
                contarGiro = 0
                faseFinal = True
                naveRotando = False
            

    
        #if finNivel == True and mostPlaneta == False and naveRotando == False:
        if faseFinal == True:
            if nivel <3:
                finNivel = True
                pausaJuego = True
            else:
                victoria = True
                juego = False
                nuevoRecord(cur, puntos)
                con.commit()
            faseFInal = False

       
        if finNivel == True:    
            if nivel <3:
                texto_salida = 'Nivel ' + str(nivel) + ' Finalizado!! PRESIONA ESPACIO PARA CONTINUAR' 
                texto = fuente.render(texto_salida, True, BLANCO)
                screen.blit(texto, [150,150])
                pg.display.flip()
            #if finNivel == True and mostPlaneta == False and muerto == False and victoria == False and naveRotando == False:
        
            while (finNivel == True):
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        finNivel = False
                        pg.quit() 
                    # EVENTOS TECLADO movimiento nave
                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            instante_de_partida = duraNivel
                            cronometro = 0
                            masMet = instante_de_partida - 3 #Cada cuanto se generan mas meteoritos (segundos)
                            all_sprite_list.empty()   
                            nivel += 1
                            finNivel = False
                            numMeteoritos += 3
                            naveRotando = False
                            faseFinal = False
                            pausaJuego= False
                            inicioNivel = True

                            '''
                            for i in range(numMeteoritos): # Creamos 2 asteroides
                                meteor = Meteor()
                                #meteor.rect.x = random.randrange(800)
                                meteor.rect.x = 700 #TOdos empiezan en el margen derecho
                                meteor.rect.y = random.randrange(600)
                                meteor_list.add(meteor)
                                all_sprite_list.add(meteor)    
                                    
                            player = Player()
                            all_sprite_list.add(player)   
                            '''
    
    if victoria == True:
        background = pg.image.load("victoria.jpg").convert()
        screen.blit(background, [0, 0])
        pg.display.flip()
        #nuevoRecord(cur, puntos)
        #con.commit()
        mostrarRecords(cur, "victoria")
        fuente = pg.font.Font("fuentes/texto.otf", 18)
        fuente2 = pg.font.Font("fuentes/texto.otf", 24)
        texto_salida = '¡¡Enhorabuena!! ¡¡Has conseguido ' + str(puntos) + ' puntos!!  '
        texto = fuente2.render(texto_salida, True, BLANCO)
        screen.blit(texto, [50,90])

        texto_salida = 'PRESIONA ENTER PARA CONTINUAR'
        texto = fuente.render(texto_salida, True, BLANCO)
        screen.blit(texto, [170, 500])
        pg.display.flip()

        while victoria == True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    reiniciar = False
                    pg.quit() 
                # EVENTOS TECLADO movimiento nave
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        reiniciar = False
                        inicio = True
                        all_sprite_list.empty()
                        victoria = False
    
    #gestión cuando no hay más vidas
    if muerto == True:
        fuente = pg.font.Font("fuentes/muerto.ttf", 72)
        fuente2 = pg.font.Font("fuentes/texto.otf", 20)
        fuente3 = pg.font.Font("fuentes/muerto.ttf", 48)
        background = pg.image.load("shipCrash.jpg").convert()
        screen.blit(background, [0, 0])
        pg.display.flip()
        #nuevoRecord(cur, puntos)
        #con.commit()
        mostrarRecords(cur, "muerte")
        texto_salida = 'GAME OVER'
        texto_salida_2 = 'PRESIONE ENTER PARA CONTINUAR' 
        texto = fuente.render(texto_salida, True, BLANCO)
        texto2 = fuente2.render(texto_salida_2, True, BLANCO)
        #screen.blit(texto, [120,285])
        #screen.blit(texto2, [120, 315])
        screen.blit(texto, [250,285])
        screen.blit(texto2, [170, 500])
        pg.display.flip()
        while muerto == True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    reiniciar = False
                    pg.quit() 
                # EVENTOS TECLADO movimiento nave
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        reiniciar = False
                        inicio = True
                        all_sprite_list.empty()
                        muerto = False

                

pg.quit()
