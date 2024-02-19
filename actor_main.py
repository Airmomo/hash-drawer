#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 11:27
# @Author  : airmomo
# @File    : actor_main.py
# @Software: PyCharm
# @Desc    : 
# @Remark  : 
# @Target profile:

import matplotlib.pyplot as plt
import numpy as np
import hashlib


def hash_actor(username):
    # 随机创建像素数据
    userid = username
    userid_hashcode = hashlib.md5(userid.encode(encoding='UTF-8')).hexdigest()
    userid_hashcode_list = list(userid_hashcode)
    userid_hashcode_color_rgb = ((ord(userid_hashcode_list[0]) * 16 + ord(userid_hashcode_list[2])) % 255 / 255,
                                 (ord(userid_hashcode_list[4]) * 16 + ord(userid_hashcode_list[8])) % 255 / 255,
                                 (ord(userid_hashcode_list[12]) * 16 + ord(userid_hashcode_list[24])) % 255 / 255)
    print(userid_hashcode_color_rgb)
    pixels = np.ones(75).reshape((5, 5, 3))
    for x in range(0, 5):
        for y in range(0, 5):
            symbol = ord(userid_hashcode_list[(x + 1) * (y + 1)]) % 2 == 0
            if symbol:
                pixels[x][y] = (1, 1, 1)
            else:
                pixels[x][y] = userid_hashcode_color_rgb
    # 绘制像素图
    plt.figure(figsize=(5, 5))
    plt.imshow(pixels)
    plt.axis("off")
    plt.margins(0, 0)
    plt.savefig("./image.png", format=None, metadata=None, bbox_inches=None, pad_inches=0)


if __name__ == '__main__':
    custom_input="Airmomo"
    hash_actor(custom_input)