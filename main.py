# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
size = [1300,600]
ancho = int(input("Ancho de la ventana: "))
alto = int(input("Alto de la ventana: "))
size = (ancho,alto)
titulo = input("¿Cómo quieres que se llame la ventana? ")
rojo = int(input("Cantidad de rojo: "))
verde = int(input("Cantidad de verde: "))
azul = int(input("Cantidad de azul: "))
color = (rojo, verde, azul)
main2(size,titulo,color)
