# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 4.ユーザーからの入力を調べる
    key = pg.key.get_pressed() # 4.ユーザーからの入力を調べる
    if key[pg.K_RIGHT]: # 右キーが押されていたら
        print("RIGHT") # 5.絵を描いたり、判定したりする
    if key[pg.K_LEFT]: # 左キーが押されていたら
        print("LEFT") # 5.絵を描いたり、判定したりする
    # 6.画面を表示する
    pg.display.update() # 画面を更新する
    pg.time.Clock().tick(60) # 60fpsになるように時間を調整する
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
