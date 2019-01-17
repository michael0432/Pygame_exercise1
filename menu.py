import pygame
from pygame.locals import *

# Menu的主要class
class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super(Menu, self).__init__()
        self.image = pygame.image.load('./image/background.jpg').convert()
        self.image = pygame.transform.scale(self.image , (800,600))
        self.rect = self.image.get_rect(center = (400,300))
        self.start = StartGame()
        self.title = Title()
        
# 開始按鈕
class StartGame(pygame.sprite.Sprite):
    def __init__(self):
        super(StartGame, self).__init__()
        self.image = pygame.image.load('./image/start.png').convert()
        self.image = pygame.transform.scale(self.image , (300 , 96))
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.image.get_rect(center = (400,300))

# 遊戲標題
class Title(pygame.sprite.Sprite):
    def __init__(self):
        super(Title, self).__init__()
        self.fontObj = pygame.font.Font('./word/OpenSans-Bold.ttf',80)
        self.textSurfaceObj = self.fontObj.render('BOOOOOM!', True, (255,255,0))
        self.textRectObj = self.textSurfaceObj.get_rect(center = (400,150))

# class LeaveGame(pygame.sprite.Sprite):