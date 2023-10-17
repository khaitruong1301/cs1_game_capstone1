import pygame
import sys
import random
pygame.init()
screen_width,screen_height = 1024,720
SCREEN = pygame.display.set_mode((screen_width,screen_height))
#Tạo background
bg_game = pygame.transform.scale(pygame.image.load("bg_game.jpg"),(1024,720))

#Tạo nhân vật game
shooter = pygame.transform.scale(pygame.image.load("shooter.png"),(90,75))
shooter_rect = shooter.get_rect()
shooter_rect.x = screen_width/2 - shooter_rect.width / 2 
shooter_rect.y = screen_height - shooter_rect.height  - 50

#Tạo bullet 
bullet  = pygame.transform.scale(pygame.image.load("bullet.png"),(100,150))
bullet_rect = bullet.get_rect()
bullet_rect.x = shooter_rect.x - 3
bullet_rect.y = shooter_rect.y - 100

#Tạo meteor
meteor = pygame.transform.scale(pygame.image.load("meteor.png"),(50,50)) 
meteor_rect = meteor.get_rect()
meteor_rect.x = random.randint(100, screen_width - meteor.get_width())
meteor_rect.y = 0
running = True

#Tạo các text điểm mạng 
font_game = pygame.font.Font("f_game.otf",24)
score = 0
score_title = font_game.render(f"Score: {score}",True,"Red","White")
score_x = 0
score_y = 0

live = 5
live_title = font_game.render(f"Live: {live}",True,"Red","White")
live_x = screen_width - live_title.get_width()
live_y = 0


while running:
    SCREEN.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        shooter_rect.x -= 1
    if keys[pygame.K_RIGHT]:
        shooter_rect.x += 1
    if keys[pygame.K_SPACE]: 
        bullet_rect.x = shooter_rect.x - 3
        bullet_rect.y = shooter_rect.y - 100
    bullet_rect.y -= 10

    #Thay đổi toạ độ y thiên thạch
    meteor_rect.y += 1

    if bullet_rect.colliderect(meteor_rect):
        meteor_rect.x = random.randint(100, screen_width - meteor.get_width())
        meteor_rect.y = 0
        score += 10
        score_title = font_game.render(f"Score: {score}",True,"Red","White")

    if meteor_rect.y == screen_height:
        live -= 1
        live_title = font_game.render(f"Live: {live}",True,"Red","White")
        meteor_rect.x = random.randint(100, screen_width - meteor.get_width())
        meteor_rect.y = 0
        
    if live == -1 :
        running = False

    #Load image rect
    SCREEN.blit(bg_game,(0,0))
    SCREEN.blit(shooter,(shooter_rect.x,shooter_rect.y))
    SCREEN.blit(bullet,(bullet_rect.x,bullet_rect.y))
    SCREEN.blit(meteor,(meteor_rect.x,meteor_rect.y))
    SCREEN.blit(score_title,(score_x,score_y))
    SCREEN.blit(live_title,(live_x,live_y))

    pygame.display.flip()
pygame.quit()
sys.exit()


