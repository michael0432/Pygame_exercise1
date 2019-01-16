import pygame
import random
from pygame.locals import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('./image/player.png').convert()
        self.image = pygame.transform.scale(self.image , (36,53))
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.image.get_rect(center=(300, 400))
        self.speed = 5
        self.hp = Hp()
        self.invincible = False
    def move(self, pressed_key):
        if pressed_key[K_UP] or pressed_key[K_w]:
            self.rect.move_ip(0,-self.speed)
        if pressed_key[K_DOWN] or pressed_key[K_s]:
            self.rect.move_ip(0,self.speed)
        if pressed_key[K_RIGHT] or pressed_key[K_d]:
            self.rect.move_ip(self.speed,0)
        if pressed_key[K_LEFT] or pressed_key[K_a]:
            self.rect.move_ip(-self.speed,0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
    def reset(self):
        self.rect = self.image.get_rect(center=(300, 400))
        self.hp = Hp()

class Hp(pygame.sprite.Sprite):
    def __init__(self):
        super(Hp, self).__init__()
        self.max_hp = 10
        self.now_hp = 10
        self.heart_group = pygame.sprite.Group()
        for i in range(0,self.max_hp):
            h = Heart((25 + i*25,25))
            self.heart_group.add(h)

    def add_hp(self,add_number):
        if self.now_hp < max_hp:
            self.now_hp += 1
            self.heart_group.empty()
            for i in range(0,self.now_hp):
                h = Heart((25 + i*25,25))
                self.heart_group.add(h)
    def substract_hp(self,substract_hp):
        self.now_hp -= 1
        self.heart_group.empty()
        for i in range(0,self.now_hp):
            h = Heart((25 + i*25,25))
            self.heart_group.add(h)

class Heart(pygame.sprite.Sprite):
    def __init__(self,position):
        super(Heart, self).__init__()
        self.image = pygame.image.load('./image/heart.png').convert()
        self.image = pygame.transform.scale(self.image , (25,25))
        self.rect = self.image.get_rect(center = position)
        self.image.set_colorkey((0,0,0),RLEACCEL)

