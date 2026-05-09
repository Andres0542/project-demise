import pygame as pg
import numpy as np
from numba import njit

def generate_map(size):
    layout = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1],
        [1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
        [1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1],
        [1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1],
        [1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,0,1],
        [1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1],
        [1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1],
        [1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1],
        [1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    maph = np.array(layout, dtype=np.int32)
    mapc = np.random.uniform(0, 1, (size, size, 3))

    posx, posy, rot = 1.5, 1.5, np.pi/4

    return posx, posy, rot, maph, mapc

def main():
    gen
    pg.init()
    screen = pg.display.set_mode((800,600))
    running = True
    clock = pg.time.Clock()

    hres = 120 #horizontal resolution
    halfvres = 100 #vertical resolution/2

    mod = hres/60 #scaling factor (60° fov)
    posx, posy, rot = 0, 0, 0
    size = 15
    maph = np.random.choice([0,0,0,1], (size, size))
    #Colores
    mapc = np.random.uniform(0,1, (size, size, 3))
    frame = np.random.uniform(0,1, (hres, halfvres*2, 3))
    sky = pg.image.load('skybox.jpg')
    sky = pg.surfarray.array3d(pg.transform.scale(sky, (360, halfvres*2)))/255
    floor = pg.surfarray.array3d(pg.image.load('floor.jpg'))/255
    wall = pg.surfarray.array3d(pg.image.load('wall.jpg'))/255
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
        frame = new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod, maph, size, wall, mapc)

        surf = pg.surfarray.make_surface(frame*255)
        surf = pg.transform.scale(surf, (800, 600))
        fps = int(clock.get_fps())
        pg.display.set_caption("Pycasting maze - FPS: " + str(fps))

        screen.blit(surf, (0,0))
        pg.display.update()

        posx, posy, rot = movement(posx, posy, rot, pg.key.get_pressed(), clock.tick())

def movement(posx, posy, rot, keys, et):
    if keys[pg.K_LEFT] or keys[ord('a')]:
        rot = rot - 0.001*et

    if keys[pg.K_RIGHT] or keys[ord('d')]:
        rot = rot + 0.001*et
        
    if keys[pg.K_UP] or keys[ord('w')]:
        posx, posy = posx + np.cos(rot)*0.002*et,  posy + np.sin(rot)*0.002*et

    if keys[pg.K_DOWN] or keys[ord('s')]:
        posx, posy = posx - np.cos(rot)*0.002*et,  posy - np.sin(rot)*0.002*et

    return posx, posy, rot

@njit()
def new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod, maph, size, wall, mapc):
    for i in range(hres):
        rot_i = rot + np.deg2rad(i/mod - 30)
        sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i/mod - 30))
        
        # 1. Fondo (Cielo)
        frame[i][:] = sky[int(np.rad2deg(rot_i)%359)][:]

        # 2. Raycasting para encontrar la pared
        x, y = posx, posy
        dist_max = 20  # Límite para evitar bucle infinito
        found_wall = False
        n = 0
        
        for _ in range(2000): # Máximo de pasos para evitar bloqueo
            x += 0.01 * cos
            y += 0.01 * sin
            n += 0.01
            if maph[int(x)%size][int(y)%size]: # Usar size directamente
                found_wall = True
                break
            if n > dist_max:
                break

        # 3. Dibujar Pared (Solo si se encontró una)
        h = 0
        if found_wall:
            h = int(halfvres / (n * cos2 + 0.001))
            xx = int(x * 3 % 1 * 99)
            if x % 1 < 0.02 or x % 1 > 0.98:
                xx = int(y * 3 % 1 * 99)
            
            # Limitar h para no salir de la pantalla
            h_screen = min(h, halfvres)
            
            shade = 0.3 + 0.7 * (h / halfvres)
            if shade > 1: shade = 1
            
            c = shade * mapc[int(x)%size][int(y)%size]
            
            # Texturizado de pared
            yy_coords = np.linspace(0, 99, h_screen * 2) 
            for k in range(h_screen * 2):
                target_y = halfvres - h_screen + k
                if 0 <= target_y < halfvres * 2:
                    idx_y = int(yy_coords[k])
                    frame[i][target_y] = c * wall[xx][idx_y]

        # 4. Dibujar Suelo (Fuera del bucle de búsqueda)
        for j in range(halfvres - h):
            if j < 0: continue
            n_floor = (halfvres / (halfvres - j)) / cos2
            xf, yf = posx + cos * n_floor, posy + sin * n_floor
            xxf, yyf = int(xf * 2 % 1 * 99), int(yf * 2 % 1 * 99)
            shade_f = 0.2 + 0.8 * (1 - j / halfvres)
            
            # Aplicar color de suelo
            pixel_pos = halfvres * 2 - j - 1
            frame[i][pixel_pos] = shade_f * floor[xxf][yyf]
                
    return frame

if __name__ == '__main__':
    main()
    pg.quit()