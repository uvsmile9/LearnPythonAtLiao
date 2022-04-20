#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def move(n, a, b, c,):
    step = 0
    if n == 1:
        print(step, a, '-->', c)
    else:
        move(n-1, a, c, b)  # 把最上面的n-1个盘子通过c移动到b
        move(1, a, b, c)  # 把最下面1个盘子经过b移到c
        move(n-1, b, a, c)  # 把b上面的n-1个盘子移到c
    return


move(3, 'a', 'b', 'c')
