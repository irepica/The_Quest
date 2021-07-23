import pygame as pg
import random
import sqlite3
from sqlite3 import Error
from datetime import datetime

from pygame.constants import KEYDOWN, KEYUP


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE =(0, 255, 255)
DARKGREEN = (34, 139, 34)

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
               
        player.rect.x = 10


    def resetSpeed(self):
        self.speed_y = 0  # Paro la nave 
    
    def borrar (self):
        self.kill()

    def rotarNave (self):
        #while (self.rotacionNave < 180):        
            #if self.rotacionNave < 180:
        #self.rotacionNave += 1
        self.angle +=3
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

    #def aterrizar(self):


 
     
    

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
        self.speed_x = -3
        self.speed_y = 0
        self.rect.x = 800
        self.rect.y = 0   #posicion inicial de la nave, centrada en altura

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
    for row in listaBD:  # Muestro en la pantalla inicial los records acumulados en la base de datos
        fila +=20
        print(row[0])
        print(row[1])
        texto = fuente.render("FECHA: " + row[1] + " Puntos: " + str(row[2]) , True, BLANCO)
        screen.blit(texto, [500, fila])

    pg.display.flip()

    while (iniciarMenu == False):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                iniciarMenu = True
                pg.quit()
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
    return current_string # this is the answer


# The display_box puts the name entry box on screen and updates while typing

def display_box(message):
    "Print a message in a box in the middle of the screen"
    left = (SCREENWIDTH / 2) - 156
    top = ( SCREENHEIGHT / 2) + 4 
    
    pg.draw.rect(screen, DARKGREEN, (left, top, 320, 200))
    screen.blit(fuente.render("New High Score!", True, VERDE), 
                    (left + 90, top + 35))
    screen.blit(fuente.render("Press return when done.", True, VERDE),
                     (left + 51, top + 160))

    pg.draw.rect(screen, NEGRO, (left + 39, top + 110, 240, 20))
    pg.draw.rect(screen, BLANCO, (left + 38, top + 108, 244, 24), 1)

    if len(message) !=0:
        screen.blit(fuente.render(message, True, BLANCO), (left+42, top + 111))

    pg.display.flip()




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

'''def sql_connection():
    try:

        con = sqlite3.connect("mydatabase.db")

        return con

    except Error:
        print (Error)

def sql_table(con):

    cur = con.cursor()

    cur.execute("CREATE TABLE if not exists tablaPuntos (nombre, puntos)")


    con.commit()

con = sql_connection()

sql_table(con)'''











sound = pg.mixer.Sound("explota.wav") #Variable para añadir sonido de explosión

background = pg.image.load("Fondo_espacio.jpg").convert()
screen.blit(background, [0, 0])

pg.key.set_repeat(5,100) # Para acelerar la nave al mantener pulsado el cursor

nombre = ""

while not done:
    #Introducir iniciales
    
    print(nombre)
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
        naveRotando = True
        contarGiro = 0
        
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
    
    
    
    if finNivel == True and mostPlaneta == False and naveRotando == True:
        contarGiro +=3
        player.rotarNave()
        if contarGiro > 177:
            naveRotando = False
            contarGiro = 0

    
    if finNivel == True and mostPlaneta == False and naveRotando == False:
        #player.rotarNave()
        if nivel <3:
            texto_salida = 'Nivel ' + str(nivel) + ' Finalizado!! PRESIONA ESPACIO PARA CONTINUAR' 
            texto = fuente.render(texto_salida, True, BLANCO)
            screen.blit(texto, [150,200])   
        else:

            #player.rotarNave()

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
    screen.blit(texto, [15,10])   
    
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
        texto_salida = 'GAME OVER'
        texto_salida_2 = 'PRESIONE ENTER PARA CONTINUAR' 
        texto = fuente.render(texto_salida, True, BLANCO)
        texto2 = fuente.render(texto_salida_2, True, BLANCO)
        screen.blit(texto, [120,270])
        screen.blit(texto2, [120, 300])

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
                        
                        cur.execute("select count(*) from tablaPuntos")
                        numFilas = int(cur.fetchone()[0])

                        print(date_timeSQL)
                        if numFilas > 0:
                            cur.execute("select puntos from tablaPuntos order by puntos ") #recuperar lista ordenada por los puntos
                            minPuntos = cur.fetchone()[0]
                            cur.execute("select id from tablaPuntos order by puntos ") #recuperar lista ordenada por los puntos
                            idBorrar = cur.fetchone()[0]
                            QUERYBORRAR = "delete from tablaPuntos where id =" + str(idBorrar)
                            print(cur.fetchall())
                            print("minPuntos = " + str(minPuntos))   

                        
                        if numFilas < 5:
                            nombre=ask("nombre")
                            cur.execute("insert into tablaPuntos values (?,?,?)", (numFilas+1,nombre,puntos))
                            con.commit()
                            print(numFilas+10)
                        elif minPuntos <= puntos:
                            nombre=ask("nombre")
                            #cur.execute("delete from tablaPuntos where id in (select id from tablaPuntos order by puntos ASC limit 1)")
                            cur.execute(QUERYBORRAR)
                            cur.execute("insert into tablaPuntos values (?,?,?)", (idBorrar,nombre,puntos))
                            con.commit()
                            print(numFilas)







    if finNivel == True and mostPlaneta == False and muerto == False and victoria == False and naveRotando == False:
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
