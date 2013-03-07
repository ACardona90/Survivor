#!/usr/bin/env python
# -*- coding: utf-8 -*-

 
# Módulos
import pygame
from pygame.locals import *	
 
# Constantes
width = 640
height = 480 

# Clases
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ventana pong")
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
