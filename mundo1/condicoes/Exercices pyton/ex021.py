import pygame

pygame.init()                  
pygame.mixer.music.load("d:/Cursos web/curso-python/Exercices pyton/ola.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

""" pygame.init() serve para iniciar o pygame"""
""" O pygame.mixer.music.load()  serve  para puxar/ou carregar o audio"""
""" O pygame.mixer.music.play()   serve para para dar play o audio """







