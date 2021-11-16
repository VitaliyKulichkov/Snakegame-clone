import pygame, sys
from random import randrange


RES = 1000
SIZE = 40

# set coordinates of a snake
x,y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
snake = [(x,y)]
dx, dy = 0, 0
#fps
fps = 10
#player score
score = 0


# initialize a game, screen , get fps, font of score and endgame$ loadin background image
pygame.init()
sc = pygame.display.set_mode([RES,RES])
clock = pygame.time.Clock()
pygame.display.set_caption('Snakegame')
# Font for score and endgame
font_score = pygame.font. SysFont('Times New Roman', 26, bold = True)
font_endgame = pygame.font. SysFont('Arial', 66, bold = True)
bg = pygame.image.load('1.jpg').convert()



while True:
    sc.blit(bg, (0,0))
    #drawing a snake and apllle
    [(pygame.draw.rect(sc,pygame.Color('green'), (i,j, SIZE - 2, SIZE - 2))) for i,j in snake]
    pygame.draw.rect(sc, pygame.Color('red'),(*apple, SIZE, SIZE))
    #show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('white'))
    sc.blit(render_score, (850, 5))
    #snake movemint
    x += dx*SIZE
    y += dy*SIZE
    snake.append((x,y))
    snake = snake[-length:]
    #eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1
        score += 1
    # gamev is over
    if x < 0 or x > RES + SIZE or y < 0 or y > RES + SIZE or len(snake) != len(set(snake)):
        while True:
            render_endgame = font_endgame.render('Game Over', 1, pygame.Color('white'))
            sc.blit(render_endgame, (RES // 2 - 125, RES // 3 + 50))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    #control /  "direction" dont let change direction to direction against
    direction = {'W': True, 'S': True, 'A': True, 'D': True}
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and direction['W']:
        dx, dy = 0, -1
        direction = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and direction['S']:
        dx, dy = 0, 1
        direction = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and direction['A']:
        dx, dy = -1, 0
        direction = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and direction['D']:
        dx, dy = 1, 0
        direction = {'W': True, 'S': True, 'A': False, 'D': True}


