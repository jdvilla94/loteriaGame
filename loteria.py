import pygame
from pygame.locals import *
import random
import loteriaDictionary
import time
import sys

pygame.init()

loteriaDictionary = {'El Gallo':'assets/elGallo.png','El diablito':'assets/elDiablito.png',
                     'La Dama':'assets/laDama.png','El Catrin':'assets/elCatrin.png','El Paraguas':'assets/elParaguas.png',
                     'La Sirena':'assets/laSirena.png','La Escalera':'assets/laEscalera.png','La Botella':'assets/laBotella.png',
                     'El Barril':'assets/elBarril.png','El Arbol ':'assets/elArbol.png','El Melon':'assets/elMelon.png'
                     }

loteriaDescList = ['El Gallo','El diablito',
                     'La Dama','El Catrin','El Paraguas',
                     'La Sirena','La Escalera','La Botella',
                     'El Barril','El Arbol ','El Melon']

loteriaImageList = ['assets/elGallo.png','assets/elDiablito.png',
                     'assets/laDama.png','assets/elCatrin.png','assets/elParaguas.png',
                    'assets/laSirena.png','assets/laEscalera.png','assets/laBotella.png',
                     'assets/elBarril.png','assets/elArbol.png','assets/elMelon.png',
                     
                     ]

newList = random.sample(loteriaImageList,len(loteriaImageList))

# print(random.sample(loteriaImageList,len(loteriaImageList)))

# for card,image in loteriaDictionary.items():
#     print(card,image)

#set dimensions for window
screenWidth = 800
screenHeight = 800

randY = random.randint(10,780)
randX = random.randint(10,780)

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
# currentCard = []

#card grid
cardGrid = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
            ]

# print(cardGrid)

# for x in range(6):
#     row = [0]*6#create a row list 
#     currentCard.append(row)

def drawText(text,font,textColor,x,y):
    img = font.render(text,True,textColor)
    screen.blit(img,(x,y))

def populateCard():
    
    row = 0
    while row < 4:
        column = 0
        # newList = random.sample(loteriaImageList,len(loteriaImageList))
        while column < 4:
            for index, image in enumerate(loteriaImageList):
                image = pygame.image.load(image)
                imageSize = (150,150)
                cardImage = pygame.transform.scale(image,imageSize)
                # cardText = font.render(str(card),True,'blue')
                # screen.blit(cardText,(column*195+33.5,row*195+30))
                screen.blit(cardImage,(column*195+33.5,row*195+30))
                column+=1
            row+=1
    #     # pygame.display.update()
    #     # time.sleep(.2) 


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
        pygame.draw.line(screen,grid,(10,x*195+10),(780,x*195+10),lineWidth)
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