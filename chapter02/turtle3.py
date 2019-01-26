# -*- coding:utf-8 -*-

from turtle import *

# 角度のリストを登録する
curve = [10, 160, 10, 20]
speed("fastest")

for i in range(40):
    forward(100)
    degree = curve[i % len(curve)]
    right(degree)

input()
