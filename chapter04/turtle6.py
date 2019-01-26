# -*- coding:utf-8 -*-

from turtle import *

def branch(length):
    """
    長さを引数として受け取って枝を描く
    """
    if length < 10:
        return
    forward(length)
    left(30)
    branch(length/2)
    right(60)
    branch(length/2)
    left(30)
    forward(-length)

branch(200)

input()
