################################################################
# Simplesmente use a linha abaixo no cmd.exe
# observe que o caminho é aquele onde está este arquivo
#
# set PYTHONPATH=C:\Users\geral\Desktop\python-simple\packages
#
# ou as linhas a seguir em cada programa
#
import sys
sys.path.append (r"C:\Users\geral\Desktop\python-simple\packages")
try:
    import pygame
except:
    print ("Pygame nao encontrado")
    exit(0)
################################################################


pygame.init()