import pygame
from pygame.locals import *
from player import *
from menu import *
from stage1 import *
from enemy import * 

# 新增敵人的event
ADDENEMY = pygame.USEREVENT +1


pygame.init()
screen = pygame.display.set_mode((800,600))
running = 1
PAGE = 0 # 目前在哪一個頁面：0為menu，1為第一關

# For Page 0 - menu用到的變數
menu_group = pygame.sprite.Group()
game_menu = Menu()
menu_group.add(game_menu)

# For Page 1 - 第一關用到的變數
player = Player()
stage1 = Stage1()
pygame.time.set_timer(ADDENEMY,1000)
start_ticks=pygame.time.get_ticks() # 用於計算無敵時間

# main loop
while running:
    if PAGE == 0: # menu頁面
        for event in pygame.event.get(): 
            # 離開遊戲
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # 離開遊戲
            elif event.type == QUIT:
                running = False
            # 判斷滑鼠點擊start
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if game_menu.start.rect.collidepoint(pygame.mouse.get_pos()):
                    # 切下一頁
                    PAGE = 1
                    player.reset()
                    stage1.reset()

        # blit / flip
        screen.fill((255, 255, 255))
        for all_item in menu_group:
            screen.blit(all_item.image,all_item.rect)
            screen.blit(all_item.start.image,all_item.start.rect)
            screen.blit(all_item.title.textSurfaceObj,all_item.title.textRectObj)
        pygame.display.flip()

    elif PAGE == 1: # 第一關頁面

        # 判斷敵人撞到
        hit_enemy = pygame.sprite.spritecollideany(player,stage1.enemy_group)
        if hit_enemy and player.invincible == False:
            # 敵人消失、玩家扣血、玩家暫時無敵
            hit_enemy.kill()
            player.hp.substract_hp(1)
            player.invincible = True
            start_ticks=pygame.time.get_ticks()
        # 死亡
        if player.hp.now_hp == 0:
            PAGE = 0


        for event in pygame.event.get():
            # 離開遊戲
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # 離開遊戲
            elif event.type == QUIT:
                running = False
            # 產生敵人
            if event.type == ADDENEMY:
                stage1.generate_enemy()

        # 被撞到後0.5秒，解除無敵
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds > 0.5:
            player.invincible = False

        # 控制player移動
        pressed_keys = pygame.key.get_pressed()
        player.move(pressed_keys)

        # 敵人移動  
        for e in stage1.enemy_group:
            e.update(player.rect.centerx,player.rect.centery)

        # blit / flip
        screen.fill((255, 255, 255))
        screen.blit(player.image,player.rect)
        for h in player.hp.heart_group:
            screen.blit(h.image,h.rect)
        for e in stage1.enemy_group:
            screen.blit(e.image,e.rect)
        pygame.display.flip()




        