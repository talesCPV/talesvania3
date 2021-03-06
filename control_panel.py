import pygame

v_energy = 16
v_enemy = 16
v_time = 300
v_score = 0
v_stage = [1,1]
v_hearts = 35
v_lifes = 4
v_mult = 1
v_wep = 2
c_time = 0

weapon= ([0,0,0,0],[3,3,60,60],[66,3,60,60],[129,3,60,60],[192,3,60,60],[255,3,60,60])
mult = ([0,0,0,0],[381,3,60,60],[444,3,60,60])

play_jump =  [0,0,0] # 0 - in jump | 1 - jump counter | 2 - jump direction
play_whip =  [0,0,0] # 0 - in whip | 1 - whip counter | 2 - crouched
play_anima = [1,0,0] # 0- Player Sprite | 1- Counter Time Sprite | 2 - Weapon Sprite
play_pos = [50, 380,1] # 0- [x, y] | 1- direction

wep_thw = [0,0,0] # 0- throwing 1 | 1- throwing 2 | 2- throwing 3
wep_flip = [0,0,0] # 0- wep 01 | 1- wep 02 |2- wep 03 |
wep_pos = [0,0,0,0,0,0] # 0- X1 | 1- Y1 | 2- X2 | 3- Y2 | 4- X3 | 5- Y3
wep_anima = [0,0]

def print_control(screen,fps, itens):
    global c_time, v_time

    s_size = pygame.display.get_surface().get_size() # screen size [width, height]
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, s_size[0], 120))

    c_time += 1
    if (c_time == fps):
        c_time = 0
        v_time -= 1

    # TEXT

    font = pygame.font.Font('font/PressStart2P-Regular.ttf', 20)

    score = font.render('SCORE-'+str(v_score).zfill(6), True, (255,255,255), (0,0,0))
    textRect = score.get_rect()
    textRect.center = ( 150,  20)
    screen.blit(score, textRect)

    time = font.render('TIME '+str(v_time).zfill(6), True, (255,255,255), (0,0,0))
    textRect = time.get_rect()
    textRect.center = ( 500,  20)
    screen.blit(time, textRect)

    stage = font.render('STAGE '+str(v_stage[0])+"-"+str(v_stage[1]), True, (255,255,255), (0,0,0))
    textRect = stage.get_rect()
    textRect.center = ( 750,  20)
    screen.blit(stage, textRect)

    player = font.render('PLAYER ', True, (255,255,255), (0,0,0))
    textRect = player.get_rect()
    textRect.center = ( 100,  50)
    screen.blit(player, textRect)

    enemy = font.render('ENEMY ', True, (255,255,255), (0,0,0))
    textRect = enemy.get_rect()
    textRect.center = ( 90,  80)
    screen.blit(enemy, textRect)

    hearts = font.render('-'+str(v_hearts).zfill(2), True, (255,255,255), (0,0,0))
    textRect = hearts.get_rect()
    textRect.center = ( 710,  50)
    screen.blit(hearts, textRect)

    lifes = font.render('P-'+str(v_lifes-1).zfill(2), True, (255,255,255), (0,0,0))
    textRect = lifes.get_rect()
    textRect.center = ( 700,  80)
    screen.blit(lifes, textRect)

    # BARS
    for i in range (v_energy):
        pygame.draw.rect(screen, (255, 55, 26), (160 + (i * 15), 40, 10, 20))

    for i in range (v_enemy):
        pygame.draw.rect(screen, (255, 123, 89), (160 + (i * 15), 70, 10, 20))

    # WEAPON SQUARE
    sq = (480,40,100,60)

    pygame.draw.lines(screen, (255, 55, 26), True, [(sq[0], sq[1]), (sq[0]+sq[2], sq[1]), (sq[0]+sq[2], sq[1]+sq[3]), (sq[0], sq[1]+sq[3])], 5)

    # IMAGES

    wep = (itens.subsurface(pygame.Rect( weapon[v_wep] )))
    wep_x = sq[0]+ sq[2]//2 - weapon[v_wep][2]//2
    wep_y = sq[1]+sq[3]//2 - weapon[v_wep][3]//2
    screen.blit(wep, (wep_x , wep_y , 60 , 60))

    screen.blit(itens.subsurface(pygame.Rect( 255 , 66 , 60 , 60 )), (640 , 20 , 60 , 60))

    mul = (itens.subsurface(pygame.Rect( mult[v_mult] )))
    screen.blit(mul, (780 , 30 , 60 , 60))