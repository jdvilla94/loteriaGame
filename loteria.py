import pygame
from pygame.locals import *
import random
import loteriaDictionary

pygame.init()

loteriaDictionary = {'El Gallo':'assets/elGallo.png','El diablito':'assets/elDiablito.png',
                     'La Dama':'assets/laDama.png','El Catrin':'assets/elCatrin.png','El Paraguas':'assets/elParaguas.png',
                     'La Sirena':'assets/laSirena.png'
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
lineWidth = 10
player = 1
currentCard = []

#card grid
cardGrid = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
            ]

for x in range(6):
    row = [0]*6#create a row list 
    currentCard.append(row)

def drawText(text,font,textColor,x,y):
    img = font.render(text,True,textColor)
    screen.blit(img,(x,y))

def populateCard():
    row = 0 
    while row < 9:
        column = 0
        while column < 9:
            for card,image in loteriaDictionary.items():
            # yPos = 0
                image = pygame.image.load(image)
                imageSize = (150,150)
                cardImage = pygame.transform.scale(image,imageSize)
                cardText = font.render(card,True,'blue')
                screen.blit(cardImage,(column*195+33.5,row*195+30))
                column+=1
                # row+=1
                # print(card,cardImage)
        row+=1
    # xPos = 0
    # for x in range(4):
    #     print('the x value is',x)
    #     for card,image in loteriaDictionary.items():
    #         yPos = 0
    #             # print(card,image)
    #         image = pygame.image.load(image)
    #         imageSize = (150,150)
    #         cardImage = pygame.transform.scale(image,imageSize)
    #         cardText = font.render(card,True,'blue')
    #         screen.blit(cardImage,(xPos*195+33.5,yPos*195+30))
    #         yPos +=1
    #     xPos +=1
    # print(xPos,yPos)


def drawGameGrid():
    background = 'black'
    grid = 'white'
    screen.fill(background)
    pygame.draw.rect(screen,pygame.Color('white'),pygame.Rect(10,10,780,780),10)
    # i = 1
    # while (i*200) < 770:
    #     pygame.draw.line(screen,pygame.Color('white'),pygame.Vector2((i*200)+15,15),pygame.Vector2((i*80)+15,785),3)
    #     i+=1


    for x in range(1,4):
        pygame.draw.line(screen,grid,(10,x*195),(780,x*195),lineWidth)
        pygame.draw.line(screen,grid,(x*195+10,10),(x*195+10,780),lineWidth)



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