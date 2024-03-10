# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    pg.draw.rect(screen, pg.Color("RED"), (100, 100, 100, 150))
    pg.draw.line(screen, pg.Color("BLUE"), (250, 100), (350, 250), 5)
    pg.draw.ellipse(screen, pg.Color("GREEN"), (400, 100, 150, 150), 5) #ellipseは楕円
    # 6.画面を表示する
    pg.display.update()
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get(): #イベントを取得
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
