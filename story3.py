# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
## 紙芝居
img1 = pg.image.load("images/flower1.png")
img2 = pg.image.load("images/flower2.png")
## ボタン
next_img = pg.image.load("images/nextbtn.png")

pushFlag = False
## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # 4.ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

def page1():
    # 3.画面を初期化する
    screen.blit(img1, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 2)

def page2():
    # 3.画面を初期化する
    screen.blit(img2, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

page = 1
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