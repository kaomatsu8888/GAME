# 1.ゲームの準備をする
import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
## バーデータ
barrect = pg.Rect(400, 500, 100, 20)
## ボールデータ
ballimg = pg.image.load("images/kaeru.png")
ballimg = pg.transform.scale(ballimg, (30, 30))
ballrect = pg.Rect(400, 450, 30, 30)
vx = random.randint(-10,10)
vy = -5

## ゲームステージ
def gamestage():
    # 3.画面を初期化する
    global vx, vy
    screen.fill(pg.Color("NAVY"))
    # 4.ユーザーからの入力を調べる
    (mx, my) = pg.mouse.get_pos()
    # 5.絵を描いたり、判定したりする
    ## バーの処理
    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)
    ## ボールの処理
    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > 800 - 30:
        vx = -vx
    if barrect.colliderect(ballrect):
        vx = ((ballrect.x + 15) - (barrect.x + 50))  / 4
        vy = random.randint(-10, -5)
        pg.mixer.Sound("sounds/pon.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

# 2.この下をずっとループする
while True:
    gamestage()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()