# -*- coding:utf-8 -*-

from turtle import *

speed('fastest')

for i in range(40):
    forward(100)
    if i % 4 == 1:
        right(160)
    elif i % 4 == 3:
        right(20)
    else:
        right(10)

input()
