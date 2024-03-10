import pygame as pg
a = pg.Rect(10,20,30,40)
print("X,Y=",a.x, a.y,"幅,高さ=",a.width, a.height)
a.x = a.x + 1
print("X,Y=",a.x, a.y,"幅,高さ=",a.width, a.height)