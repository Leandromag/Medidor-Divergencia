import pygame
import sys
from pygame import *
from Medidor import Medidor

WIDTH = 517
HEIGHT = 210



pygame.init()
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
sprites=pygame.sprite.Group()


medidor=Medidor()
medidor.formarNumero()
lista=medidor.get_lista_spr()


sprites=pygame.sprite.Group()

for sprite in lista:
    sprites.add(sprite)

ventana.fill((0,0,0))
sprites.draw(ventana)

pygame.display.set_caption("Divergencia Actual: "+medidor.linea)
pygame.display.flip()

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60) / 1000
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            pygame.quit()
            sys.exit(0)
