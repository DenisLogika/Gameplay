import pygame
import random

pygame.init()

ball_radius = 10
paddle_width = 10
paddle_height = 100
ball_speed = 5
paddle_speed = 4

width, height = 800, 600

black = (0, 0, 0)
white = (255, 255, 255)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

font = pygame.font.SysFont("None", 30)

ball = pygame.Rect(width // 2 - ball_radius // 2, height // 2 - ball_radius // 2, ball_radius, ball_radius)
paddle1 = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

ball_speed_x = ball_speed * random.choice((1, -1))
ball_speed_y = ball_speed * random.choice((1, -1))

score1 = 0
score2 = 0

def collision():
    global ball_speed_x, ball_speed_y, score1, score2
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= width:
        score1 += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (width // 2, height // 2)
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
            if event.type == pygame.QUIT:
                run = False
            elif score1 >= 10:
                run = False
                print("You lose")
            elif score2 >= 10:
                run = False
                print("You win")

        bot_control()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle2.top > 0:
            paddle2.y -= paddle_speed
        if keys[pygame.K_s] and paddle2.bottom < height:
            paddle2.y += paddle_speed

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        collision()

        win.fill(black)

        pygame.draw.rect(win, white, paddle1)
        pygame.draw.rect(win, white, paddle2)
        pygame.draw.rect(win, white, ball)

        score_text = font.render(f"{score1} - {score2}", True, white)
        win.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()