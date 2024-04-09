import pygame
import sys
import random
from time import sleep


BLACK = (0, 0, 0)
padWidth = 1550
padHeight = 800
clock = 0


def crash():
    if 900 + HP == 726:
        global gamePad, score
        writeMessage('점수 : ' + (str(score)))




def writeMessage(text):    
    global gamePad
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    playGame()
    
def Soulmove():
    global soulX, soulY
    for event in pygame.event.get():
        if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:      
                soulX -= 4

            elif event.key == pygame.K_RIGHT:       
                soulX += 4

            elif event.key == pygame.K_UP:
                    soulY -= 4

            elif event.key == pygame.K_DOWN:
                soulY += 4

        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                soulX = 0        

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                soulY = 0


def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y,))


def initGame():
    global gamePad, clock, background, nifeSound
    global soul, nife, nife2, nife3, nife4
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    background = pygame.image.load('undertale_background.png')
    soul = pygame.image.load('soul.jpg')
    nife = pygame.image.load("nife.png")
    nife2 = pygame.image.load("nife2.png")
    nife3 = pygame.image.load("nife3.png")
    nife4 = pygame.image.load("nife4.png")
    pygame.mixer.music.load('undertalebgm2.mp3')
    nifeSound = pygame.mixer.Sound('nifesound2.mp3')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()


def playGame():
    global gamePad, clock, background, nifeSpeed, nifeHeight, nifeWidth, nifeSound
    global score, nife, nife2, nife3, nife4, soul
    global soulX, soulY, nifeX, nifeY, nife2X, nife2Y, nife3X, nife3Y, nife4X, nife4Y
    global nifeHeight, nifeWidth, nife2Height, nife2Width, nife3Height, nife3Width, nife4Height, nife4Width
    global HP
    HP = 0
    score = 0
    RED = (255, 0, 0)
    soulSize = soul.get_rect().size
    soulWidth = soulSize[0]
    soulHeight = soulSize[1]



    HPX = 710
    HPY = 705







    x = padWidth * 0.48
    y = padHeight * 0.5
    soulX = 0
    soulY = 0
    
    nifeSize = nife.get_rect().size
    nifeWidth = nifeSize[0]
    nifeHeight = nifeSize[1]



    nifeX = random.randint(605, 970)
    nifeY = 0
    nifeSpeed = 5




    nife2Size = nife2.get_rect().size
    nife2Width = nife2Size[0]
    nife2Height = nife2Size[1]

    nife2X = 200
    nife2Y = random.randint(275, 630)
    nife2Speed = 5



    nife3Size = nife3.get_rect().size
    nife3Width = nife3Size[0]
    nife3Height = nife3Size[1]

    nife3X = random.randint(605, 970)
    nife3Y = 800
    nife3Speed = 5





    nife4Size = nife4.get_rect().size
    nife4Width = nife4Size[0]
    nife4Height = nife4Size[1]

    nife4X = 1350
    nife4Y = random.randint(275, 630)
    nife4Speed = 5



    onGame = False
    while not onGame:
        Soulmove()



        drawObject(background, 0, 0)

        x += soulX
        if x < 598:
            x = 598

        elif x > 955:
            x = 955

        


        y += soulY
        if y < 282:
            y = 282

        elif y > 625:
            y = 625

        if y < nifeY + nifeHeight:
            if(nifeX > x and nifeX < x + soulWidth) or (nifeX + nifeWidth > x and nifeX + nifeWidth < x + soulWidth):
                crash()
                HP -= 2


        if score > 15:
            if x < nife2X + nife2Width:
                if(nife2Y > y and nife2Y < y + soulHeight) or (nife2Y + nife2Height > x and nife2Y + nife2Height < y + soulHeight):
                    crash()
                    HP -= 2
                

        if score > 35:        
            if y > nife3Y + nife3Height:
                if(nife3X > x and nife3X < x + soulWidth) or (nife3X + nife3Width > x and nife3X + nife3Width < x + soulWidth):
                    crash()
                    HP -= 2

        if score > 70:
            if x > nife4X + nife4Width:
               if(nife4Y > y and nife4Y < y + soulHeight) or (nife4Y + nife4Height > x and nife4Y + nife4Height < y + soulHeight):
                    crash()
                    HP -= 2


                

        
        drawObject(soul, x, y)


        nifeY += nifeSpeed
        nife2X += nife2Speed
        nife3Y -= nife3Speed
        nife4X -= nife4Speed

        if nifeY > padHeight:
            
            nifeSound.play() 
            nifeSize = nife.get_rect().size
            nifeWidth = nifeSize[0]
            nifeHeight = nifeSize[1]
            nifeX = random.randint(605, 970)
            nifeY = 0
            nifeSpeed += 0.1
            score += 2


        if nife2X > padWidth:
            if score > 15:
                nifeSound.play()
            nifeSound.play()
            nife2Size = nife.get_rect().size
            nife2Width = nifeSize[0]
            nife2Height = nifeSize[1]
            nife2X = 200
            nife2Y = random.randint(275, 630)
            nife2Speed += 0.2
            score += 2


        if nife3Y < 0:
            if score > 35:
                nifeSound.play()
            nifeSound.play()
            nife3Size = nife3.get_rect().size
            nife3Width = nife3Size[0]
            nife3Height = nife3Size[1]
            nife3X = random.randint(605, 970)
            nife3Y = 800
            nife3Speed += 0.1
            score += 2



        if nife4X < 0:
            if score > 70:
                nifeSound.play()
            nifeSound.play()
            nife4Size = nife4.get_rect().size
            nife4Width = nife4Size[0]
            nife4Height = nife4Size[1]

            nife4X = 1200
            nife4Y = random.randint(275, 630)
            nife4Speed += 0.2
            score += 2
        
            
            
        
        drawObject(nife, nifeX, nifeY)

        if score > 15:
            drawObject(nife2, nife2X, nife2Y)
        if score > 35:
            drawObject(nife3, nife3X, nife3Y)
        if score > 70:
            drawObject(nife4, nife4X, nife4Y)


        pygame.draw.polygon(gamePad, RED, ((900 + HP, 699), (900 + HP, 744), (900, 744), (900, 699))) 


     
 



        
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

initGame()

playGame()

            
