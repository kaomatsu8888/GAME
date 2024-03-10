import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))

while True:
    screen.fill(pg.Color("WHITE"))
    pg.draw.rect(screen, pg.Color("RED"), (100, 100, 100, 150))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()