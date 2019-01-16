import pygame
import random
from pygame.locals import *

class Enemy1(pygame.sprite.Sprite):
    def __init__(self,position):
        super(Enemy1, self).__init__()
        self.image = pygame.image.load('./image/enemy1.png').convert()
        self.image = pygame.transform.scale(self.image , (60,40))
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.image.get_rect(center=position)
        self.speed = 5
    def update(self,player_positionx,player_positiony):
        dx, dy = (player_positionx - self.rect.centerx , player_positiony - self.rect.centery)
        stepx, stepy = (dx / 40 , dy / 50)
        self.rect.move_ip(stepx,stepy)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600