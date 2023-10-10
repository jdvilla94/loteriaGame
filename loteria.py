import pygame
from pygame.locals import *
import random
import time
import sys
from button import Button




pygame.init()

loteriaImageList = ['assets/elGallo.png','assets/elDiablito.png',
                     'assets/laDama.png','assets/elCatrin.png','assets/elParaguas.png',
                    'assets/laSirena.png','assets/laEscalera.png','assets/laBotella.png',
                     'assets/elBarril.png','assets/elArbol.png','assets/elMelon.png','assets/elValiente.png',
                     'assets/elGorrito.png','assets/laMuerte.png','assets/laPera.png','assets/laBandera.png','assets/elBandolon.png',
                     'assets/elVioloncello.png','assets/laGarza.png','assets/elPajaro.png','assets/laMano.png','assets/laBota.png','assets/laLuna.png',
                     'assets/elCotorro.png','assets/elBorracho.png','assets/elNegrito.png','assets/elCorzaon.png','assets/laSandia.png',
                     'assets/elTambor.png','assets/elCameron.png','assets/lasJaras.png','assets/elMusico.png','assets/laArana.png','assets/elSoldado.png',
                     'assets/laEstrella.png','assets/elCazo.png','assets/elMundo.png','assets/elApache.png','assets/elNopal.png','assets/elAlacran.png',
                    'assets/laRosa.png','assets/laCalavera.png','assets/laCampana.png','assets/elCantarito.png','assets/elVenado.png','assets/elSol.png',
                    'assets/laCorona.png','assets/laChalupa.png','assets/elPino.png','assets/elPescado.png','assets/laPalma.png','assets/laMaceta.png',
                    'assets/elArpa.png','assets/laRana.png'
                    ]

cardList =          ['assets/elGallo.png','assets/elDiablito.png',
                     'assets/laDama.png','assets/elCatrin.png','assets/elParaguas.png',
                    'assets/laSirena.png','assets/laEscalera.png','assets/laBotella.png',
                     'assets/elBarril.png','assets/elArbol.png','assets/elMelon.png','assets/elValiente.png',
                     'assets/elGorrito.png','assets/laMuerte.png','assets/laPera.png','assets/laBandera.png','assets/elBandolon.png',
                     'assets/elVioloncello.png','assets/laGarza.png','assets/elPajaro.png','assets/laMano.png','assets/laBota.png','assets/laLuna.png',
                     'assets/elCotorro.png','assets/elBorracho.png','assets/elNegrito.png','assets/elCorzaon.png','assets/laSandia.png',
                     'assets/elTambor.png','assets/elCameron.png','assets/lasJaras.png','assets/elMusico.png','assets/laArana.png','assets/elSoldado.png',
                     'assets/laEstrella.png','assets/elCazo.png','assets/elMundo.png','assets/elApache.png','assets/elNopal.png','assets/elAlacran.png',
                    'assets/laRosa.png','assets/laCalavera.png','assets/laCampana.png','assets/elCantarito.png','assets/elVenado.png','assets/elSol.png',
                    'assets/laCorona.png','assets/laChalupa.png','assets/elPino.png','assets/elPescado.png','assets/laPalma.png','assets/laMaceta.png',
                    'assets/elArpa.png','assets/laRana.png'
                    ]

# poppedCardList = []

copyCardGrid = []
currentCardDict = {}
dummyArray = [[0 for i in range(4)]for j in range (4)]

currentCard = ''

newList = random.sample(loteriaImageList,16)

#set dimensions for window
screenWidth = 1250
screenHeight = 1000


#rects dimensions
cardWidth = 300
cardHeight = 300
cardX = 900
cardY = 10
card2x = 900
card2y = 500
recColor = 'white'

clock = pygame.time.Clock()
FPS = 120

randY = random.randint(10,780)
randX = random.randint(10,780)

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Loteria')


