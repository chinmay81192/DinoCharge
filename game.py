import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()

test_sky = pygame.image.load("images/sky.jpeg")
test_ground = pygame.image.load("images/ground.png")
test_cactus = pygame.image.load("images/cactus.tiff")

cactus_x_position = 900
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_sky,(0,0)) 
    screen.blit(test_ground,(0,700))
    if cactus_x_position < -10:
        cactus_x_position = 1210
    cactus_x_position -= 4
    screen.blit(test_cactus,(cactus_x_position,625))      
    pygame.display.update()
    clock.tick(60)