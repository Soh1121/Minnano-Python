# -*- coding:utf-8 -*-

year = int(input("西暦："))

if year == 1868:
    print("明治元年")
elif year < 1912:
    print("明治", year - 1867, "年")
elif year == 1912:
    print("大正元年")
elif year < 1926:
    print("大正", year - 1911, "年")
elif year == 1926:
    print("昭和元年")
elif year < 1989:
    print("大正", year - 1925, "年")
elif year == 1989:
    print("平成元年")
elif year < 2019:
    print("平成", year - 1988, "年")

input()

