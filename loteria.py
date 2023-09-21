import pygame
from pygame.locals import *
import random
import loteriaDictionary

pygame.init()

loteriaDictionary = {'El Gallo':'assets/elGallo.png','El diablito':'assets/elDiablito.png',
                     'La Dama':'assets/laDama.png'
                     }

# for card,image in loteriaDictionary.items():
#     print(card,image)

#set dimensions for window
screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Loteria')


#game variables
gameStart = False

#define Fonts
font = pygame.font.SysFont('arialBlack',40)

#define colors
textColor = 'white'

#define variables
lineWidth = 5
player = 1
currentCard = []

for x in range(6):
    row = [0]*6#create a row list 
    currentCard.append(row)

def drawText(text,font,textColor,x,y):
    img = font.render(text,True,textColor)
    screen.blit(img,(x,y))

def populateCard():
    xPos = 0
    for x in range(4):
        for card,image in loteriaDictionary.items():
            yPos = 0
                # print(card,image)
            image = pygame.image.load(image)
            imageSize = (200,200)
            cardImage = pygame.transform.scale(image,imageSize)
            cardText = font.render(card,True,'blue')
            screen.blit(cardImage,(xPos*200,yPos*200))
            yPos +=1
        xPos +=1
    # print(xPos,yPos)


def drawGameGrid():
    background = 'black'
    grid = 'white'
    screen.fill(background)
    for x in range(1,4):
        pygame.draw.line(screen,grid,(0,x*200),(screenWidth,x*200),lineWidth)
        pygame.draw.line(screen,grid,(x*200,0),(x*200,screenHeight),lineWidth)



running = True
while running:
    #draw board
    # drawGameGrid()
    if gameStart == True:
        drawGameGrid()
        populateCard()
    else:
        drawText('Press space to pause',font,textColor,160,250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameStart = True
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()