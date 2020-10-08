import pygame
import control_panel as cp


#      ( ((X,Y,X+,Y+), Fix_X, Fix_y, Fix_X_Crounched, Fix_Y_Crounched)  ) # crounched is used only for weapons sprites
simon= (((60,10,60,110),0,0),((0,10,60,110),0,0),((120,10,60,110),0,0),((180,10,60,110),0,0),((120,10,60,110),0,0),((570,10,80,110),15,0),((650,10,70,110),5,0),((720,10,80,110),17,0),((810,10,80,110),-13,0),((890,10,80,110),-6,0),((960,10,80,110),14,0))
whip= ((( 0,0,0,0),0,0,0,0),(( 0,120,40,110),-20,0,-50,0),(( 60,120,60,110),-35,-15,-50,-15),(( 120,120,130,110),85,0,80,0))



def move_simon(screen, sprites, joystick):
#    print(joystick)

    if(joystick[1]):
        cp.play_anima[0] = 0
        cp.play_whip[2] = 1
    else:
        if not(cp.play_whip[0]):
            cp.play_whip[2] = 0

        if(joystick[2]    and not cp.play_jump[0] and not cp.play_whip[0]):
            cp.play_pos[0] -= 12
            cp.play_anima[1] += 1
            if(cp.play_anima[1] == 2):
                cp.play_anima[0] += 1
                cp.play_anima[1] = 0
            cp.play_pos[2] = 0
            cp.play_jump[2] = 1
        if(joystick[3] and not cp.play_jump[0] and not cp.play_whip[0]):
            cp.play_pos[0] += 12
            cp.play_anima[1] += 1
            if(cp.play_anima[1] == 2):
                cp.play_anima[0] += 1
                cp.play_anima[1] = 0
            cp.play_pos[2] = 1
            cp.play_jump[2] = 2

        if((cp.play_anima[0] > 4) or not(joystick[2] or joystick[3])):
            cp.play_anima[0] = 1
            if not(cp.play_jump[0]):
                cp.play_jump[2] = 0

        if(cp.play_anima[0] < 1):
            cp.play_anima[0] = 4


    if(joystick[4]):
        cp.play_anima[0] = 0
        cp.play_jump[0] = 1

    if(joystick[5]):
        cp.play_anima[0] = 0
        cp.play_whip[0] = 1


    if(cp.play_jump[0]):
        cp.play_anima[0] = 0
        cp.play_anima[2] = 0
        jump_simon(cp.play_jump[2])

    if (cp.play_whip[0]):
        cp.play_anima[0] = 5
        whip_simon(joystick)


    hero_surface   = (sprites.subsurface(pygame.Rect( simon[cp.play_anima[0]][0]  )))
    weapon_surface = (sprites.subsurface(pygame.Rect( whip[cp.play_anima[2]][0] )))

    invert = -1

    if(cp.play_pos[2]):
        hero_surface = pygame.transform.flip((hero_surface), True, False)
        weapon_surface = pygame.transform.flip((weapon_surface), True, False)
        invert = 1

#   fix player sprite correct
#   fix pos =     center sprite          + fix feet distance  * side
    fix_x = - simon[cp.play_anima[0]][0][2] // 2 + simon[cp.play_anima[0]][1] * invert
    fix_y = - simon[cp.play_anima[0]][0][3] // 2 + simon[cp.play_anima[0]][2]

    screen.blit(hero_surface, (cp.play_pos[0] + fix_x, cp.play_pos[1] + fix_y))

    #   fix weapon sprite correct
    #   fix pos =     center sprite          + fix feet distance (crouched or not)  * side
    if(cp.play_whip[2]):
        crouched = 2 # add 2 in fix weapon sprite position index
    else:
        crouched = 0
    fix_x = - whip[cp.play_anima[2]][0][2] // 2 + whip[cp.play_anima[2]][1 + crouched] * invert
    fix_y = - whip[cp.play_anima[2]][0][3] // 2 + whip[cp.play_anima[2]][2 + crouched]
    if(cp.play_whip[2]):
        fix_y += 20

    screen.blit(weapon_surface, (cp.play_pos[0]+fix_x,cp.play_pos[1]+fix_y))

def jump_simon(dir):

    if (cp.play_jump[1] < 6):
        cp.play_pos[1] -= 10
    else:
        cp.play_pos[1] += 10

    if(dir == 1):
        cp.play_pos[0] -= 12
    if(dir == 2):
        cp.play_pos[0] += 12

    cp.play_jump[1] += 1
    if(cp.play_jump[1] == 12):
        cp.play_jump = [0,0,0]

def whip_simon(joystick):
    global whip

    if (cp.play_whip[1] < 2):
        cp.play_anima[0] = 5
        if not (joystick[0]): cp.play_anima[2] = 1
        else: cp.play_anima[2] = 0
    else:
        if (cp.play_whip[1] < 4):
            cp.play_anima[0] = 6
            if not (joystick[0]): cp.play_anima[2] = 2
            else: cp.play_anima[2] = 0
        else:
            cp.play_anima[0] = 7
            if not (joystick[0]): cp.play_anima[2] = 3
            else: cp.play_anima[2] = 0
    if(cp.play_whip[2]):
        cp.play_anima[0] += 3

    cp.play_whip[1] += 1
    if(cp.play_whip[1] == 7):
        cp.play_whip = [0,0,0]
        cp.play_anima[2] = 0
        if (joystick[0] and ( cp.wep_thw[0]+cp.wep_thw[1]+cp.wep_thw[2] ) < cp.v_mult+1 ):

            if (cp.play_pos[2] == 0):
                w_x = cp.play_pos[0] - 80
            else:
                w_x = cp.play_pos[0] + 20
            w_y =  cp.play_pos[1] - 40

            if(cp.wep_thw[0] == 0):
                cp.wep_thw[0] = 1
                cp.wep_pos[0] = w_x
                cp.wep_pos[1] = w_y
                cp.wep_flip[0] = cp.play_pos[2]

            else:
                if (cp.wep_thw[1] == 0):
                    cp.wep_thw[1] = 1
                    cp.wep_pos[2] = w_x
                    cp.wep_pos[3] = w_y
                    cp.wep_flip[1] = cp.play_pos[2]
                else:
                    if (cp.wep_thw[2] == 0):
                        cp.wep_thw[2] = 1
                        cp.wep_pos[4] = w_x
                        cp.wep_pos[5] = w_y
                        cp.wep_flip[2] = cp.play_pos[2]


