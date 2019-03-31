from turtle import *

speed('fastest')

for i in range(40):     # 60回繰り返す
    forward(100)        # 10進む
    if i % 4 == 1:
        right(160)
    elif i % 4 == 3:
        right(20)
    else:
        right(10)

input()
