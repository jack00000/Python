# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import time
import random

"""
1. 搭建游戏界面，主要是完成窗口和背景图的显示
2. 通过键盘操作，获取游戏事件
3. 在游戏窗口显示飞机，并实现按左右键控制飞机左右移动
4. 实现按空格键飞机发射子弹
5. 显示敌人飞机
6. 优化敌机发射的子弹
7. 让敌机移动
8. 敌机发射子弹
9. 玩家子弹射中敌机，敌机爆炸
"""


# 创建飞机基类
class Plane(object):
    def __init__(self, x, y, screen):
        # 设置飞机的默认位置
        self.x = x
        self.y = y
        # 设置要显示内容的窗口
        self.screen = screen
        # 用来存储飞机发射的子弹
        self.bullet_list = []


# 创建英雄飞机类
class HeroPlane(Plane):
    def __init__(self, x, y, screen):
        # 继承父类的init方法
        super(HeroPlane, self).__init__(x, y, screen)
        self.image = pygame.image.load('image/fj5.png')

        self.image_boom_list = []
        self.image_boom_list.append(pygame.image.load('image/hero_blowup_n1.png'))
        self.image_boom_list.append(pygame.image.load('image/hero_blowup_n2.png'))
        self.image_boom_list.append(pygame.image.load('image/hero_blowup_n3.png'))
        self.image_boom_list.append(pygame.image.load('image/hero_blowup_n4.png'))
        # 用于判断敌机是否爆炸
        self.boom = False
        # 选取敌机爆炸的图片索引
        self.image_boom_index = 0
        # 爆炸图片切换的间隔

        self.num = 1
        self.left = False
        self.right = False
        self.up = False
        self.down = False


    def display(self):
        if self.left:
            self.x -= 3
            if self.x < -20:
                self.left = False
                self.right = True
                self.up = False
                self.down = False

        if self.right:
            self.x += 3
            if self.x > 300:
                self.left = True
                self.right = False
                self.up = False
                self.down = False

        if self.up:
            self.y -= 3
            if self.y < 0:
                self.left = False
                self.right = False
                self.up = False
                self.down = True

        if self.down:
            self.y += 3
            if self.y > 600:
                self.left = False
                self.right = False
                self.up = True
                self.down = False


        if not self.boom:
            self.screen.blit(self.image, (self.x, self.y))

            # 如果子弹越界，先将子弹对象从列表中删除
            for bullet in self.bullet_list:
                if bullet.judge():
                    self.bullet_list.remove(bullet)

            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
        else:
            if self.image_boom_index < len(self.image_boom_list):
                if self.num % 5 == 0:
                    self.screen.blit(self.image_boom_list[self.image_boom_index], (self.x, self.y))
                    self.image_boom_index += 1
                self.num += 1

    def move_left(self):
            self.left = True
            self.right = False
            self.up = False
            self.down = False

    def move_right(self):
            self.right = True
            self.left = False
            self.up = False
            self.down = False

    def move_up(self):
            self.right = False
            self.left = False
            self.up = True
            self.down = False

    def move_down(self):
            self.right = False
            self.left = False
            self.up = False
            self.down = True

    def stop(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def shoot(self):
        bullet = Bullet(self.x, self.y, self.screen)
        self.bullet_list.append(bullet)

    def shoot_by(self, bullet):
        x1 = self.x + self.image.get_rect().width
        y1 = self.y + self.image.get_rect().height
        if bullet.x < x1 and bullet.x > self.x and bullet.y < y1 and bullet.y > self.y:
            return True
        else:
            return False


# 创建子弹类
class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 50
        self.y = y - 40
        self.screen = screen
        self.image = pygame.image.load('image/zd10.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 修改子弹的位置，在窗口显示为动态的移动
    def move(self):
        self.y -= 4

    # 判断子弹是否越界
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

    def shoot_by(self, bullet):
        x1 = self.x + self.image.get_rect().width
        y1 = self.y + self.image.get_rect().height
        if bullet.x < x1 and bullet.x > self.x and bullet.y < y1 and bullet.y > self.y:
            return True
        else:
            return False


# 创建敌人飞机类
class EnemyPlane(Plane):
    def __init__(self, x, y, screen):
        super(EnemyPlane, self).__init__(x, y, screen)
        self.image = pygame.image.load('image/fj3.png')
        # 将敌机爆炸图片放入到列表，动态显示爆炸效果
        self.image_boom_list = []
        self.image_boom_list.append(pygame.image.load('image/enemy0_down1.png'))
        self.image_boom_list.append(pygame.image.load('image/enemy0_down2.png'))
        self.image_boom_list.append(pygame.image.load('image/enemy0_down3.png'))
        self.image_boom_list.append(pygame.image.load('image/enemy0_down4.png'))
        # 存储敌机发射的子弹
        self.bullet_list = []
        # 指定敌机开始的飞行方向
        self.direction = 'right'
        # 用于判断敌机是否爆炸
        self.boom = False
        # 选取敌机爆炸的图片索引
        self.image_boom_index = 0
        # 爆炸图片切换的间隔
        self.num = 1

    def display(self):
        if not self.boom:
            self.screen.blit(self.image, (self.x, self.y))

            for bullet in self.bullet_list:
                if bullet.judge():
                    self.bullet_list.remove(bullet)

            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
            self.move()
            self.shoot()
        else:
            if self.image_boom_index < len(self.image_boom_list):
                if self.num % 5 == 0:
                    self.screen.blit(self.image_boom_list[self.image_boom_index], (self.x, self.y))
                    self.image_boom_index += 1
                self.num += 1

    def move(self):
        # 如果方向是向右，就往右走
        if self.direction == 'right':
            self.x += 2
        # 如果方向是向左，就往左走
        if self.direction == 'left':
            self.x -= 2
        # 如果到达右边的边界，则向左走
        if self.x > 350:
            self.direction = 'left'
        # 如果到达左边的边界，则向右走
        if self.x < 0:
            self.direction = 'right'
        self.y += 1

    # 敌机发射子弹，在1-75个整数中，随机取数字，只有数字为25才发射子弹
    def shoot(self):
        num = random.randint(1, 75)
        if num == 25:
            bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(bullet)

    # 检查敌机是否被子弹bullet (x, y)击中
    def shoot_by(self, bullet):
        x1 = self.x + self.image.get_rect().width
        y1 = self.y + self.image.get_rect().height
        if bullet.x < x1 and bullet.x > self.x and bullet.y < y1 and bullet.y > self.y:
            return True
        else:
            return False


class SEnemyPlane(Plane):
    def __init__(self, x, y, screen):
        super(SEnemyPlane, self).__init__(x, y, screen)
        self.image = pygame.image.load('image/fj6.png')
        # 将敌机爆炸图片放入到列表，动态显示爆炸效果
        self.image_boom_list = []
        self.image_boom_list.append(pygame.image.load('image/enemy1_down1.png'))
        self.image_boom_list.append(pygame.image.load('image/enemy1_down2.png'))
        self.image_boom_list.append(pygame.image.load('image/enemy1_down3.png'))
        self.image_boom_list.append(pygame.image.load('image/enemy1_down4.png'))
        # 存储敌机发射的子弹
        self.bullet_list = []
        # 指定敌机开始的飞行方向
        self.direction = 'right'
        # 用于判断敌机是否爆炸
        self.boom = False
        # 选取敌机爆炸的图片索引
        self.image_boom_index = 0
        # 爆炸图片切换的间隔
        self.num = 1

    def display(self):
        if not self.boom:
            self.screen.blit(self.image, (self.x, self.y))

            for bullet in self.bullet_list:
                if bullet.judge():
                    self.bullet_list.remove(bullet)

            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
            self.move()
            self.shoot()
        else:
            if self.image_boom_index < len(self.image_boom_list):
                if self.num % 5 == 0:
                    self.screen.blit(self.image_boom_list[self.image_boom_index], (self.x, self.y))
                    self.image_boom_index += 1
                self.num += 1

    def move(self):
        # 如果方向是向右，就往右走
        if self.direction == 'right':
            self.x += 2
        # 如果方向是向左，就往左走
        if self.direction == 'left':
            self.x -= 2
        # 如果到达右边的边界，则向左走
        if self.x > 350:
            self.direction = 'left'
        # 如果到达左边的边界，则向右走
        if self.x < 0:
            self.direction = 'right'
        self.y += 1

    # 敌机发射子弹，在1-75个整数中，随机取数字，只有数字为25才发射子弹
    def shoot(self):
        num = random.randint(1, 100)
        if num == 25:
            bullet = SEnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(bullet)

    # 检查敌机是否被子弹bullet (x, y)击中
    def shoot_by(self, bullet):
        x1 = self.x + self.image.get_rect().width
        y1 = self.y + self.image.get_rect().height
        if bullet.x < x1 and bullet.x > self.x and bullet.y < y1 and bullet.y > self.y:
            return True
        else:
            return False


class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 30
        self.y = y + 60
        self.screen = screen
        self.image = pygame.image.load('image/zd7.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 2

    def judge(self):
        if self.y > 700:
            return True
        else:
            return False

class SEnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 30
        self.y = y + 60
        self.screen = screen
        self.image = pygame.image.load('image/zd8.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 3

    def judge(self):
        if self.y > 700:
            return True
        else:
            return False


enemy_plane_list = []


def add_enemy_plane(screen):
    num = random.randint(0, 500)
    x = random.randrange(0, 395, 50)
    if num < 3:
        enemy_plane = EnemyPlane(x, 0, screen)
        enemy_plane_list.append(enemy_plane)
    if num == 4:
        enemy_plane = SEnemyPlane(x, 0, screen)
        enemy_plane_list.append(enemy_plane)
    return enemy_plane_list


def remove_enemy_plane(screen):
    for enemy_plane in enemy_plane_list:
        if enemy_plane.y > 700:
            enemy_plane_list.remove(enemy_plane)


class SB(pygame.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 700:
            self.rect.y = -700


if __name__ == '__main__':
    # 创建一个windows窗口用来显示游戏内容
    screen = pygame.display.set_mode((395, 700))
    pygame.display.set_caption('雷电2018')

    groups_bg = pygame.sprite.Group()
    bg = SB('image/bj2.jpg')
    bg1 = SB('image/bj2.jpg')
    bg1.rect.y = -700
    groups_bg.add(bg,bg1)



    # 创建一个飞机对象
    hero_plane = HeroPlane(145, 550, screen)

    # 创建一个敌机对象
    enemy_plane = EnemyPlane(0, 0, screen)

    while True:

        groups_bg.update()
        groups_bg.draw(screen)



        # 将飞机对象放到背景图像上显示
        hero_plane.display()

        enemy_plane_list = add_enemy_plane(screen)

        # 遍历所有英雄飞机发射的子弹，判断是否能射中敌机

        for bullet in hero_plane.bullet_list:
            for enemy_plane in enemy_plane_list:
                if enemy_plane.shoot_by(bullet):
                    enemy_plane.boom = True

        for enemy_plane in enemy_plane_list:
            for bullet in enemy_plane.bullet_list:
                if hero_plane.shoot_by(bullet):
                    hero_plane.boom = True
        if hero_plane.boom == True:
            gameover = pygame.image.load('image/gameover.jpg')
            screen.blit(gameover, (50, 300))


        for enemy_plane in enemy_plane_list:
            enemy_plane.display()

        remove_enemy_plane(screen)

        # 通过键盘获取游戏事件
        for event in pygame.event.get():
            # 如果点击了退出按钮，则退出游戏
            if event.type == QUIT:
                print('exit')
                exit()

            # 判断键盘是否按下了键
            elif event.type == KEYDOWN:
                # 如果按键是a或者是<-键，则控制飞机向左移动
                if event.key == K_a or event.key == K_LEFT:
                    hero_plane.move_left()
                    print('left')
                if event.key == K_w or event.key == K_UP:
                    hero_plane.move_up()
                    print('up')
                if event.key == K_s or event.key == K_DOWN:
                    hero_plane.move_down()
                    print('down')
                # 如果按键是d或者是->键，则控制飞机向右移动
                elif event.key == K_d or event.key == K_RIGHT:
                    hero_plane.move_right()
                    print('right')
                # 如果按键是Esc则停止移动
                elif event.key == K_ESCAPE:
                    hero_plane.stop()
                # 如果按键是空格键，则飞机发射子弹
                elif event.key == K_SPACE:
                    hero_plane.shoot()
                    print('space')

        # 通过延迟的方式，来降低while循环的循环速度，从而降低cpu占用率
        time.sleep(0.01)

        # 更新需要显示的内容
        pygame.display.update()