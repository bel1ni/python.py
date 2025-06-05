import pygame
pygame.init()
pygame.mixer.init()
sound=pygame.mixer.Sound('desafios/desafio021/thatsmyname.mp3')
screen=pygame.display.set_mode((400,400))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                sound.play()
pygame.display.update()