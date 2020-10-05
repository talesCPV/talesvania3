import pygame


jump = [0,0,0] # 0 - in jump | 1 - jump counter | 2 - jump direction
whip = [0,0,0] # 0 - in whip | 1 - whip counter | 2 - crouched
anima = [1,0,0] # 0- Player Sprite | 1- Counter Time Sprite | 2 - Weapon Sprite
pos = [50, 380,1] # 0- [x, y] | 1- direction
joystick = [0,0,0,0,0,0,0,0] # 0- up | 1- down | 2- left | 3- right | 4- jump | 5- whip

#      ( ((X,Y,X+,Y+), Fix_X, Fix_y, Fix_X_Crounched, Fix_Y_Crounched)  ) # crounched is used only for weapons sprites
simon= (((60,10,60,110),0,0),((0,10,60,110),0,0),((120,10,60,110),0,0),((180,10,60,110),0,0),((120,10,60,110),0,0),((570,10,80,110),15,0),((650,10,70,110),5,0),((720,10,80,110),17,0),((810,10,80,110),-13,0),((890,10,80,110),-6,0),((960,10,80,110),14,0))
weapon= ((( 0,0,0,0),0,0,0,0),(( 0,120,40,110),-20,0,-50,0),(( 60,120,60,110),-35,-15,-50,-15),(( 120,120,130,110),85,0,80,0))

_hero = []
_weapon = []

def move_simon(screen, sprites):
    print(joystick)

    if(joystick[1]):
        anima[0] = 0
        whip[2] = 1
    else:
        if not(whip[0]):
            whip[2] = 0

        if(joystick[2]    and not jump[0] and not whip[0]):
            pos[0] -= 12
            anima[1] += 1
            if(anima[1] == 2):
                anima[0] += 1
                anima[1] = 0
            pos[2] = 0
            jump[2] = 1
        if(joystick[3] and not jump[0] and not whip[0]):
            pos[0] += 12
            anima[1] += 1
            if(anima[1] == 2):
                anima[0] += 1
                anima[1] = 0
            pos[2] = 1
            jump[2] = 2

        if((anima[0] > 4) or not(joystick[2] or joystick[3])):
            anima[0] = 1
            if not(jump[0]):
                jump[2] = 0

        if(anima[0] < 1):
            anima[0] = 4


    if(joystick[4]):
        anima[0] = 0
        jump[0] = 1

    if(joystick[5]):
        anima[0] = 0
        whip[0] = 1

    if(jump[0]):
        anima[0] = 0
        anima[2] = 0
        jump_simon(jump[2])

    if (whip[0]):
        anima[0] = 5
        whip_simon()


    hero_surface   = (sprites.subsurface(pygame.Rect( simon[anima[0]][0]  )))
    weapon_surface = (sprites.subsurface(pygame.Rect( weapon[anima[2]][0] )))

    invert = -1

    if(pos[2]):
        hero_surface = pygame.transform.flip((hero_surface), True, False)
        weapon_surface = pygame.transform.flip((weapon_surface), True, False)
        invert = 1

#   fix player sprite correct
#   fix pos =     center sprite          + fix feet distance  * side
    fix_x = - simon[anima[0]][0][2] // 2 + simon[anima[0]][1] * invert
    fix_y = - simon[anima[0]][0][3] // 2 + simon[anima[0]][2]

    screen.blit(hero_surface, (pos[0] + fix_x, pos[1] + fix_y))

    #   fix weapon sprite correct
    #   fix pos =     center sprite          + fix feet distance (crouched or not)  * side
    if(whip[2]):
        crouched = 2 # add 2 in fix weapon sprite position index
    else:
        crouched = 0
    fix_x = - weapon[anima[2]][0][2] // 2 + weapon[anima[2]][1 + crouched] * invert
    fix_y = - weapon[anima[2]][0][3] // 2 + weapon[anima[2]][2 + crouched]
    if(whip[2]):
        fix_y += 20
    print("X: ",fix_x, " Y: ", fix_y)

    screen.blit(weapon_surface, (pos[0]+fix_x,pos[1]+fix_y))




def jump_simon(dir):
    global jump
    if (jump[1] < 6):
        pos[1] -= 10
    else:
        pos[1] += 10

    if(dir == 1):
        pos[0] -= 12
    if(dir == 2):
        pos[0] += 12

    jump[1] += 1
    if(jump[1] == 12):
        jump = [0,0,0]


def whip_simon():
    global whip

    if (whip[1] < 2):
        anima[0] = 5
        anima[2] = 1
    else:
        if (whip[1] < 4):
            anima[0] = 6
            anima[2] = 2
        else:
            anima[0] = 7
            anima[2] = 3
    if(whip[2]):
        anima[0] += 3

    whip[1] += 1
    if(whip[1] == 7):
        whip = [0,0,0]
        anima[2] = 0
