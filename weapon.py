import pygame
from control_panel import v_wep, weapon as array_wep

wep_thw = [0,0,0] # 0- throwing 1 | 1- throwing 2 | 2- throwing 3
wep_flip = [0,0,0]
wep_pos = [0,0,0,0,0,0] # 0- X1 | 1- Y1 | 2- X2 | 3- Y2 | 4- X3 | 5- Y3

def throw_wep(screen,itens):
    wep = (itens.subsurface(pygame.Rect(array_wep[v_wep])))

    if(wep_thw[0] == 1):
        if (wep_flip[0] == 0):
            wep = pygame.transform.flip((wep), True, False)
        screen.blit(wep, (wep_pos[0] , wep_pos[1] , 60 , 60))
        move_wep(0)

    wep = (itens.subsurface(pygame.Rect(array_wep[v_wep])))
    if(wep_thw[1] == 1):
        if (wep_flip[1] == 0):
            wep = pygame.transform.flip((wep), True, False)
        screen.blit(wep, (wep_pos[2] , wep_pos[3] , 60 , 60))
        move_wep(1)

    wep = (itens.subsurface(pygame.Rect(array_wep[v_wep])))
    if(wep_thw[2] == 1):
        if (wep_flip[2] == 0):
            wep = pygame.transform.flip((wep), True, False)
        screen.blit(wep, (wep_pos[4] , wep_pos[5] , 60 , 60))
        move_wep(2)

def move_wep(num_wep):

    x = num_wep * 2

    if(v_wep == 3): # espada
        if(wep_flip[num_wep] == 0):
            wep_pos[x] -= 35
        else:
            wep_pos[x] += 35

    if(wep_pos[x] < 0 or wep_pos[x] > 1000):
        clear_wep(num_wep)


def clear_wep(num_wep):
    wep_thw[num_wep] = 0
    wep_flip[num_wep] = 0
    wep_pos[num_wep*2] = 0



