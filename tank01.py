"""
1.坦克类(我方坦克、地方坦克)
 射击
 移动类
 显示坦克的方法

2.子弹类
 移动
 显示子弹的方法

3.墙壁类
 属性：是否可以通过

4.爆炸效果类
 展示爆炸效果

5.音效类
 播放音乐

6.主类

"""


class MainGame():
    def __init__(self):
        pass

    #开始游戏
    def startGame(self):
        pass


    #结束游戏
    def endGame(self):
        pass

#坦克类
class Tank():
    def __init__(self):
        pass

    #移动
    def move(self):
        pass


    #射击
    def shot(self):
        pass

    #显示坦克的方法
    def displayTank(self):
        pass



#我方坦克
class MyTank(Tank):
    def __init__(self):
        pass



#地方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass

#子弹类
class Bullet():
    def __init__(self):
        pass

    #移动
    def move(self):
        pass

    #展示子弹
    def displayBullet(self):
        pass

#墙壁
class Wall():
    def __init__(self):
        pass


    #显示墙壁
    def displayWall(self):
        pass


class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def displayExplode(self):
        pass


class Music():
    def __init__(self):
        pass

    def