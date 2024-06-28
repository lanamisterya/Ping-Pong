from random import*
from pygame import *
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y ,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
background = transform.scale(image.load('valentinstr.jpg'), (win_width, win_height))

run = True
finish = False
clock = time.Clock()
FPS = 60

player1 = Player('kinderbueno.png',0, win_height - 300,100,200,10)
player2 = Player('kinderbueno.png',600, win_height - 300,100,200,10)

ball = GameSprite('valentindyadka.png',350,250,100,100,3)

font.init()
font = font.SysFont("verdana", 40)
lose1 = font.render('PLAYER 1 LOSE', 1 , (255, 215, 0))
lose2 = font.render("PLAYER 2 LOSE", 1 , (180, 0, 0))

speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

                
    if finish != True:
        
        window.blit(background, (0, 0))       
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-100 or ball.rect.y < 0:
            speed_y *= -1
        
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))


    display.update()
    clock.tick(FPS)
