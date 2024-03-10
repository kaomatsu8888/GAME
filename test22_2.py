# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
imageR = pg.image.load("images/playerR.png")
myrect = pg.Rect(300, 200, 80, 100)

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    vx = 0
    # 4.ユーザーからの入力を調べる
    key = pg.key.get_pressed()
    # 5.絵を描いたり、判定したりする
    if key[pg.K_RIGHT]:
        vx = 5
    if key[pg.K_LEFT]:
        vx = -5
    myrect.x = myrect.x + vx
    screen.blit(imageR, myrect)
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            