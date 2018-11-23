import pygame
from random import randrange
from random import randint
from pygame import sprite
from copy import copy


class Medidor:

    listaSpr=list()
    listaSprFormados=list()
    sprsht=sprite.Sprite()
    linea="lineaTemporal"

    def __init__(self):
        self.crearListaSprites()
        self.sprsht.spritesheet=pygame.image.load("images/medidor.png").convert_alpha()
        self.iniciarMedidor()


    def formarNumero(self):

        self.listaSprFormados.clear()


        for i in range(0,8):
            eleccion=randrange(10)
            if i == 0:
                eleccion=randint(0,1)
                if eleccion == 0:
                    self.linea="BETA"
                else:
                    self.linea="ALFA"
            if i == 1:
                eleccion=10
            spri=copy(self.listaSpr[eleccion])
            spri.rect=(i*65,0)
            self.listaSprFormados.append(spri)

    def get_lista_spr(self):
        return self.listaSprFormados

    def crearListaSprites(self):
        for i in range(0,11):
            self.listaSpr.append(sprite.Sprite())

    def iniciarMedidor(self):
        aux=0
        img=0
        for sprite in self.listaSpr:
            sprite.image=pygame.transform.scale(self.sprsht.spritesheet.subsurface((img,0,130,384)),(65,192))
            sprite.rect = sprite.image.get_rect()
            sprite.rect=(aux,0)
            aux=aux+65
            img=img+130
