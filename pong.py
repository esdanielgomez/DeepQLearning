#Modified from http://www.pygame.org/project-Very+simple+Pong+game-816-.html
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
import numpy
import pygame
from pygame.locals import *
from sys import exit
import random
import pygame.surfarray as surfarray

pygame.init()


#MEDIDA DEL ARCO ES 640,480
#740,680)

screen = pygame.display.set_mode((675,675),0,32)

#Creating 2 bars, a ball and background.
#Creando 2 barras, una pelota y fondo.

back = pygame.Surface((675,675))
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((75,75))
bar1 = bar.convert()
bar1.fill((255,255,255))

#bar2 = bar.convert()
#bar2.fill((255,255,255))
circ_sur = pygame.Surface((37,37))
circ = pygame.draw.circle(circ_sur,(255,255,255),(int(37/2),int(37/2)),int(37/2))
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))



# some definitions
bar1_x= 10.
bar1_y= 337.5
circle_x, circle_y = 675, 337.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0,0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

done = False

inicio_pelota = random.randint(1,640)

while done==False:       
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -ai_speed
            elif event.key == K_DOWN:
                bar1_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.
    if bar1_y < 0:
        bar1_y = 0.
    if bar1_y > 600.:
        bar1_y = 600.
    score1 = font.render(str(bar1_score), True,(255,255,255))
    score2 = font.render(str(bar2_score), True,(255,255,255))

    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
    screen.blit(bar1,(bar1_x,bar1_y))
   # screen.blit(bar2,(bar2_x,bar2_y))
    screen.blit(circle,(circle_x,circle_y))
    screen.blit(score1,(250.,210.))
    screen.blit(score2,(380.,210.))

    bar1_y += bar1_move
        
    # movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0
        
    circle_x -= speed_x * time_sec  #LA PELOTA SE MUEVE SIEMPRE PARA LA IZQUIERDA
    circle_y = inicio_pelota
    ai_speed = speed_circ * time_sec
    
    #AI of the computer.
    """
    if circle_x >= 305.:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed
            if  bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed
        else:
            bar2_y == circle_y + 7.5
    
    if bar1_y >= 420.: bar1_y = 420.
    elif bar1_y <= 10. : bar1_y = 10.
    if bar2_y >= 420.: bar2_y = 420.
    elif bar2_y <= 10.: bar2_y = 10.
    """
    #since i don't know anything about collision, ball hitting bars goes like this.
    if circle_x <= bar1_x + 75.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            if circle_x <= 75. and circle_y > 150. and  circle_y < 520.:
                #Choca la pelota con la barra
                #circle_x = 307.5
                print(circle_x , circle_y)
                inicio_pelota = random.randint(1, 640)
                bar1_score+=2
                circle_x = 640
                #speed_x = -speed_x
    """
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            #speed_x = -speed_x
    """
    if circle_x < 5.:
        #LA PELOTA NO CAE EN LA BARRA - SE VA FUERA
        if  circle_y > 150. and circle_y < 520.:
                bar2_score += 2
                #circle_x, circle_y = 640, 232.5
                #bar1_y,bar_2_y = 215., 215.
                circle_x = 640
                inicio_pelota = random.randint(1,640)
    """
    elif circle_x > 620.:
        #LA PELOTA SE VA FUERA DEL CONTRINCATE
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    """
    #LIMITE DE LA PORTERIA
    if circle_x <= 75. and circle_y < 150.:
        if bar1_y < 150. or bar1_y > 520:
            bar2_score +=1
            inicio_pelota = random.randint(1, 640)
            circle_x = 640
        else:
            bar1_score += 1
            inicio_pelota = random.randint(1, 640)
            circle_x = 640
    """
    if circle_x <= 75. and circle_y > 520.:
        if bar1_y > 520.:
            bar2_score +=1
            inicio_pelota = random.randint(1, 640)
            circle_x = 640
        else:
            bar1_score +=1
            inicio_pelota = random.randint(1, 640)
            circle_x = 640
    """

    """
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5
    """
    if circle_x < 5. :
        inicio_pelota = random.randint(1, 640)
        circle_x = 640.

    pygame.display.update()
            
pygame.quit()