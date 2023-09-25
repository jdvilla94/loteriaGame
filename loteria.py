import pygame
from pygame.locals import *
import random
import loteriaDictionary
import time
import sys

pygame.init()

loteriaImageList = ['assets/elGallo.png','assets/elDiablito.png',
                     'assets/laDama.png','assets/elCatrin.png','assets/elParaguas.png',
                    'assets/laSirena.png','assets/laEscalera.png','assets/laBotella.png',
                     'assets/elBarril.png','assets/elArbol.png','assets/elMelon.png','assets/elValiente.png',
                     'assets/elGorrito.png','assets/laMuerte.png','assets/laPera.png','assets/laBandera.png','assets/elBandolon.png',
                     'assets/elVioloncello.png','assets/laGarza.png','assets/elPajaro.png','assets/laMano.png','assets/laLuna.png',
                     'assets/elCotorro.png','assets/elBorracho.png','assets/elNegrito.png','assets/elCorzaon.png','assets/laSandia.png',
                     'assets/elTambor.png','assets/elCameron.png','assets/lasJaras.png','assets/elMusico.png','assets/laArana.png','assets/elSoldado.png',
                     'assets/laEstrella.png','assets/elCazo.png','assets/elMundo.png','assets/elApache.png','assets/elNopal.png','assets/elAlacran.png',
                    'assets/laRosa.png','assets/laCalavera.png','assets/laCampana.png','assets/elCantarito.png','assets/elVenado.png','assets/elSol.png',
                    'assets/laCorona.png','assets/laChalupa.png','assets/elPino.png','assets/elPescado.png','assets/laPalma.png','assets/laMaceta.png',
                    'assets/elArpa.png','assets/laRana.png'
                    ]

newList = random.sample(loteriaImageList,16)
# print(newList)

#set dimensions for window
screenWidth = 1250
screenHeight = 1000

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


def drawText(text,font,textColor,x,y):
    img = font.render(text,True,textColor)
    screen.blit(img,(x,y))

def populateCard():
    #creates a 2d list with dimensions, rows and columns, initialized with zeros
    rows,columns = (4,4)
    cardGrid = [[0 for i in range(rows)]for j in range (columns)]

    #iterate through the values and add them to the 2d grid
    # for i in range(len(loteriaDescList)):
    for index, image in enumerate(newList):
        #calculate the row and column
        row = index //columns# calculate the row index
        col = index % columns#calculate the column index
        #add the value to the position in the 2d grid/matrix
        image = pygame.image.load(image)
        imageSize = (150,150)
        cardImage = pygame.transform.scale(image,imageSize)
        cardGrid[row][col] = cardImage

    # print(cardGrid)
  
    row = 0
    while row <4:
        # for row in range(0,4):
        column = 0
        while column <4:
            screen.blit(cardGrid[row][column],pygame.Vector2((column*195+33.5),(row*195+30)))
            column+=1
        row +=1


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