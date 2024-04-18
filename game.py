import pygame
import time
from sys import exit
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SPEED = 5
FLOOR_Y = 625

RED   = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()

test_sky = pygame.image.load("images/sky.jpeg")
test_ground = pygame.image.load("images/ground.png")
test_cactus = pygame.image.load("images/cactus.tiff")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/cactus.tiff")
        self.rect = self.image.get_rect()
        self.rect.center = (900, FLOOR_Y)    
 
      def move(self):
        self.rect.move_ip(-SPEED,0)
        if (self.rect.right < 0):
            self.rect.center = (1210, FLOOR_Y)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width / 2, FLOOR_Y)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0,5)
         
        #if self.rect.left > 0:
        #      if pressed_keys[K_LEFT]:
        #          self.rect.move_ip(-5, 0)
        #if self.rect.right < SCREEN_WIDTH:        
        #      if pressed_keys[K_RIGHT]:
        #          self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_sky,(0,0)) 
    screen.blit(test_ground,(0,700))
    
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          screen.fill(RED)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          exit()

    pygame.display.update()
    clock.tick(60)