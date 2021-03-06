import pygame
import random
from pygame.locals import *
from enemy import *

# 第一關畫面
class Stage1(pygame.sprite.Sprite):
    def __init__(self):
        super(Stage1, self).__init__()
        self.image = pygame.image.load('./image/stage1_background.jpg').convert()
        self.image = pygame.transform.scale(self.image , (800,600))
        self.rect = self.image.get_rect(center = (400,300))
        self.all_sprite = pygame.sprite.Group() 
        self.enemy_group = pygame.sprite.Group() # 敵人的group

    # 產生敵人
    def generate_enemy(self):
        e = Enemy1((random.randint(0,800),random.randint(0,600)))
        self.enemy_group.add(e)

    # 重設畫面，用於重新開始
    def reset(self):
        self.all_sprite = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
