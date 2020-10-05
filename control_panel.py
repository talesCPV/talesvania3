import pygame

v_energy = 100
v_enemy = 100
v_time = 300
v_score = 3700
v_stage = [1,1]
v_hearts = 5
v_lifes = 4

c_time = 0

def print_control(screen,fps):
    global c_time, v_time

    s_size = pygame.display.get_surface().get_size() # screen size [width, height]
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, s_size[0], 100))

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
    textRect.center = ( 800,  20)
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

    # IMAGES