import pygame
import random

pygame.init()

ball_radius = 10
paddle_widht = 10
paddle_height = 100
ball_speed = 5
paddle_speed = 5

wIdth, heIght = 600, 800

win = pygame.display.set_mode((wIdth, heIght))
pygame.display.set_caption("Ping Pong")

font = pygame.font.SysFont("None", 30)

ball = pygame.Rect(wIdth // 2 - ball_radius // 2, heIght //2 - ball_radius // 2, ball_radius, ball_radius)
paddle1 = pygame.Rect(50, heIght // 2 - paddle_height // 2, paddle_widht, paddle_height)
paddle2 = pygame.Rect(wIdth - 50 - paddle_widht, heIght // 2 - paddle_height // 2, paddle_widht, paddle_height)

ball_speed_x = ball_speed * random.choice((1, -1))
ball_speed_y = ball_speed * random.choice((1, -1))

score1 = 0
score2 = 0

def collision():
    global ball_speed_x, ball_speed_y, score1, score2
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= heIght:
        ball_speed_y *= - 1
    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= wIdth:
        score1 += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (wIdth // 2, heIght // 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

def bot_control():
    if paddle1.centery < ball.centery:
        paddle1.y += paddle_speed
    elif paddle1.centery > ball.centery:
        paddle1.y -= paddle_speed

def main():
    global ball_speed_x, ball_speed_y, score1, score2

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False

        bot_control()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle2.top > 0:
            paddle2.y -= paddle_speed
        if keys[pygame.K_s] and paddle2.bottom < heIght:
            paddle2.y += paddle_speed

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        