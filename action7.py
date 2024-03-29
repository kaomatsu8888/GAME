# 1.ゲームの準備をする
import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600)) # 画面の大きさ
## プレイヤーデータ
myimgR = pg.image.load("images/playerR.png")
myimgR = pg.transform.scale(myimgR, (40, 50)) # 画像の大きさ
myimgL = pg.transform.flip(myimgR, True, False) # 左向きの画像
myrect = pg.Rect(50,200,40,50) # 位置と大きさ
## 壁データ
walls = [pg.Rect(0,0,800,20),
        pg.Rect(0,0,20,600),
        pg.Rect(780,0,20,600),
        pg.Rect(0,580,800,20)]
## ワナデータ
trapimg = pg.image.load("images/uni.png")
trapimg = pg.transform.scale(trapimg, (30, 30))
traps = []
for i in range(20):
    wx = 150 + i * 30
    wy = random.randint(20,550)
    traps.append(pg.Rect(wx,wy,30,30))
## ボタンデータ
replay_img = pg.image.load("images/replaybtn.png")
goalrect = pg.Rect(750,250,30,100)
## オバケデータ
enemyimgR = pg.image.load("images/obake.png")
enemyimgR = pg.transform.scale(enemyimgR, (50, 50))
enemyimgL = pg.transform.flip(enemyimgR, True, False) # 左向きの画像.flip(左右, 上下)
enemyrect = pg.Rect(650,200,50,50) # 位置と大きさ
## メインループで使う変数
rightFlag = True
pushFlag = False
page = 1

## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag # グローバル変数を使う
    # 4.ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed() # マウスのボタンが押されたかどうか
    (mx, my) = pg.mouse.get_pos() # マウスの位置
    if mdown[0]: # 左ボタンが押されたら
        if btn.collidepoint(mx, my) and pushFlag == False: # ボタンの上にマウスがあるか
            pg.mixer.Sound("sounds/pi.wav").play() # 効果音を鳴らす
            page = newpage # ページを移動する
            pushFlag = True
    else:
        pushFlag = False

## ゲームステージ
def gamestage():
    # 3.画面を初期化する
    global rightFlag # グローバル変数を使う
    global page # グローバル変数を使う
    screen.fill(pg.Color("DEEPSKYBLUE")) # 背景色
    vx = 0
    vy = 0
    # 4.ユーザーからの入力を調べる
    key = pg.key.get_pressed()
    # 5.絵を描いたり、判定したりする
    if key[pg.K_RIGHT]:
        vx = 4
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -4
        rightFlag = False
    if key[pg.K_UP]:
        vy = -4
    if key[pg.K_DOWN]:
        vy = 4
    ## プレイヤーの処理
    myrect.x += vx # x座標を変化させる
    myrect.y += vy
    if myrect.collidelist(walls) != -1:
        myrect.x -= vx
        myrect.y -= vy
    if rightFlag:
        screen.blit(myimgR, myrect)
    else :
        screen.blit(myimgL, myrect)
    ## 壁の処理
    for wall in walls:
        pg.draw.rect(screen, pg.Color("DARKGREEN"), wall)
    ## ワナの処理
    for trap in traps:
        screen.blit(trapimg, trap)
    if myrect.collidelist(traps) != -1: # ワナに触れたら
        pg.mixer.Sound("sounds/down.wav").play() # 効果音を鳴らす
        page = 2 # ゲームオーバー
    ## ゴールの処理
    pg.draw.rect(screen, pg.Color("GOLD"), goalrect) # ゴールの描画
    if myrect.colliderect(goalrect): # ゴールに触れたら
        pg.mixer.Sound("sounds/up.wav").play() # 効果音を鳴らす
        page = 3 # ゲームクリア
    ## オバケの処理
    ovx = 0 # オバケの速度
    ovy = 0
    if enemyrect.x < myrect.x : # プレイヤーの方向を調べる
        ovx = 1 # オバケの速度を設定する
    else :
        ovx = -1 # オバケの速度
    if enemyrect.y < myrect.y : # プレイヤーの方向を調べる
        ovy = 1 # オバケの速度を設定する
    else : # プレイヤーの方向を調べる
        ovy = -1 # オバケの速度を設定する
    enemyrect.x += ovx # オバケの位置を変化させる
    enemyrect.y += ovy
    if ovx > 0 : # オバケの向きを調べる
        screen.blit(enemyimgR, enemyrect) # オバケの描画
    else : # オバケの向きを調べる
        screen.blit(enemyimgL, enemyrect) # オバケの描画
    if myrect.colliderect(enemyrect): # オバケに触れたら
        pg.mixer.Sound("sounds/down.wav").play() # 効果音を鳴らす
        page = 2

## データのリセット
def gamereset() :
    myrect.x = 50
    myrect.y = 100
    for d in range(20):
        traps[d].x = 150 + d * 30
        traps[d].y = random.randint(20,550)
    enemyrect.x = 650
    enemyrect.y = 200

# ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img,(320, 480))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

# ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img,(320, 480))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

# 2.この下をずっとループする
while True:
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    elif page == 3:
        gameclear()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
