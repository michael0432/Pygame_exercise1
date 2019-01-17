import pygame
import random
from pygame.locals import *

# Player : 玩家
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('./image/player.png').convert()
        self.image = pygame.transform.scale(self.image , (36,53))
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.image.get_rect(center=(300, 400)) # player的位置
        self.speed = 5 # player的移動速度
        self.hp = Hp() # player的hp
        self.invincible = False # player是否無敵，被用在剛被怪物撞到
    def move(self, pressed_key):
        # player 移動
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
        # player reset : 用在重新開始遊戲
        self.rect = self.image.get_rect(center=(300, 400))
        self.hp = Hp()

# HP : 用來記錄hp
class Hp(pygame.sprite.Sprite):
    def __init__(self):
        super(Hp, self).__init__()
        self.max_hp = 10 # hp最大值
        self.now_hp = 10 # 當前hp
        self.heart_group = pygame.sprite.Group() #放血量愛心的group
        for i in range(0,self.max_hp): # 初始愛心的圖片
            h = Heart((25 + i*25,25)) # 每隔25pixel放一個
            self.heart_group.add(h)

    def add_hp(self,add_number): # 加一滴血
        if self.now_hp < max_hp:
            self.now_hp += 1
            self.heart_group.empty() # 清空heart_group
            for i in range(0,self.now_hp): # 重新放一次heart
                h = Heart((25 + i*25,25))
                self.heart_group.add(h)

    def substract_hp(self,substract_hp):
        self.now_hp -= 1
        self.heart_group.empty() # 清空heart_group
        for i in range(0,self.now_hp): # 重新放一次heart
            h = Heart((25 + i*25,25))
            self.heart_group.add(h)

# 愛心的圖案
class Heart(pygame.sprite.Sprite):
    def __init__(self,position):
        super(Heart, self).__init__()
        self.image = pygame.image.load('./image/heart.png').convert()
        self.image = pygame.transform.scale(self.image , (25,25))
        self.rect = self.image.get_rect(center = position)
        self.image.set_colorkey((0,0,0),RLEACCEL)

