# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
img1 = pg.image.load("images/car.png")
img1 = pg.transform.scale(img1, (50, 50))
myrect = pg.Rect(100,100,50,50)

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    myrect.x = myrect.x + 1 # 4.四角形を動かす
    screen.blit(img1, myrect)# myrectの位置にimg1を描画する
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
