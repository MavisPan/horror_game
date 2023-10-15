from time import sleep
from pygame import *
from random import randint
from time import time as timer
from tkinter import *


win_width = 1300
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('My game')
background = transform.scale(image.load('title.png'), (win_width, win_height))

'''mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
kick = mixer.Sound("fire.ogg")'''

FPS = 360
clock = time.Clock()
run = True
finish = False
font.init()
font1 = font.Font(None, 100)
font2 = font.Font(None, 30)
t = font2.render("Переключение диалога: f", True, (100,100,100))
t1 = font1.render("Ну, до завтра Сатания!", True, (255, 200, 10))
t2 = font1.render("Увидимся", True, (255, 200, 10))
t3 = font1.render("Наконец-то можно идти домой", True, (255, 200, 10))
t31 = font1.render("Yо сначала...", True, (255, 200, 10))
t4 = font1.render("Меня ждёт булочка!", True,(255, 200, 10))
t5 = font1.render("Стоп... А что это за книга?", True, (255,255,255))
t51 = font1.render("И где моя булочка?!", True, (255,255,255))
t6 = font1.render("Ч-ЧТО?!", True, (255,255,255))
t7 = font1.render("Уфф... БУЛОЧКИ! Надо идти за ними!", True, (255,255,255))
t8 = font1.render("Ну, наконец-то...", True, (255,255,255))
t9 = font1.render("Минутку...", True, (255,255,255))
t10 = font1.render("О НЕТ, СОБАКИ!", True, (255,255,255))





class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = "left"
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet("Безымянный.png", self.rect.centerx, self.rect.centery,  -5, 10, 20)
        bullets.add(bullet)

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global lost
        if self.rect.x <= 0:
            self.rect.x = 1000
            self.rect.y = randint(80, 620)
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 1000:
            self.kill()

first = (255, 169, 146)
second = (0, 0, 0)
wall_1 = Wall(148, 255, 248, 400, 0, 30, 350)
wall_2 = Wall(148, 255, 248, 400, 150, 130, 10)
wall_3 = Wall(148, 255, 248, 840, 70, 30, 500)
wall_4 = Wall(148, 255, 248, 840, 180, 150, 10)

player = Player("satania.png", 0, 400, 7, 115, 130)
satania = GameSprite('pngwing.com (1).png', 100, 350, 2, 250,400)
satania2 = GameSprite('pngwing.com (2).png', 60, 360, 2, 250,350)
satania3 = GameSprite('pngwing.com (3).png', 60, 400, 2,300,550)
satania4 = GameSprite('sat.png', 80, 380, 2,200,400)
toradora = GameSprite('tora.png', 100, 200, 2,500,600)
bun = GameSprite('bun.png', 1000, 300, 2, 100, 100)
exit1 = Enemy("exit.png",  0, 350, 2, 90, 65)
speed_x = 3
speed_y = 3
num = 1
gameStage = 0
loose = font1.render('WASTED', True, (255,0,0))
win = font1.render('To be continued...', True, (221, 127, 255))
monster = Enemy("bun.png", 0, randint(80, 620), 2, 90, 65)
'''monsters.add(monster)'''   
while run:    
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        if gameStage == 0:
            window.blit(background,(0,0))
            
            if e.type == KEYDOWN:
                if e.key == K_1:
                    gameStage += 1
        if gameStage == 1:
            background = transform.scale(image.load('back1.png'), (win_width, win_height))
            window.blit(background,(0,0))
            window.blit(t, (1000,30))
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1
                    sleep(1)
        if gameStage == 2:
            
            background = transform.scale(image.load('back.jpg'), (win_width, win_height))
            window.blit(background,(0,0))
            toradora.update()
            toradora.reset()
            window.blit(t1, (400,600))
            
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1
                    sleep(1)

        

        elif gameStage == 3:
            window.blit(background,(0,0))
            satania.update()
            satania.reset()
            window.blit(t2, (400,600))
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1
                    sleep(1)
                            
        elif gameStage == 4:
            window.blit(background,(0,0))
            
            satania2.update()
            satania2.reset()
            window.blit(t3, (200,600))
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1
                    sleep(1)
        
        elif gameStage == 5:
            window.blit(background,(0,0))
            
            satania2.update()
            satania2.reset()
            window.blit(t31, (200,600))
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1
                    sleep(1)

        elif gameStage == 6:
            window.blit(background,(0,0))
            
            satania3.update()
            satania3.reset()
            window.blit(t4, (200,600))
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1
                    sleep(1)

        elif gameStage == 7:
            background = transform.scale(image.load('book.jpg'), (win_width, win_height))
            window.blit(background,(0,0))
            window.blit(t5, (300,600))
            satania.update()
            satania.reset()
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1  
                    sleep(1)         

        elif gameStage == 8:
            window.blit(background,(0,0))
            window.blit(t51, (300,600))
            satania.update()
            satania.reset()
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1  
                    sleep(1)    

        elif gameStage == 9:
            background = transform.scale(image.load('winx.jpg'), (win_width, win_height))
            window.blit(background,(0,0))
            window.blit(t6, (350,600))
            satania4.update()
            satania4.reset()
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1  
                    sleep(1)             
        
        elif gameStage == 10:
            window.blit(background,(0,0))
            window.blit(t7, (100,600))
            satania3.update()
            satania3.reset()
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1  
                    sleep(1)   

        if gameStage == 11:
            window.blit(background,(0,0))
            player.update()
            player.reset()
            wall_1.draw_wall()
            wall_2.draw_wall()
            wall_3.draw_wall()
            wall_4.draw_wall()
            bun.update()
            bun.reset()
            
            if sprite.collide_rect(player, bun):
                window.blit(win, (200,200))          
                finish = True  
            if sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4):
                background = transform.scale(image.load('dog.gif'), (win_width, win_height))
                window.blit(background,(0,0))
                window.blit(loose, (550,500))
                finish = True
            
        '''if gameStage == 11:
            window.blit(background,(0,0))
            window.blit(t8, (100,600))
            satania2.update()
            satania2.reset()
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1  
                    sleep(1)   

        if gameStage == 12:
            window.blit(background,(0,0))
            window.blit(t9, (100,600))
            satania4.update()
            satania4.reset()
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1  
                    sleep(1)   

        if gameStage == 13:
            window.blit(background,(0,0))
            window.blit(t10, (100,600))
            satania4.update()
            satania4.reset()
            if e.type == KEYDOWN:
                if e.key == K_f:
                    gameStage += 1  
                    sleep(1)   

        if gameStage == 10:
            window.blit(background,(0,0))
            player.update()
            player.reset()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:                   
                    player.fire()
            if score >= 3:
                exit1.update()
                exit1.reset()
            if sprite.collide_rect(player, exit1):
                window.blit(win, (200,200))     
                finish = True  
            if sprite.collide_rect(player, wall_5) or sprite.collide_rect(player, wall_6) or sprite.collide_rect(player, wall_7) or sprite.collide_rect(player, wall_8):
                background = transform.scale(image.load('dog.gif'), (win_width, win_height))
                window.blit(background,(0,0))
                window.blit(loose, (550,500))
                finish = True'''
    '''if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

    if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1


    if ball.rect.x < 0:
        finish = True
        window.blit(loose, (200,200))
    
    if ball.rect.x > 630:
        finish = True
        window.blit(loose2, (200,200))'''
    
   
    display.update()
    clock.tick(FPS)