#game variables
# gameStart = False
winner = 0
clicked = False
gameOver = False
currentCard = ''

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

def drawCardRect():
    rectangle = pygame.Rect(cardX,cardY,cardWidth,cardHeight)
    # pygame.draw.rect(screen,pygame.Color('white'),pygame.Rect(10,10,780,780),10)
    pygame.draw.rect(screen,recColor,rectangle,10)

def drawSecondCardRect():
    rectangle = pygame.Rect(card2x,card2y,cardWidth,cardHeight)
    # pygame.draw.rect(screen,pygame.Color('white'),pygame.Rect(10,10,780,780),10)
    pygame.draw.rect(screen,recColor,rectangle,10)



def drawBeanToScreen():
    global currentCard
    global cardList
    global copyCardGrid

    # print('WE ARE IN THE DRAWBEAN DEF, THE LENGTH OF THE CARD LIST IS: '+str(len(cardList)))

    for rowIndex,row in enumerate(copyCardGrid):
        for colIndex,element in enumerate(row):
            if element == currentCard:#if statemnet causing errors
                currentCardDict[element] = rowIndex,colIndex
                print(currentCardDict)
                dummyArray[rowIndex][colIndex] = 1

    for key, value in currentCardDict.items():
        image = pygame.image.load('assets/frijole.png')
        imageSize = (75,75)
        cardImage = pygame.transform.scale(image,imageSize)
        row,col = value
        screen.blit(cardImage,pygame.Vector2(col*195+60,row*195+60))
        checkWinner()


                
def checkWinner():

    # Calculate row sums
    for row in dummyArray:
        if sum(row) == 4:
            # print('YOU WON in row '+ str(row))
            drawWinner()
        else:
            print('WE HAVE NO MATCHES for row '+ str(row)) 

    # Calculate column sums
    num_columns = len(dummyArray[0])  # Assuming all rows have the same number of columns
    for col in range(num_columns):
        col_sum = sum(dummyArray[row][col] for row in range(len(dummyArray)))
        if col_sum == 4:
            # print('YOU WON in column '+ str(col))
            drawWinner()
        else:
            print('WE HAVE NO MATCHES for column '+ str(col)) 

    if dummyArray[0][0] + dummyArray[1][1] + dummyArray[2][2] + dummyArray[3][3] == 4 or dummyArray[3][0] + dummyArray[1][2] + dummyArray[2][1] + dummyArray[3][0] == 4:
        # print('YOU WON in the first diagnol')
        drawWinner()

# def addToSecondSquare():
#     for picture in poppedCardList:
#         image = pygame.image.load(picture)
#         imageSize = (300,300)
#         cardImage = pygame.transform.scale(image,imageSize)
#         screen.blit(cardImage,pygame.Vector2(900,500))

def clickSquare():
    # print(f"Clicked on cell({row},{column})")
    global clicked
    global shuffleCard
    global currentCard
    global copyCardGrid
    global cardList
 
    
    # print(copyCardGrid)
    if len(cardList)>0:
        currentCard = random.choice(cardList) 
        print('the current card is: '+ currentCard)
        image = pygame.image.load(currentCard)
        imageSize = (300,300)
        cardImage = pygame.transform.scale(image,imageSize)
        screen.blit(cardImage,pygame.Vector2(900,10))
        cardList.remove(currentCard)
        drawBeanToScreen()
        # print('the length of the cardlist currently is: '+ str(len(cardList)))
                        
    else:
        print('There are no more cards in the deck')
        
