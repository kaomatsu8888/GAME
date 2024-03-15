# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
## 紙芝居
img1 = pg.image.load("images/flower1.png")
img2 = pg.image.load("images/flower2.png")

def page1():
    # 3.画面を初期化する
    screen.blit(img1, (0,0))

def page2():
    # 3.画面を初期化する
    screen.blit(img2, (0,0))

page = 2
# 2.この下をずっとループする
while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()