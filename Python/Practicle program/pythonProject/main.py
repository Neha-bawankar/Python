import pygame

#intialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))


#Titel and Icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # screen rgb -red green and blue
        screen.fill((0, 255, 0))
        pygame.display.update()