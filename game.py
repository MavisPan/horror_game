from time import sleep
from pygame import *
from random import randint
from time import time as timer
from tkinter import *
root = Tk()

win_width = 1300
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('My game')
background = transform.scale(image.load('winx.jpg'), (win_width, win_height))

root.title("Окно")
root.geometry("300x250")
#
def btn_click(event):
    button1.config(state='disabled')   # Изменить сосотояние
    tex=Label(text="AAAAAA")
    tex.pack()
#
#
button1 = Button(text="Ок")


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
t2 = font1.render("ы", True, (0,0,0), (255,255,255))
t3 = font1.render("б", True, (0,0,0), (255,255,255))
t4 = font1.render(".ь", True,(0,0,0), (255,255,255))
t5 = font1.render(".павп", True, (0,0,0), (255,255,255))
t6 = font1.render(".вапв", True, (0,0,0), (255,255,255))





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


first = (255, 169, 146)
second = (0, 0, 0)

player = Player("satania.png", 0, 400, 7, 115, 130)
'''player2 = Player("klipartz.com.png", 680, 400, 2, 25, 150)
ball = GameSprite("pngwing.com.png", 250, 400, 1, 80, 80)'''
satania = GameSprite('pngwing.com.png', 200, 400, 2,200,400)
speed_x = 3
speed_y = 3

while run:  
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if finish != True:
        '''ball.rect.x += speed_x
        ball.rect.y += speed_y'''
        window.blit(background,(0,0))
        satania.reset()
        satania.reset()
        if e.type == MOUSEBUTTONDOWN:
            window.blit(t1, (200,200))
            display.update()
            clock.tick(FPS)
            sleep(3)
            
        
            window.blit(background,(0,0))
            window.blit(t2, (200,200))
            display.update()
            clock.tick(FPS)
            sleep(3)
        
            window.blit(background,(0,0))
            window.blit(t3, (200,200))
            display.update()
            clock.tick(FPS)
            sleep(3)
            '''if e.type == MOUSEBUTTONDOWN:
                window.blit(t4, (200,200))
                window.blit(background,(0,0))
                display.update()
                clock.tick(FPS)
                sleep(5)
            if e.type == MOUSEBUTTONDOWN:
                window.blit(t5, (200,200))
                window.blit(background,(0,0))
                display.update()
                clock.tick(FPS)
                sleep(5)
            if e.type == MOUSEBUTTONDOWN:
                window.blit(t6, (200,200))
                window.blit(background,(0,0))
                display.update()
                clock.tick(FPS)
                sleep(5)'''
            window.blit(background,(0,0))
            player.update()
            player.reset()
    
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