def populateCard():
    global copyCardGrid
    global currentCard
    #creates a 2d list with dimensions, rows and columns, initialized with zeros
    rows,columns = (4,4)
    cardGrid = [[0 for i in range(rows)]for j in range (columns)]
    copyCardGrid = [[0 for i in range(rows)]for j in range (columns)]
    #iterate through the values and add them to the 2d grid
    # for i in range(len(loteriaDescList)):
    for index, picture in enumerate(newList):
        #calculate the row and column
        row = index //columns# calculate the row index
        col = index % columns#calculate the column index
        #add the value to the position in the 2d grid/matrix
        image = pygame.image.load(picture)
        imageSize = (150,150)
        cardImage = pygame.transform.scale(image,imageSize)
        cardGrid[row][col] = cardImage
        copyCardGrid[row][col] = picture


    row = 0
    while row <4:
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

    for x in range(1,4):
        pygame.draw.line(screen,grid,(10,x*195+10),(780,x*195+10),lineWidth)
        pygame.draw.line(screen,grid,(x*195+10,10),(x*195+10,780),lineWidth)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont('arialBlack', size)

def drawWinner():
    global dummyArray 
    global cardList
    global loteriaImageList
    global newList
    
    while True:
        mousePos = pygame.mouse.get_pos()

        screen.fill('black')

        winnerText = 'You Won'
        winnerImage = font.render(winnerText,True,'white')
        winnerRect = winnerImage.get_rect(center=(640,260))
        screen.blit(winnerImage,winnerRect)

        playAgain = Button(image= None,pos=(625,500),text_input='Play Again',font= get_font(75),base_color='white',hovering_color='blue')
        playAgain.changeColor(mousePos)
        playAgain.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playAgain.checkForInput(mousePos):
                    dummyArray = [[0 for i in range(4)]for j in range (4)]
                    cardList = loteriaImageList
                    currentCardDict.clear()
                    newList = random.sample(loteriaImageList,16)
                    print('the new list is": '+ str(newList))
                    play()
                    

            pygame.display.update()


# Initialize a variable to store the entered text
entered_text = ""

# def toTextInput():


def mainScreen():
    gameStart = False
    # running = True
    while True:
        #draw board
        # if gameStart == True:
        #     drawGameGrid()
        #     populateCard()
        #     drawCardRect()
        #     drawSecondCardRect()
            # addToSecondSquare()
        # else:
        #     drawText('Press space to begin',font,textColor,160,250)

        screen.fill('black')
        mousePos = pygame.mouse.get_pos()
        menuText = get_font(100).render('MAIN MENU',True,'white')
        menuRect = menuText.get_rect(center=(640,100))

        playButton = Button(image=None,pos=(640,250),text_input='PLAY',font=get_font(75),base_color='white',hovering_color='blue')
        exitButton = Button(image=None,pos=(640,400),text_input='EXIT',font=get_font(75),base_color='white',hovering_color='blue')


        screen.blit(menuText,menuRect)

        for button in [playButton,exitButton]:
            button.changeColor(mousePos)
            button.update(screen)

        for event in pygame.event.get():
            # pygame.event.set_blocked(pygame.MOUSEMOTION)
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePos):
                    play()
            if event.type == pygame.MOUSEBUTTONUP:
                if playButton.checkForInput(mousePos):
                    play()
                if exitButton.checkForInput(mousePos):
                    pygame.quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         gameStart = True
            
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         clicked=True
            #         # x,y = pygame.mouse.get_pos()
            #         # if 900 < x <1200 and 10<y<400:
            #         if not clicked:
            #             clickSquare()
                                
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         clicked = True  
            #         # x,y = pygame.mouse.get_pos()
            #         # if 900 < x <1200 and 10<y<400:
            #         if clicked:
            #             clickSquare()
            
        pygame.display.update()

def play():
    while True:
        drawGameGrid()
        populateCard()
        drawCardRect()
        # drawSecondCardRect()
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked=True
                        # x,y = pygame.mouse.get_pos()
                        # if 900 < x <1200 and 10<y<400:
                    if not clicked:
                        clickSquare()
                                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = True  
                        # x,y = pygame.mouse.get_pos()
                        # if 900 < x <1200 and 10<y<400:
                    if clicked:
                        clickSquare()

            

            pygame.display.update()


mainScreen()
        
