# -*- coding:utf-8 -*-

from turtle import *

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

input()