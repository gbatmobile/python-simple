import sys
sys.path.append (r"C:\Users\geral\Desktop\python-simple\packages")

try:
    import pygame
    print ("pygame ok....")
except:
    print ("Pygame nao encontrado")
    exit(0)

import time

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Ol� mundo')

screen.fill([0, 0, 0])

pygame.display.flip()

time.sleep(5)