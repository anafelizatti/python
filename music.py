import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
#precisa colar um arquivo de musica dentro da pasta de projeto pra ela tocar.
