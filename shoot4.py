# 1.ゲームの準備をする
import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
## 自機データ
myimg = pg.image.load("images/myship.png")
myimg = pg.transform.scale(myimg, (50, 50))
myrect = pg.Rect(400, 500, 50, 50)
## 弾データ
bulletimg = pg.image.load("images/bullet.png")
bulletimg = pg.transform.scale(bulletimg, (16, 16))
bulletrect = pg.Rect(400, -100, 16, 16)
## UFOデータ
ufoimg = pg.image.load("images/UFO.png")
ufoimg = pg.transform.scale(ufoimg, (50, 50))
ufos = []
for i in range(10):
    ux = random.randint(0,800)
    uy = -100 * i
    ufos.append(pg.Rect(ux, uy, 50, 50))
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
        pg.mixer.Sound("sounds/pi.wav").play()
        if btn.collidepoint(mx, my) and pushFlag == False:
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

## ゲームステージ
def gamestage():
    # 3.画面を初期化する
    global page
    screen.fill(pg.Color("NAVY"))
    # 4.ユーザーからの入力を調べる
    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()
    # 5.絵を描いたり、判定したりする
    ## 自機の処理
    myrect.x = mx - 25
    screen.blit(myimg, myrect)
    ## 弾の処理
    if mdown[0] and bulletrect.y < 0: # 弾が画面外に出たら発射できる
        bulletrect.x = myrect.x + 25 - 8  # 弾の位置を自機の中心にする
        bulletrect.y = myrect.y - 16 # 弾の位置を自機の上にする
        pg.mixer.Sound("sounds/beam.wav").play() # 弾を発射する音
    if bulletrect.y >= 0: # 弾が画面内にあるとき
        bulletrect.y += -15 # 弾を上に動かす
        screen.blit(bulletimg, bulletrect) # 弾を描く
    ## UFOの処理
    for ufo in ufos:
        ufo.y += 10
        screen.blit(ufoimg, ufo)
        if ufo.y > 600:
            ufo.x = random.randint(0,800)
            ufo.y = -100
        ## 自機とUFOの衝突処理
        if ufo.colliderect(myrect):
            page = 2
            pg.mixer.Sound("sounds/down.wav").play()
        ## 弾とUFOの衝突処理
        if ufo.colliderect(bulletrect):
            ufo.y = -100
            ufo.x = random.randint(0,800)
            bulletrect.y = -100
            pg.mixer.Sound("sounds/piko.wav").play()

## データのリセット
def gamereset():
    myrect.x = 400
    myrect.y = 500
    bulletrect.y = -100
    for i in range(10):
        ufos[i] = pg.Rect(random.randint(0,800), -100 * i, 50, 50)

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

page = 1
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
