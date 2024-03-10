# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 4.ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    # 5.絵を描いたり、判定したりする
    if mdown[0]:
        pg.draw.rect(screen, pg.Color("RED"), (mx-50, my-50, 100, 100))
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            