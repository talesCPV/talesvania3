import pygame
import control_panel as cp

count = [0,0,0,0]
cross= ([3,3,60,60],[318,66,60,60],[381,66,60,60])

def throw_wep(screen,itens):
    if(cp.v_wep == 1): # cruz
        wep = (itens.subsurface(pygame.Rect(cross[count[3]])))
    elif(cp.v_wep == 2):  # machado
        wep = (itens.subsurface(pygame.Rect(cp.weapon[cp.v_wep])))
        if(count[3] == 1):
            wep = pygame.transform.flip((wep), True, False)
        elif(count[3] == 2):
            wep = pygame.transform.flip((wep), True, True)
        elif(count[3] == 3):
            wep = pygame.transform.flip((wep), False, True)
    else:
        wep = (itens.subsurface(pygame.Rect(cp.weapon[cp.v_wep])))

    if(cp.wep_thw[0] == 1):
        if (cp.wep_flip[0] == 0):
            wep = pygame.transform.flip((wep), True, False)
        screen.blit(wep, (cp.wep_pos[0] , cp.wep_pos[1] , 60 , 60))
        move_wep(0)

    if(cp.wep_thw[1] == 1):
        if (cp.wep_flip[1] == 0):
            wep = pygame.transform.flip((wep), True, False)
        screen.blit(wep, (cp.wep_pos[2] , cp.wep_pos[3] , 60 , 60))
        move_wep(1)

    if(cp.wep_thw[2] == 1):
        if (cp.wep_flip[2] == 0):
            wep = pygame.transform.flip((wep), True, False)
        screen.blit(wep, (cp.wep_pos[4] , cp.wep_pos[5] , 60 , 60))
        move_wep(2)

def move_wep(num_wep):
    global count
    x = num_wep * 2

    if(cp.v_wep == 1): # cruz
        count[3] += 1
        count[num_wep] += 1
        vel = 35

        if(count[3] == 3):
            count[3] = 0

#        print(cp.wep_pos[x] - cp.play_pos[0])

        if(count[num_wep] >  15 or count[num_wep] <  -10):
            vel *= -1

        if(cp.wep_flip[num_wep] == 0):
            cp.wep_pos[x] -= vel
        else:
            cp.wep_pos[x] += vel

    if(cp.v_wep == 2): # machado
        count[3] += 1
        count[num_wep] += 1
        vel = 35

        y = parabola(count[num_wep])
        print(y)
        cp.wep_pos[x+1] += y

        if(count[3] == 4):
            count[3] = 0

#        if(count[num_wep] > 8 ):
#            cp.wep_pos[x+1] += vel
#        else:
#            cp.wep_pos[x+1] -= vel


        if(cp.wep_flip[num_wep] == 0):
            cp.wep_pos[x] -= vel
        else:
            cp.wep_pos[x] += vel


    if(cp.v_wep == 3): # espada
        if(cp.wep_flip[num_wep] == 0):
            cp.wep_pos[x] -= 35
        else:
            cp.wep_pos[x] += 35

    if(cp.wep_pos[x] < -200 or cp.wep_pos[x] > 1200):
        clear_wep(num_wep)


def clear_wep(num_wep):
    cp.wep_thw[num_wep] = 0
    cp.wep_flip[num_wep] = 0
    cp.wep_pos[num_wep*2] = 0
    count[num_wep] = 0

def parabola(x):
    y = (-3.1 * (x**2) + 1 * x + 80) * -1
    return (y)





