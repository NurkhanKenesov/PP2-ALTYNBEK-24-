import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

# Setiing up FPS
FPS = 60
FramePerSecond = pygame.time.Clock()

#Just some Variables
score1 = 0
CL = 60
weight = 400
height = 600
step = 5
e_step = 8
clock = pygame.time.Clock()
screen = pygame.display.set_mode((weight, height))
bg = pygame.image.load("AnimatedStreet.png")
font = pygame.font.SysFont("comicsansms", 20)
SPEED = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Fonts when game is over
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#White screen
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Variable for a random number
ran = 0

#Background music
pygame.mixer.Sound('background.wav').play(-1)

# setting up an enemy car
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > height:
            self.top = 0
            global ran
            ran = random.randint(30, 350)
            self.rect.center = (ran, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)



#Creating a coin: uploading its image, size, etc.

class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.counter = 0

    #coin's movement
    def update(self):
        self.rect.move_ip(0, e_step)
        if self.rect.bottom > height:
            self.top = 0
            pan = random.randint(30, 350)
            while(pan > ran-24 and ran+24 > pan):
                pan = random.randint(30, 350)
            self.rect.center = (pan, 0)

    def draw(self):
        screen.blit(self.image, self.rect.topleft)

    #collision
    def collide(self):
        self.top = 0
        self.rect.center = (random.randint(30, 350), 0)



#creating our car
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (150, 520)

    def update(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-step, 0)
        if self.rect.right < weight:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(step, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


#Sprite groups
p1 = player()
e1 = enemy()
c1 = coin()
all_sprite = pygame.sprite.Group()
all_sprite.add(e1)
all_sprite.add(c1)
all_sprite.add(p1)
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(e1)
coins.add(c1)

#Taking one uservent space for a increase speed var
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #score counter
    score = font.render(str(c1.counter), True, (0, 128, 0))
    p1.update()
    e1.update()
    c1.update()

    #collision between our car and enemies car
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        #game over
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprite:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    #Picking up a coin, and one plus score
    if pygame.sprite.spritecollideany(p1, coins):
        pygame.mixer.Sound('eat.ogg').play()
        SPEED += 0.3
        c1.collide()
        c1.counter += 1



    screen.blit(bg, (0, 0))
    screen.blit(score, (weight - score.get_width() - 10, 0))

    p1.draw(screen)
    e1.draw(screen)
    c1.draw()

    pygame.display.update()
    clock.tick(CL)
