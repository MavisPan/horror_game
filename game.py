from time import sleep
from pygame import *
from random import randint
from time import time as timer
from tkinter import *
'''root = Tk()'''

win_width = 1300
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('My game')
background = transform.scale(image.load('winx.jpg'), (win_width, win_height))

'''root.title("Окно")
root.geometry("300x250")
#
def btn_click(event):
    button1.config(state='disabled')   # Изменить сосотояние
    tex=Label(text="AAAAAA")
    tex.pack()
#
#
button1 = Button(text="Ок")'''


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
t1 = font1.render("Ну, до завтра Сатания!", True, (255, 200, 10))
t2 = font1.render("Увидимся", True, (0,0,0), (255,255,255))
t3 = font1.render("Наконец-то можно идти домой, но сначала...", True, (0,0,0), (255,255,255))
t4 = font1.render("Меня ждёт булочка!", True,(0,0,0), (255,255,255))
t5 = font1.render("Стоп... А что это за книга? И где моя булочка?!", True, (0,0,0), (255,255,255))
t6 = font1.render("Ч-ЧТО?!", True, (0,0,0), (255,255,255))
t7 = font1.render("Уфф... БУЛОЧКИ! Надо идти за ними!", True, (0,0,0), (255,255,255))





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
    '''def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed'''
    '''def fire(self):
        bullet = Bullet("Безымянный.png", self.rect.centerx, self.rect.top,  -5, 10, 20)
        bullets.add(bullet)'''

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

first = (255, 169, 146)
second = (0, 0, 0)
wall_1 = Wall(255, 255, 255, 200, 0, 30, 350)
wall_2 = Wall(255, 255, 255, 200, 150, 130, 10)
wall_3 = Wall(255, 255, 255, 420, 70, 30, 500)
wall_4 = Wall(255, 255, 255, 420, 180, 150, 10)
player = Player("satania.png", 0, 400, 7, 115, 130)
'''player2 = Player("klipartz.com.png", 680, 400, 2, 25, 150)
ball = GameSprite("pngwing.com.png", 250, 400, 1, 80, 80)'''
satania = GameSprite('pngwing.com.png', 200, 400, 2,200,400)
satania2 = GameSprite('pngwing(2).com.png', 200, 400, 2,200,400)
satania3 = GameSprite('pngwing(1).com.png', 200, 400, 2,200,400)
speed_x = 3
speed_y = 3

while run:  
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if finish != True:
        window.blit(background,(0,0))
        satania.update()
        satania.reset()

        if e.type == MOUSEBUTTONDOWN:
            window.blit(t1, (200,600))
            display.update()
            clock.tick(FPS)
            sleep(3)
            
            window.blit(background,(0,0))
            window.blit(t2, (200,600))
            display.update()
            clock.tick(FPS)
            sleep(3)
        
            window.blit(background,(0,0))
            window.blit(t3, (200,600))
            display.update()
            clock.tick(FPS)
            sleep(3)

            window.blit(background,(0,0))
            window.blit(t4, (200,600))
            display.update()
            clock.tick(FPS)
            sleep(3)

            window.blit(background,(0,0))
            window.blit(t5, (200,600))
            display.update()
            clock.tick(FPS)
            sleep(3)

            window.blit(background,(0,0))
            window.blit(t6, (200,600))
            display.update()
            clock.tick(FPS)
            sleep(3)

            window.blit(background,(0,0))
            window.blit(t7, (200,600))
            display.update()
            clock.tick(FPS)
            sleep(3)

        window.blit(background,(0,0))
        player.update()
        player.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()

        if sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4):
            finish = True
            window.blit(loose2, (200,200))
    
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