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
## ボタンデータ
replay_img = pg.image.load("images/replaybtn.png")
## メインループで使う変数
pushFlag = False
page = 1

## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # 4.ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            pg.mixer.Sound("sounds/pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

## ゲームステージ
def gamestage():
    # 3.画面を初期化する
    global vx, vy
    global page
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
    if ballrect.y > 600:
        page = 2
        pg.mixer.Sound("sounds/down.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)
    
## データのリセット
def gamereset():
    global vx, vy
    vx = random.randint(-10,10)
    vy = -5
    ballrect.x = 400
    ballrect.y = 450

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img,(320, 480))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

# 2.この下をずっとループする
while True:
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()