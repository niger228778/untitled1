import threading
import pygame
import sys
import random
import time

width = 11
height = 22
rectSizePx = 15

stopThread = False

boxColors = ((0,0,0), (255,0,0), (0,255,0), (0,0,255))

figures = (
    ((1,0),
     (1,0),
     (1,0),
     (1,0)),
    ((1,1),
     (1,1)),
    ((1,0),
     (1,0),
     (1,1))
)



pole = []
for _ in range(height):
    res = []
    for _ in range(width):
        res.append([0,False])
    pole.append(res)

pygame.init()

screen = pygame.display.set_mode((370,600))

def drawRect(x,y,color):
    global rectSizePx,screen
    rect = pygame.Rect(x,y,rectSizePx,rectSizePx)
    pygame.draw.rect(screen, color, rect)

def drawFirure(x_local, y_local, figure_type, isGravity=False):
    figure = figures[figure_type]
    color = random.randint(1, len(boxColors)-1)
    for y in range(len(figure)):
        for x in range(len(figure[y])):
            if figure[y][x] == 1:
                pole[y_local+y][x_local+x] = [color,isGravity]

def gravity():
    global pole
    while not stopThread:
        for y in range(len(pole) - 1, -1, -1):
            for x in range(len(pole[y])):
                if pole[y][x][1] and (y == len(pole) - 1 or (not (pole[y + 1][x][1]) and pole[y + 1][x][0] != 0)):
                    pole[y][x][1] = False
                if pole[y][x][1]:
                    pole[y + 1][x] = pole[y][x]
                    pole[y][x] = [0, False]
        time.sleep(0.5)

def draw_pole():
    global width, height, rectSizePx, screen, pole
    rect = pygame.Rect(28, 48, (width)*rectSizePx+4, (height)*rectSizePx+4)
    pygame.draw.rect(screen, (232, 232, 232), rect)
    rect = pygame.Rect(30, 50, (width) * rectSizePx, (height) * rectSizePx)
    pygame.draw.rect(screen, (0, 0, 0), rect)
    for y in range(len(pole)):
        for x in range(len(pole[y])):
            drawRect(30+x*rectSizePx, 50+y*rectSizePx, boxColors[pole[y][x][0]])
    pygame.display.flip()

gr = threading.Thread(target=gravity)
def startGame():
    global gr, stopThread
    drawFirure(4, 0, 1, True)
    while True:
        draw_pole()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    for y in range(0, len(pole)):
                        for x in range(len(pole[y])):
                            if pole[y][x][1] and (x > 0 and pole[y][x-1][0] == 0):
                                pole[y][x - 1] = pole[y][x]
                                pole[y][x] = [0, False]
            if event.type == pygame.QUIT:
                pygame.quit()
                stopThread = True
                sys.exit()

gr.start()
startGame()




