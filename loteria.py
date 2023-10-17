import pygame
from pygame.locals import *
import random
import time
import sys
from button import Button
from network import Network





pygame.init()
pygame.mixer.init()


loteriaImageList = ['assets/elGallo.png','assets/elDiablito.png',
                     'assets/laDama.png','assets/elCatrin.png','assets/elParaguas.png',
                    'assets/laSirena.png','assets/laEscalera.png','assets/laBotella.png',
                     'assets/elBarril.png','assets/elArbol.png','assets/elMelon.png','assets/elValiente.png',
                     'assets/elGorrito.png','assets/laMuerte.png','assets/laPera.png','assets/laBandera.png','assets/elBandolon.png',
                     'assets/elVioloncello.png','assets/laGarza.png','assets/elPajaro.png','assets/laMano.png','assets/laBota.png','assets/laLuna.png',
                     'assets/elCotorro.png','assets/elBorracho.png','assets/elNegrito.png','assets/elCorazon.png','assets/laSandia.png',
                     'assets/elTambor.png','assets/elCamaron.png','assets/lasJaras.png','assets/elMusico.png','assets/laArana.png','assets/elSoldado.png',
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
                     'assets/elCotorro.png','assets/elBorracho.png','assets/elNegrito.png','assets/elCorazon.png','assets/laSandia.png',
                     'assets/elTambor.png','assets/elCamaron.png','assets/lasJaras.png','assets/elMusico.png','assets/laArana.png','assets/elSoldado.png',
                     'assets/laEstrella.png','assets/elCazo.png','assets/elMundo.png','assets/elApache.png','assets/elNopal.png','assets/elAlacran.png',
                    'assets/laRosa.png','assets/laCalavera.png','assets/laCampana.png','assets/elCantarito.png','assets/elVenado.png','assets/elSol.png',
                    'assets/laCorona.png','assets/laChalupa.png','assets/elPino.png','assets/elPescado.png','assets/laPalma.png','assets/laMaceta.png',
                    'assets/elArpa.png','assets/laRana.png'
                    ]

assetCardDict =          {'assets/elGallo.png':'audio/elGallo.mp3','assets/elDiablito.png':'audio/elDiablito.mp3',
                     'assets/laDama.png':'audio/laDama.mp3','assets/elCatrin.png':'audio/elCatrin.mp3','assets/elParaguas.png':'audio/elParaguas.mp3',
                    'assets/laSirena.png':'audio/laSirena.mp3','assets/laEscalera.png':'audio/laEscalera.mp3','assets/laBotella.png':'audio/laBotella.mp3',
                     'assets/elBarril.png':'audio/elBarril.mp3','assets/elArbol.png':'audio/elArbol.mp3','assets/elMelon.png':'audio/elMelon.mp3','assets/elValiente.png':'audio/elValiente.mp3',
                     'assets/elGorrito.png':'audio/elGorrito.mp3','assets/laMuerte.png':'audio/laMuerte.mp3','assets/laPera.png':'audio/laPera.mp3','assets/laBandera.png':'audio/laBandera.mp3','assets/elBandolon.png':'audio/elBandalon.mp3',
                     'assets/elVioloncello.png':'audio/elVioloncello.mp3','assets/laGarza.png':'audio/laGarza.mp3','assets/elPajaro.png':'audio/elPajaro.mp3','assets/laMano.png':'audio/laMano.mp3','assets/laBota.png':'audio/laBota.mp3','assets/laLuna.png':'audio/laLuna.mp3',
                     'assets/elCotorro.png':'audio/elCotorro.mp3','assets/elBorracho.png':'audio/elBorracho.mp3','assets/elNegrito.png':'audio/elNegrito.mp3','assets/elCorazon.png':'audio/elCorazon.mp3','assets/laSandia.png':'audio/laSandia.mp3',
                     'assets/elTambor.png':'audio/elTambor.mp3','assets/elCamaron.png':'audio/elCamaron.mp3','assets/lasJaras.png':'audio/lasJaras.mp3','assets/elMusico.png':'audio/elMusico.mp3','assets/laArana.png':'audio/laArana.mp3','assets/elSoldado.png':'audio/elSoldado.mp3',
                     'assets/laEstrella.png':'audio/laEstrella.mp3','assets/elCazo.png':'audio/elCazo.mp3','assets/elMundo.png':'audio/elMundo.mp3','assets/elApache.png':'audio/elApache.mp3','assets/elNopal.png':'audio/elNopal.mp3','assets/elAlacran.png':'audio/elAlacran.mp3',
                    'assets/laRosa.png':'audio/laRosa.mp3','assets/laCalavera.png':'audio/laCalavera.mp3','assets/laCampana.png':'audio/laCampana.mp3','assets/elCantarito.png':'audio/elCantarito.mp3','assets/elVenado.png':'audio/elVenado.mp3','assets/elSol.png':'audio/elSol.mp3',
                    'assets/laCorona.png':'audio/laCorona.mp3','assets/laChalupa.png':'audio/laChalupa.mp3','assets/elPino.png':'audio/elPino.mp3','assets/elPescado.png':'audio/elPescado.mp3','assets/laPalma.png':'audio/laPalma.mp3','assets/laMaceta.png':'audio/laMaceta.mp3',
                    'assets/elArpa.png':'audio/elArpa.mp3','assets/laRana.png':'audio/laRana.mp3'
                    }

