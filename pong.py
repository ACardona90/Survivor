#!/usr/bin/env python
# -*- coding: utf-8 -*-

 
# Módulos
import sys, pygame
from pygame.locals import *	
 
# Constantes
width = 740
height = 580 

# Clases
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Survivor pong")
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
