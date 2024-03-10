# 1.ゲームの準備をする
import pygame as pg, sys
pg.init() # 初期化
screen = pg.display.set_mode((800, 600)) # 画面の大きさ

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE")) #fillは塗りつぶし
    # 5.絵を描いたり、判定したりする
    pg.draw.rect(screen, pg.Color("RED"), (100, 100, 100, 150)) #rectは四角形
    # 6.画面を表示する
    pg.display.update() # 画面を更新する
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
