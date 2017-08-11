#!/usr/bin/python  
# -*- coding: utf-8 -*-  
import pygame
import sys
import os
def chinese_to_pinyin(x):
    y = ''
    dic = {}
    with open("unicode_pinyin.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
        # print dic
    c=0
    for i in x:
        b = i
        i = str(i.encode('unicode_escape'))[2:].upper()
        
        
        try:
            y += dic[i] + ' '
            print b+"-"+i+"-"+dic[i]
            # c=c+1
            # file_base = u'录音 (%s).m4a'%c
            # print file_base
            # file_aim = '%s.m4a'%dic[i]
            # print file_aim
            # os.rename(file_base,file_aim)
            # print c
        except:
            y += 'XXXX '
    return y

def make_voice(x):
    pygame.mixer.init()
    voi = chinese_to_pinyin(x).split()
    for i in voi:
        if i == 'XXXX':
            continue
        pygame.mixer.music.load("voice/" + i + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
    return None

# while True:
print u"中文"
# p = u"我是夏力维 很高兴在这里哈"
# p = u"你们好 我是夏力维 很高兴在这里 认识大家 也不知道 说什么好 就先这样吧"
p = u"大家好 我是夏力维 很高兴认识大家在这里"
# print p
# print chinese_to_pinyin(p)
print make_voice(p)
    # make_vioce(p)