import pygame
import time
from sys import exit
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPEED = 5
FLOOR_Y = 665
JUMP_FRAMES = 46
JUMP_HEIGHT_FACTOR = 0.1

INIT_JUMP_COUNT = JUMP_FRAMES/2

RED   = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()

sky = pygame.image.load("images/sky.jpeg").convert()
ground = pygame.image.load("images/ground.png").convert()
# cactus = pygame.image.load("images/cactus.tiff").convert()

class Enemy(pygame.sprite.Sprite):
      def __init__(self,path,x,y):
        super().__init__() 
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
 
      def move(self):
        self.rect.move_ip(-SPEED,0)
        if (self.rect.right < 0):
            self.rect.center = (SCREEN_WIDTH, self.rect.center[1])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/mclaren.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width / 2, 690)
        self.isJumping = False
        self.jumpCount = INIT_JUMP_COUNT
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if not self.isJumping:
            if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE]:
                self.isJumping = True
        else:
            if self.jumpCount >= -INIT_JUMP_COUNT:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * JUMP_HEIGHT_FACTOR
                self.jumpCount -= 1
            else: 
                self.jumpCount = INIT_JUMP_COUNT
                self.isJumping = False

#Setting up Sprites        
P1 = Player()
E1 = Enemy("images/cactus.tiff",1300,665)
E2 = Enemy("images/vulture.png",1500,200)
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky,(0,0)) 
    screen.blit(ground,(0,700))
    
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