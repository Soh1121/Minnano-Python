from turtle import *

def branch(length):
    """
    長さを引数として受け取って枝を描く
    """
    if length < 10:
        return
    forward(length)     # length分前進
    left(30)            # 30度左に回転
    branch(length/2)    # 左の枝を再帰的に描く
    right(60)           # 60度右に回転
    branch(length/2)    # 右の枝を再帰的に描く
    left(30)            # 30度左に回転
    forward(-length)    # length分戻る

branch(200)

input()
