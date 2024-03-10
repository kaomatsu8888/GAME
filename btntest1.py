# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
next_img = pg.image.load("images/nextbtn.png")


# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    btn = screen.blit(next_img,(350, 200))
    # 4.ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    # 5.絵を描いたり、判定したりする
    if mdown[0]:
        if btn.collidepoint(mx, my):
            print("押した!")
    else:
        print("押していない")
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    