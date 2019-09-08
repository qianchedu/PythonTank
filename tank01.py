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
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR = pygame.Color(255,0,0)

class MainGame():
    window = None
    def __init__(self):
        pass

    #开始游戏
    def startGame(self):
        #加载主窗口
        #初始化窗口
        pygame.display.init()
        #设置窗体大小
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])


        #设置窗口的标题
        pygame.display.set_caption("我的世界1.0")
        while True:
            #给窗口背景设置填充色
            MainGame.window.fill(BG_COLOR)
            self.getEvent()
            #绘制文字
            MainGame.window.blit(self.getTextSuface('敌方坦克剩余数量%d'%6),(10,10))
            pygame.display.update()



    #结束游戏
    def endGame(self):
        print('谢谢使用')
        exit()

    def getTextSuface(self,text):
        #初始化字体模块
        pygame.font.init()
        #查看所有字体名称
        print(pygame.font.get_fonts())
        #获取字体Font对象
        font = pygame.font.SysFont('kaiti',18)
        textSurface = font.render(text,True,TEXT_COLOR)
        return textSurface



    #获取事件
    def getEvent(self):
        eventList = pygame.event.get()

        #遍历事件
        for event in eventList:
            #判断按下的按钮
            #如果按下的是退出，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()

            if event.type == pygame.KEYDOWN:
                #判断按下的是上、下、左、右
                if event.type == pygame.K_LEFT:
                    print('按下左键')

                elif event.type == pygame.K_RIGHT:
                    print('按下右键')

                elif event.type == pygame.K_UP:
                    print('按下上建')
                elif event.type == pygame.K_DOWN:
                    print('按下下减')






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


#爆炸效果
class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def displayExplode(self):
        pass


#音乐
class Music():
    def __init__(self):
        pass

    #播放音乐
    def play(self):
        pass



if __name__ == '__main__':
    MainGame().startGame()