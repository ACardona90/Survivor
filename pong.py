#!/usr/bin/env python
# -*- coding: utf-8 -*-

 
# Módulos
import sys, pygame
from pygame.locals import *	
 
# Constantes
width = 1024
height = 768 

# Clases
# ---------------------------------------------------------------------
 
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/bola.jpg", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.speed = [0.5, -0.5]

    def actualizar(self, time):
    self.rect.centerx += self.speed[0] * time
    self.rect.centery += self.speed[1] * time
    if self.rect.left <= 0 or self.rect.right >= width:
        self.speed[0] = -self.speed[0]
        self.rect.centerx += self.speed[0] * time
    if self.rect.top <= 0 or self.rect.bottom >= height:
        self.speed[1] = -self.speed[1]
        self.rect.centery += self.speed[1] * time

    if pygame.sprite.collide_rect(self, palaj):
        self.speed[0] = -self.speed[0]
        self.rect.centerx += self.speed[0] * time

class Pala(pygame.sprite.sprite):
    def __init__(self, X):
        pygame.sprite.sprite.__init__(self)
        self.image = load_imagine("imagenes/pala.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = height / 2
        self.speed = 0.5

    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= height:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
        

# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Survivor pong")

    background_image = load_image('imagenes/fondo.jpg')
    bola = Bola()
    palaj = Pala

    clock = pygame.time.Clock()

    while True:
        time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
                
        bola.actualizar(time, palaj)
        pala_jug.mover(time, keys)
        screen.blit(background_image, (0,0))
        screen.blit(bola.image, bola.rect)
        screen.blit(palaj.image, palaj.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
