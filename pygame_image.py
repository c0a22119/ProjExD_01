import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img0 = pg.image.load("EX01/fig/pg_bg.jpg")#haikei
    bg_img1 = pg.image.load("EX01/fig/pg_bg.jpg")#haikei
    bg_img1 = pg.transform.flip(bg_img1,True,False)#haikei
    bg_img11 = pg.image.load("EX01/fig/pg_bg.jpg")#haikei

    bg_img = pg.image.load("EX01/fig/3.png")
    bg_img = pg.transform.flip(bg_img,True,False)
    bg_img2 = pg.transform.rotozoom(bg_img,0,1.0)
    bg_img3 = pg.transform.rotozoom(bg_img,5,1.0)
    bg_img4 = pg.transform.rotozoom(bg_img,10,1.0)
    bk_imgs = [bg_img,bg_img2,bg_img3,bg_img4]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200
        if tmr%1000 <= 500:
            num = 0
        else:
            num = 3
        screen.blit(bg_img0, [-x,0])#haikei
        screen.blit(bg_img0, [1600-x,0])#haikei
        screen.blit(bg_img1, [1600-x,0])#haikei
        screen.blit(bg_img11, [3200-x,0])#haikei

        screen.blit(bk_imgs[num],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()