# poppedCardList = []

copyCardGrid = []
currentCardDict = {}
dummyArray = [[0 for i in range(4)]for j in range (4)]

currentCard = ''

userInput = ''

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




randY = random.randint(10,780)
randX = random.randint(10,780)

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Loteria')


#game variables
winner = 0
clicked = False
gameOver = False
currentCard = ''
# Initialize a variable to store the entered text
username = ''

#define Fonts
font = pygame.font.SysFont('arialBlack',40)

#define colors
textColor = 'white'

#define variables
lineWidth = 10

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
            pygame.time.delay(1000)
            drawWinner()
        else:
            print('WE HAVE NO MATCHES for row '+ str(row)) 

    # Calculate column sums
    num_columns = len(dummyArray[0])  # Assuming all rows have the same number of columns
    for col in range(num_columns):
        col_sum = sum(dummyArray[row][col] for row in range(len(dummyArray)))
        if col_sum == 4:
            # print('YOU WON in column '+ str(col))
            pygame.time.delay(1000)
            drawWinner()
        else:
            print('WE HAVE NO MATCHES for column '+ str(col)) 

    if dummyArray[0][0] + dummyArray[1][1] + dummyArray[2][2] + dummyArray[3][3] == 4 or dummyArray[3][0] + dummyArray[1][2] + dummyArray[2][1] + dummyArray[3][0] == 4:
        # print('YOU WON in the first diagnol')
        pygame.time.delay(1000)
        drawWinner()

# def addToSecondSquare(game,p):
#     for picture in poppedCardList:
#         image = pygame.image.load(picture)
#         imageSize = (300,300)
#         cardImage = pygame.transform.scale(image,imageSize)
#         screen.blit(cardImage,pygame.Vector2(900,500))

def checkGameConnected(game,p):
    if not(game.conneced()):
        print('WE ARE NOT CONNECTED')

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
        value = assetCardDict.get(currentCard)
        # print(value)
        pygame.mixer.music.load(value)
        pygame.mixer.music.play()
        # sound = pygame.mixer.music.load(value)
        # sound = pygame.mixer.Sound(value)
        # sound.play()
        print('the current card is: '+ currentCard)
        image = pygame.image.load(currentCard)
        imageSize = (300,300)
        cardImage = pygame.transform.scale(image,imageSize)
        screen.blit(cardImage,pygame.Vector2(900,10))
        cardList.remove(currentCard)
        drawBeanToScreen()
        # pygame.time.delay(3000)
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
    global userInput
    
    while True:
        mousePos = pygame.mouse.get_pos()

        screen.fill('black')

        winnerText = userInput.upper() +' YOU WON'
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

