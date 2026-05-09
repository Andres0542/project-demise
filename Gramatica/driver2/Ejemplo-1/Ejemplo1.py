import pygame as pg
import numpy as np



def main():
    #Inicializacion de variables y modo de pantalla
    pg.init()
    screen = pg.display.set_mode((800, 600))
    running = True
    clock = pg.time.Clock()

    hres = 120
    halfvres = 100 # half of vertical resolution

    mod = hres/60
    posx, posy, rot = 0,0,0
    frame = np.random.uniform(0,1,(hres, halfvres*2, 3))

    while running: #main game loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        for i in range(hres):
            rot_i = rot + np.deg2rad(i/mod - 30)
            sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i/mod-30))
            #frame[i] = sky[int(rot_i*180/np.pi)%360]
            for j in range(halfvres):
                n = (halfvres/(halfvres-j))/cos2
                x , y = posx + cos*n, posy + sin*n

                if int(x) % 2 == int(y) % 2:
                    frame[i][halfvres*2-j-1] = [0,0,0]
                else:
                    frame[i][halfvres*2-j-1] = [1,1,1]
        
        surf = pg.surfarray.make_surface(frame*255)
        surf = pg.transform.scale(surf, (800, 600))
        screen.blit(surf, (0,0))
        pg.display.update()

        pressed_keys = pg.key.get_pressed()        
        posx, posy, rot = movement(pressed_keys,posx, posy, rot, clock.tick()/500)

def movement(pressed_keys,posx, posy, rot, et):
    
    x, y = (posx, posy)
    
    p_mouse = pg.mouse.get_rel()
    rot = rot +(p_mouse[0])/200
    
    if pressed_keys[pg.K_UP] or pressed_keys[ord('w')]:
        x, y = (x + et*np.cos(rot), y + et*np.sin(rot))
        
    if pressed_keys[pg.K_DOWN] or pressed_keys[ord('s')]:
        x, y = (x - et*np.cos(rot), y - et*np.sin(rot))
        
    if pressed_keys[pg.K_LEFT] or pressed_keys[ord('a')]:
        x, y = (x + et*np.sin(rot), y - et*np.cos(rot))
        
    if pressed_keys[pg.K_RIGHT] or pressed_keys[ord('d')]:
        x, y = (x - et*np.sin(rot), y + et*np.cos(rot))
        
    posx, posy = (x, y)
                                                
    return posx, posy, rot
if __name__ == "__main__":
    main()
    pg.quit()