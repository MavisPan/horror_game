from pygame import *
from random import randint
from time import time as timer
win_width = 1930
win_height = 1050
window = display.set_mode((win_width, win_height))
display.set_caption('My game')
background = transform.scale(image.load('winx.jpg'), (win_width, win_height))



'''mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
kick = mixer.Sound("fire.ogg")'''
FPS = 360
clock = time.Clock()
run = True
finish = False
font.init()
font1 = font.Font(None, 60)
t1 = font1.render("Ну, до завтра Сатания!", True, (255, 200, 10))
t2 = font1.render("ы", True, (255, 200, 10))
t3 = font1.render("б", True, (255, 200, 10))
t4 = font1.render(".ь", True, (255, 200, 10))
t5 = font1.render(".павп", True, (255, 200, 10))
t6 = font1.render(".вапв", True, (255, 200, 10))





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
        if e.type == MOUSEBUTTONDOWN:
            window.blit(t1, (200,200))
            display.update()
            clock.tick(FPS)
            if e.type == MOUSEBUTTONUP:
                break
            if e.type == MOUSEBUTTONDOWN:
                window.blit(background,(0,0))
                window.blit(t2, (200,200))
                display.update()
                clock.tick(FPS)
                if e.type == MOUSEBUTTONDOWN:
                    window.blit(t3, (200,200))
                    display.update()
                    clock.tick(FPS)
                    if e.type == MOUSEBUTTONDOWN:
                        window.blit(t4, (200,200))
                        display.update()
                        clock.tick(FPS)
                        if e.type == MOUSEBUTTONDOWN:
                            window.blit(t5, (200,200))
                            display.update()
                            clock.tick(FPS)
                            if e.type == MOUSEBUTTONDOWN:
                                window.blit(t6, (200,200))
                                display.update()
                                clock.tick(FPS)
                                finish = True
        '''player2.update_l()
        player2.reset()'''
        '''player.update()
        player.reset()'''
        '''ball.update()
        ball.reset()'''
    
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