import sys, pygame
from sprites import move_simon
from control_panel import print_control


pygame.init()

pygame.display.set_caption("Talesvania 3")
screen = pygame.display.set_mode((1200, 600))
sprites = pygame.image.load('img/simon_sprites.png').convert_alpha()
sprites = pygame.transform.scale(sprites, (1281, 235) ) # escala

itens = pygame.image.load('img/itens.png').convert_alpha()
itens = pygame.transform.scale(itens, (570, 204) ) # escala

joystick = [0,0,0,0,0,0,0,0] # 0- up | 1- down | 2- left | 3- right | 4- jump | 5- whip

fps = 16
clock = pygame.time.Clock()

while 1:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                joystick[0] = 0
            if event.key == pygame.K_DOWN:
                joystick[1] = 0
            if event.key == pygame.K_LEFT:
                joystick[2] = 0
            if event.key == pygame.K_RIGHT:
                joystick[3] = 0
            if event.key == pygame.K_z:
                joystick[4] = 0
            if event.key == pygame.K_x:
                joystick[5] = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                joystick[0] = 1
            if event.key == pygame.K_DOWN:
                joystick[1] = 1
            if event.key == pygame.K_LEFT:
                joystick[2] = 1
            if event.key == pygame.K_RIGHT:
                joystick[3] = 1
            if event.key == pygame.K_z:
                joystick[4] = 1
            if event.key == pygame.K_x:
                joystick[5] = 1

    screen.fill((255, 255, 255)) # background color

    move_simon(screen, sprites, joystick)
    print_control(screen,fps, itens)

    #    print("X: ",fix_x, " Y: ", fix_y)


    pygame.display.update()
