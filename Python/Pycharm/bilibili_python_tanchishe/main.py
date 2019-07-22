#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''实现步骤
1.定义颜色变量
2.定义游戏结束函数
3.定义main函数
3.1初始化pygame
3.2定义一个变量控制速度
3.3创建pygame显示层
3.4初始化变量
初始化贪吃蛇的起始位置
初始化吃蛇长度
初始化目标位置
初始化目标方块的标记：判断是否被吃了
定义方向变量并初始化方向
3.5 pygame的所有事件都放在实时循环中完成
3.6确定方向
3.7根据方向 改变蛇头
3.8增加蛇的长度
3.9判断及改变目标状态
3.10填充背景颜色
3.11画蛇和目标
4 更新显示到屏幕表面
5 启动入口函数
'''

import pygame #游戏库
import sys #控制系统
import random

from pygame.locals import *

#1.定义颜色变量
redColor=pygame.Color(255,0,0)#R,G,B 目标红色
blackColor=pygame.Color(0,0,0)#背景黑色
whiteColor=pygame.Color(255,255,255)#蛇白色

#2.游戏结束函数
def gameOver():
    pygame.quit()
    sys.exit()

#3.main函数
def main():
    pygame.init()#3.1初始化pygame 导入的模块

    fpsClock=pygame.time.Clock()#3.2定义速度变量,clock对象，提供了控制游戏帧速的函数

    playSurface=pygame.display.set_mode((640,480))#3.3创建pygame显示层,窗口大小640，480

    pygame.display.set_caption('贪吃蛇')#界面标题

    snakePosition=[100,100]#初始化蛇的坐标为[100,100]

    #初始化社身体长度，以食物大小为基准[20,20]，列表中元素个数，表示蛇身大小
    snakeBody=[[100,100],[80,100],[60,100]]

    targetPosition=[300,300]#初始化目标位置

    targetflag=1#目标的状态 1表示吃掉，0表示未吃掉

    direction='right'#初始化方向，向右

    #定义控制方向变量(键盘方向键)
    changedirection=direction
    print(QUIT,KEYDOWN)
    while True:#遍历事件

        for event in pygame.event.get():#该方法从队列中获取事件

            print(str(event.type))

            if event.type==QUIT:

                pygame.quit()

                sys.exit()

            elif event.type==KEYDOWN:

                if event.key==K_RIGHT:

                    changedirection='right'

                if event.key==K_LEFT:

                    changedirection='left'

                if event.key==K_UP:

                    changedirection='up'

                if event.key==K_DOWN:

                    changedirection='down'

                if event.key==K_ESCAPE:

                    pygame.event.post(pygame.event.Event(QUIT))

        #确定方向
        if changedirection=='left' and not direction=='right':
            direction=changedirection

        if changedirection == 'right' and not direction == 'left':
            direction = changedirection

        if changedirection == 'up' and not direction == 'down':
            direction = changedirection

        if changedirection == 'down' and not direction == 'up':
            direction = changedirection

        #根据方向改变蛇头
        if direction=='right':
            snakePosition[0]+=20

        if direction=='left':
            snakePosition[0]-=20

        if direction=='up':
            snakePosition[1]-=20

        if direction=='down':
            snakePosition[1]+=20

        #增加蛇的长度
        snakeBody.insert(0,list(snakePosition))

        if snakePosition[0]==targetPosition[0] and snakePosition[1]==targetPosition[1]:
            targetflag=0
        else:
            snakeBody.pop()

        if targetflag==0:
            x=random.randrange(1,32)
            y=random.randrange(1,24)
            targetPosition=[int(x*20),int(y*20)]
            targetflag=1

        #填充背景颜色
        playSurface.fill(blackColor)

        #画蛇和目标
        for position in snakeBody:
            pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],20,20))
            #第三个参数:返回一个矩形((x,y),(width,height))
            #第四个参数：线条的粗细，0表示填充
        pygame.draw.rect(playSurface,redColor,Rect(targetPosition[0],targetPosition[1],20,20))

        #更新显示到屏幕表面
        pygame.display.flip()

        if snakePosition[0]>620 or snakePosition [0]<0:
            gameOver()
        elif snakePosition[1]>460 or snakePosition[1]<0:
            gameOver()

        #控制游戏速度
        fpsClock.tick(3)#3秒

#启动main
if __name__=='__main__':
    main()