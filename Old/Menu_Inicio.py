
import pygame as pg

def menuInicio():
    iniciar = False  
    #window.fill(black)
    myfont=pg.font.SysFont("Britannic Bold", 40)
    
    nlabel=myfont.render("Welcome Start Screen", 1, (255, 0, 0))    #texto
    
    while (iniciar==False):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.type==pg.K_SPACE:
                iniciar=True


pg.init()

menuInicio()