def toTextInput():
    run = True
    # clock = pygame.time.Clock()
    # n = Network()
    # player = int(n.getP())
    # print('You are player', player)
    global userInput
    # active = False
    # colorActive = 'red'
    # colorPassive = 'blue'
    # color = colorPassive
    while run:

        # clock.tick(60)
        # try:
        #     game = n.send('get')
        # except:
        #     run = False
        #     print('Coudlnt get game') 
        #     break  

        # print(game.connected())
        # if (game.connected()):
    
        screen.fill('black')
        mousePos = pygame.mouse.get_pos()
        header = get_font(100).render('ENTER USER NAME',True,'white')
        headerRect = header.get_rect(center=(640,75))
        screen.blit(header,headerRect)

        rect = pygame.Rect(500,250,300,100)

        # if not(game.connected()):
        # text = get_font(50).render('Waiting for player...',True,'white')
        #         # get_font(50).render(userInput,True,'white')
        #     screen.blit(text,(400,500))
        # else:
        # submitButton = Button(image=None,pos=(640,650),text_input='Submit',font=get_font(75),base_color='white',hovering_color='blue')
        #     submitButton.changeColor(mousePos)
        #     submitButton.update(screen)
        


        submitButton = Button(image=None,pos=(640,550),text_input='Submit',font=get_font(75),base_color='white',hovering_color='blue')
        submitButton.changeColor(mousePos)
        submitButton.update(screen)


        # if game.connected()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if submitButton.checkForInput(mousePos):
                    if len(userInput) > 4:
                        play()
                    else:
                        print('YOU NEED TO TYPE A LONGER NAME')
                if rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                #check for backspace
                if event.key == pygame.K_BACKSPACE:
                    userInput = userInput[:-1]
                #unicode standard is used for string formation   
                else:
                    userInput += event.unicode
                    # print(n.send(userInput))
        # n.send(userInput)


        # if active:
        #     color = colorActiveo
        # else:
        #     color = colorPassive
        
        #create a rectangle
        pygame.draw.rect(screen,'white',rect,2,3)

        textSurface = get_font(50).render(userInput,True,'white')

        #display to screen
        screen.blit(textSurface,(rect.x+5,rect.y+5))
        

        # rect.w = max(300,textSurface.get_width()+10)

        pygame.display.flip()

def readCard(card):
    pass

def mainScreen():
    run = True
    gameStart = False
    
    while run:            
        # if ():
        #     pygame.time.delay(200)
        #     try:
        #         game = n.send('reset')
        #     except:
        #         run = False
        #         print('Couldnt get game')
        #         break
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
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePos):
                    toTextInput()
                        
            if event.type == pygame.MOUSEBUTTONUP:
                if playButton.checkForInput(mousePos):
                    toTextInput()
        
                if exitButton.checkForInput(mousePos):
                    pygame.quit()
        pygame.display.update()
                
def play():
    global userInput
    pygame.display.set_caption(userInput+' is playing Loteria!')
    while True:
        drawGameGrid()
        populateCard()
        drawCardRect()
        drawSecondCardRect()

        pygame.event.set_blocked(pygame.MOUSEMOTION)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #below we get mouse input, but we dont need it now
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         clicked=True
            #             # x,y = pygame.mouse.get_pos()
            #             # if 900 < x <1200 and 10<y<400:
            #         if not clicked:
            #             clickSquare()
                                    
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         clicked = True  
            #             # x,y = pygame.mouse.get_pos()
            #             # if 900 < x <1200 and 10<y<400:
            #         if clicked:
            #             clickSquare()
        #instead we call the function, and add a delay so it goes througth the cards manually
        clickSquare() 
        pygame.display.update()
        pygame.time.delay(3000)   
        
        
        


mainScreen()
        
