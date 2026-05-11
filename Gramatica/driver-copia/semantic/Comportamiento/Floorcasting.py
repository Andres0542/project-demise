import pygame as pg
import numpy as np

class Floorcasting:
    def __init__(self):
        self.posx, self.posy = 0.0, 0.0
        self.rot = 0.0

    def main(self):
        pg.init()
        screen = pg.display.set_mode((800, 600))
        clock = pg.time.Clock()
        
        hres = 120  # Horizontal resolution
        halfvres = 100  # Half of vertical resolution
        
        #Cielo
        frame = np.random.uniform(0, 1, (hres, halfvres * 2, 3))
        mod = hres / 60
        frame = np.zeros((hres, halfvres * 2, 3))
        
        running = True
        while running:  # Main game loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            # Render floor
            frame[:, 0:halfvres] = [0.5, 0.7, 1.0]
            for i in range(hres):
                rot_i = self.rot + np.deg2rad(i / mod - 30)
                sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i / mod - 30))
                #frame[i] = sky[int(rot_i*180/np.pi)%360]
                for j in range(halfvres):
                    n = (halfvres / (halfvres - j)) / cos2
                    x, y = self.posx + cos * n, self.posy + sin * n
                    
                    if int(x) % 2 == int(y) % 2:
                        frame[i][halfvres * 2 - j - 1] = [0, 0, 0]  # Black
                    else:
                        frame[i][halfvres * 2 - j - 1] = [1, 1, 1]  # White
            
            # Convert to surface and display
            surf = pg.surfarray.make_surface(frame * 255)
            surf = pg.transform.scale(surf, (800, 600))
            screen.blit(surf, (0, 0))
            pg.display.update()
            
            # Handle movement
            pressed_keys = pg.key.get_pressed()
            dt = clock.tick(60) / 1000.0  # Delta time in seconds
            self.movement(pressed_keys, dt)

    def movement(self, pressed_keys, et):
        # Mouse rotation
        p_mouse = pg.mouse.get_rel()
        self.rot += p_mouse[0] / 200
        
        # Movement keys
        if pressed_keys[pg.K_UP] or pressed_keys[pg.K_w]:
            self.posx += et * np.cos(self.rot)
            self.posy += et * np.sin(self.rot)
        
        if pressed_keys[pg.K_DOWN] or pressed_keys[pg.K_s]:
            self.posx -= et * np.cos(self.rot)
            self.posy -= et * np.sin(self.rot)
        
        if pressed_keys[pg.K_LEFT] or pressed_keys[pg.K_a]:
            self.posx += et * np.sin(self.rot)
            self.posy -= et * np.cos(self.rot)
        
        if pressed_keys[pg.K_RIGHT] or pressed_keys[pg.K_d]:
            self.posx -= et * np.sin(self.rot)
            self.posy += et * np.cos(self.rot)

if __name__ == "__main__":
    game = Floorcasting()
    game.main()
    pg.quit()
