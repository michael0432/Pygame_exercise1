import pygame
from pygame.locals import *
from player import *
from menu import *
from stage1 import *
from enemy import * 

ADDENEMY = pygame.USEREVENT +1


pygame.init()
screen = pygame.display.set_mode((800,600))
running = 1
PAGE = 0

# For Page 0
menu_group = pygame.sprite.Group()
game_menu = Menu()
menu_group.add(game_menu)

# For Page 1
player = Player()
stage1 = Stage1()
pygame.time.set_timer(ADDENEMY,1000)
start_ticks=pygame.time.get_ticks()

while running:
    if PAGE == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if game_menu.start.rect.collidepoint(pygame.mouse.get_pos()):
                    PAGE = 1
                    player.reset()
                    stage1.reset()
                    # change_page
        screen.fill((255, 255, 255))
        for all_item in menu_group:
            screen.blit(all_item.image,all_item.rect)
            screen.blit(all_item.start.image,all_item.start.rect)
            screen.blit(all_item.title.textSurfaceObj,all_item.title.textRectObj)
        pygame.display.flip()

    elif PAGE == 1:
        hit_enemy = pygame.sprite.spritecollideany(player,stage1.enemy_group)
        if hit_enemy and player.invincible == False:
            hit_enemy.kill()
            player.hp.substract_hp(1)
            player.invincible = True
            start_ticks=pygame.time.get_ticks()
        if player.hp.now_hp == 0:
            PAGE = 0
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            if event.type == ADDENEMY:
                stage1.generate_enemy()

        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds > 0.5:
            player.invincible = False

        pressed_keys = pygame.key.get_pressed()
        player.move(pressed_keys)   
        for e in stage1.enemy_group:
            e.update(player.rect.centerx,player.rect.centery)
        screen.fill((255, 255, 255))
        screen.blit(player.image,player.rect)
        for h in player.hp.heart_group:
            screen.blit(h.image,h.rect)
        for e in stage1.enemy_group:
            screen.blit(e.image,e.rect)
        pygame.display.flip()




        