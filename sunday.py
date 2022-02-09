import pygame, sys
import os
import random
import time

from pygame.locals import *


validCharM = ["1","2","3","4","5","6","7","8","9","0","-"]
pygame.init()
pygame.display.set_mode()
pygame.font.get_init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,50)
win = pygame.display.set_mode((1000,675)) #creates a surface

cardfont = pygame.font.SysFont("timesnewroman", 13) #fonts and sizes
bigfont = pygame.font.SysFont("timesnewroman", 18)

cA = cardfont.render("A", True, (0, 0, 0))###letters for the cards
c2 = cardfont.render("2", True, (0, 0, 0))
c3 = cardfont.render("3", True, (0, 0, 0))
c4 = cardfont.render("4", True, (0, 0, 0))
c5 = cardfont.render("5", True, (0, 0, 0))
c6 = cardfont.render("6", True, (0, 0, 0))
c7 = cardfont.render("7", True, (0, 0, 0))
c8 = cardfont.render("8", True, (0, 0, 0))
c9 = cardfont.render("9", True, (0, 0, 0))
c10 = cardfont.render("10", True, (0, 0, 0))
cJ = cardfont.render("J", True, (0, 0, 0))
cQ = cardfont.render("Q", True, (0, 0, 0))
cK = cardfont.render("K", True, (0, 0, 0))

#Images for the suits
heart = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\heart.png').convert_alpha()
spade = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\spade.png').convert_alpha()
club = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\club.png').convert_alpha()
diamond = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\diamond.png').convert_alpha()

##heart = pygame.image.load(r'C:\Users\Zoltan\Downloads\heart.png').convert_alpha()##immages for the suits
##spade = pygame.image.load(r'C:\Users\Zoltan\Downloads\spade.png').convert_alpha()
##club = pygame.image.load(r'C:\Users\Zoltan\Downloads\club.png').convert_alpha()
##diamond = pygame.image.load(r'C:\Users\Zoltan\Downloads\diamond.png').convert_alpha()

pygame.display.set_caption("Black Jack")#sets the name of the window

suits = ['s','c','h','d']
cardValues = ['A','2','3','4','5','6','7','8','9','0','J','Q','K']

class TextBoxM(pygame.sprite.Sprite):# class for inputing text
  def __init__(self):#constructor to initialize starting text
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = bigfont
    self.image = bigfont.render("Enter running count:", False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.sumOfWager = 0
    self.numDigit = 0
  def add_chr(self, char): #accepting a proper number
    if char in validCharM:
        self.text += str(char)
    self.update()

  def update(self): #getting the input
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos

def trueCount(): #allows the player to wager an amount of money
    textBox = TextBoxM()
    textBox.rect.center = [470, 615]
    running = True
    while running:
      back, forward = tutorialButtons()
      if back:
          return False
      elif forward:
          return True
      pygame.draw.rect(win,(255,255,255), (380,605,200,30))
      win.blit(textBox.image, textBox.rect)
      pygame.display.flip()
      for e in pygame.event.get(): #has user add am amount to wager
        if e.type == pygame.QUIT:
            killgame()
        if e.type == pygame.KEYDOWN:
            if len(textBox.text)<10:
                textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            if e.key == pygame.K_RETURN: #when enter is hit the string is returned
                if len(textBox.text) > 0:
                    print (textBox.text)
                    return str(textBox.text)
                
class TextBoxM1(pygame.sprite.Sprite):# class for inputing text
  def __init__(self):#constructor to initialize starting text
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = bigfont
    self.image = bigfont.render("Enter the wager:", False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.sumOfWager = 0
    self.numDigit = 0
  def add_chr(self, char): #accepting a proper number
    if char in validCharM:
        self.text += str(char)
    self.update()

  def update(self): #getting the input
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos

def trueCount1(): #allows the player to wager an amount of money
    textBox = TextBoxM1()
    textBox.rect.center = [470, 615]
    running = True
    while running:
      back, forward = tutorialButtons()
      if back:
          return False
      elif forward:
          return True
      pygame.draw.rect(win,(255,255,255), (380,605,200,30))
      win.blit(textBox.image, textBox.rect)
      pygame.display.flip()
      for e in pygame.event.get(): #has user add am amount to wager
        if e.type == pygame.QUIT:
            killgame()
        if e.type == pygame.KEYDOWN:
            if len(textBox.text)<10:
                textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            if e.key == pygame.K_RETURN: #when enter is hit the string is returned
                if len(textBox.text) > 0:
                    print (textBox.text)
                    return str(textBox.text)

def killgame(): #exits the game
    pygame.display.quit()
    pygame.quit()
    exit()    
    
def checkquit(): #checks if the bix X in the corrner is hit
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killgame()   
    
def drawcard (card, placex, placey): #draws the correct card in the correct spot
    player = 0
    pygame.draw.rect(win,(0,0,0), (placex,placey,80,120))
    pygame.draw.rect(win,(255,255,255), (placex+1,placey+1,80-2,120-2))
    if card[0] == 'A':
        win.blit(cA,(placex+4 , placey+3 ))
        player+=11
    elif card[0] == '2':
        win.blit(c2,(placex+4 , placey+3 ))
        player+=2
    elif card[0] == '3':
        win.blit(c3,(placex+4 , placey+3 ))
        player+=3
    elif card[0] == '4':
        win.blit(c4,(placex+4 , placey+3 ))
        player+=4
    elif card[0] == '5':
        win.blit(c5,(placex+4 , placey+3 ))
        player+=5
    elif card[0] == '6':
        win.blit(c6,(placex+4 , placey+3 ))
        player+=6
    elif card[0] == '7':
        win.blit(c7,(placex+4 , placey+3 ))
        player+=7
    elif card[0] == '8':
        win.blit(c8,(placex+4 , placey+3 ))
        player+=8
    elif card[0] == '9':
        win.blit(c9,(placex+4 , placey+3 ))
        player+=9
    elif card[0] == '0':
        win.blit(c10,(placex+4 , placey+3 ))
        player+=10
    elif card[0] == 'J':
        win.blit(cJ,(placex+4 , placey+3 ))
        player+=10
    elif card[0] == 'Q':
        win.blit(cQ,(placex+4 , placey+3 ))
        player+=10
    elif card[0] == 'K':
        win.blit(cK,(placex+4 , placey+3 ))
        player+=10

    if card[1] == 'h':
        win.blit(heart, (placex+2,placey+17))
    elif card[1] == 's':
        win.blit(spade, (placex+2,placey+17))
    elif card[1] == 'd':
        win.blit(diamond, (placex+2,placey+17))
    elif card[1] == 'c':
        win.blit(club, (placex+2,placey+17))
    pygame.display.update()
    return player

def tutorialButtons():
    pygame.event.get()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    mousex=mouse[0]
    mousey=mouse[1]
    leftclick=click[0]
    backButtonHit = False
    forwardButtonHit = False
    #Check back button click
    if mousex>=50 and mousex<=150 and mousey>=30 and mousey<=85:
        pygame.draw.rect(win,(100,100,255),(55,35,90,45))
        if leftclick ==1:
            backButtonHit = True
        

    elif mousex>=855 and mousex<=955 and mousey>=30 and mousey<=85:
        pygame.draw.rect(win,(100,100,255),(855,35,90,45))
        if leftclick ==1:
            forwardButtonHit = True
        
    else:
        drawButtons()
    return(backButtonHit, forwardButtonHit)

def drawButtons():
    pygame.draw.rect(win,(0,0,0),(50,30,100,55))
    pygame.draw.rect(win,(0,0,255),(55,35,90,45))
    
    pygame.draw.rect(win,(0,0,0),(850,30,100,55))
    pygame.draw.rect(win,(0,0,255),(855,35,90,45))
    win.blit(backTM, (75,45))
    win.blit(forwardTM, (875,45))
    pygame.display.update()
def formula():
    printText(menuFont,"Calculate the wager",400,50)
    pygame.draw.rect(win,(255,255,255),(600,125,350,400))
    pygame.draw.line(win,(0,0,0),(600,320),(950,320))
    printText(cardfont,"Betting Formula: W = B(T-1)",700,190)
    printText(cardfont,"For W = wager, B = betting unit and T = true count",625,250)
    printText(cardfont,"True Count: T = R / D",730,380)
    printText(cardfont,"For T = true count, R = running count and D = number of decks ",605,440)
    pygame.draw.rect(win,(255,255,255),(100,270,320,150))
    
def checkWin(condition,func):
    if func()==condition:
        printText(menuFont,"That is correct",375,170)
        pygame.display.update()
        time.sleep(1.5)
        phase1 = False
        return 1
    return 0
def printText(font,text,x,y):
    textT = font.render(text,True,(0,0,0))
    win.blit(textT,(x,y))
    pygame.display.update()
################################ B L A C K J A C K   T U T O R I A L ###################
SlideM = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\BCCC.jpg')
Slide0 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide.jpg')
Slide1 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (1).jpg').convert_alpha()
Slide2 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (2).jpg').convert_alpha()
Slide3 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (3).jpg').convert_alpha()
##Slide4 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (4).jpg').convert_alpha()
Slide5 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (5).jpg').convert_alpha()
Slide6 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (6).jpg').convert_alpha()
Slide7 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (7).jpg').convert_alpha()
##Slide8 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (8).jpg').convert_alpha()
Slide9 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (9).jpg').convert_alpha()
Slide10 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (10).jpg').convert_alpha()
Slide11 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (11).jpg').convert_alpha()
Slide12 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (12).jpg').convert_alpha()
Slide13 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (13).jpg').convert_alpha()
Slide14 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (14).jpg').convert_alpha()
Slide15 = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\Card Counting Guide (15).jpg').convert_alpha()
tutorialPages = [SlideM,Slide0,Slide1,Slide2,Slide3,Slide5,Slide6,Slide7,Slide9,Slide10,Slide11,Slide12,Slide13,Slide14,Slide15]
menuFont = pygame.font.SysFont("timesnewroman", 28)
mTextFont = pygame.font.SysFont("timesnewroman", 52)
forwardTM = menuFont.render("Next", True, (0,0,0))
backTM = menuFont.render("Back", True, (0,0,0))
textTM = menuFont.render("Press enter to proceed", True, (0,0,0))
winTM = mTextFont.render("Win!", True, (0,0,0))
blackjackTM = mTextFont.render("Blackjack!", True, (0,0,0))
bustTM = mTextFont.render("Bust!", True, (0,0,0))
pushTM = mTextFont.render("Push!", True, (0,0,0))

##Efficiency and user friendly
##REMEMBER TO UPDATE SLIDES TO THE NEW ONES
pageIndex = 10
subIndex = 0
change = subIndex
tutorial = [1,2,4,5,7,8,11,12,13,14,15]
simulation = [3,6,9,10]
inTutorial = True

###################  M A I N    L O O P   ######################
while inTutorial:
    phase1 = True
    try:
        win.blit(tutorialPages[pageIndex], (0,0))
        pygame.display.update()
        #Implement tap anywhere to start for menu page
        if pageIndex == 0:
            #mouse shenanigans
            pygame.event.get()
            click = pygame.mouse.get_pressed()
            leftclick=click[0]
            rightclick=click[2]

            if leftclick == 1 or rightclick == 1:
                pageIndex+=1
                time.sleep(.5)

        else:
            drawButtons()
            subIndex = 0
            while True:
                #mouse shenanigans

                back, forward = tutorialButtons()
                pygame.display.update()
                time.sleep(.06)#Doesn't make the buttons spasm
                if pageIndex in tutorial:
                    ##DO TUTORIAL SHIT
                    win.blit(tutorialPages[pageIndex], (0,0))
                    drawButtons()
                    pygame.display.update()
                    if back:
                        if pageIndex-1>=0:
                            pageIndex-=1
                            time.sleep(.5)
                            subIndex = 0
                            phase1 = True
                            break
                    elif forward:
                        pageIndex+=1
                        time.sleep(.5)
                        subIndex = 0
                        break
                elif pageIndex in simulation:
                    ##DO SIMULATION SHIT
                    drawButtons()
                    checkquit()
                    if back:
                        if pageIndex-1>=0:
                            pageIndex-=1
                            time.sleep(.5)
                            subIndex = 0
                            phase1 = True
                            break
                    elif forward:
                        pageIndex+=1
                        time.sleep(.5)
                        subIndex = 0
                        phase1 = True
                        break
                    else:
                        if pageIndex ==3:
                            
                            if subIndex ==0: 
                                while phase1:

                                    printText(menuFont,"Press enter to proceed", 400, 50)
                                    ######   W I N   ########
                                    pygame.draw.line(win,(0,0,0),(25,415),(975,415))
                                    drawcard("0s",425,250)
                                    time.sleep(.5)
                                    drawcard("7h",450,270)
                                    time.sleep(.5)
                                    printText(menuFont,"Dealer's hand total is 17",125,280)
                                    time.sleep(.5)
                                    drawcard("Jd",425,450)
                                    time.sleep(.5)
                                    drawcard("Kc",450,470)
                                    time.sleep(.5)
                                    printText(menuFont,"Player's hand total is 20",625,500)
                                    phase1 = False
                                    time.sleep(.5)
                                    win.blit(winTM, (450,100))
                                    pygame.display.update()
                            elif subIndex ==1:
                                while phase1:
                                    printText(menuFont,"Press enter to proceed", 400, 50)
                                    #######   B L A C K J A C K   ########
                                    pygame.draw.line(win,(0,0,0),(25,415),(975,415))
                                    drawcard("0s",425,250)
                                    time.sleep(.5)
                                    drawcard("7h",450,270)
                                    time.sleep(.5)
                                    printText(menuFont,"Dealer's hand total is 17",125,280)
                                    time.sleep(.5)
                                    drawcard("Jd",425,450)
                                    time.sleep(.5)
                                    drawcard("Ad",450,470)
                                    printText(menuFont,"Player's hand total is 21",625,500)
                                    phase1 = False
                                    time.sleep(.5)
                                    win.blit(blackjackTM, (370,150))
                                    pygame.display.update()
                            elif subIndex ==2:
                                while phase1:
                                    printText(menuFont,"Press enter to proceed", 400,50)
                                    #######   B U S T   ########
                                    pygame.draw.line(win,(0,0,0),(25,415),(975,415))
                                    drawcard("9s",425,250)
                                    time.sleep(.5)
                                    drawcard("0d",450,270)
                                    time.sleep(.5)
                                    printText(menuFont,"Dealer's hand total is 19",125,280)
                                    time.sleep(.5)
                                    drawcard("3c",425,450)
                                    time.sleep(.5)
                                    drawcard("7h",450,470)
                                    time.sleep(.5)
                                    drawcard("5d",475,490)
                                    time.sleep(.5)
                                    drawcard("Js",500,510)
                                    printText(menuFont,"Player's hand total is 25", 625,500)
                                    phase1 = False
                                    time.sleep(.5)
                                    win.blit(bustTM, (450,150))
                                    pygame.display.update()
                            elif subIndex ==3:
                                while phase1:
                                    printText(menuFont,"Press enter to proceed",400,50)
                                    #######   P U S H   ########
                                    pygame.draw.line(win,(0,0,0),(25,415),(975,415))
                                    drawcard("0s",425,250)
                                    time.sleep(.5)
                                    drawcard("7h",450,270)
                                    time.sleep(.5)
                                    printText(menuFont,"Dealer's hand total is 17",125,280)
                                    time.sleep(.5)
                                    drawcard("3s",425,450)
                                    time.sleep(.5)
                                    drawcard("5h",450,470)
                                    time.sleep(.5)
                                    drawcard("9d",475,490)
                                    printText(menuFont,"Player's hand total is 17",625,500)
                                    phase1 = False
                                    time.sleep(.5)
                                    win.blit(pushTM, (450,150))
                                    pygame.display.update()
                            print("HI")
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_RETURN:
                                        if subIndex<3:
                                            subIndex+=1
                                            phase1 = True
                                            win.blit(tutorialPages[pageIndex],(0,0))
                                            drawButtons()
                                            pygame.display.update()
                        elif pageIndex ==6:
                            drawButtons()
                            checkquit()
                            if subIndex == 0:
                                while phase1:
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    change = subIndex
                                    printText(bigfont,"Enter the running count. Then press enter to continue",275,50)
                                    ######   R U N N I N G  C O U N T   #####
                                    pygame.draw.line(win,(0,0,0),(25,415),(975,415))
                                    drawcard("Ks",425,250)
                                    drawcard("0h",450,270)
                                    drawcard("0d",425,450)
                                    drawcard("2c",450,470)
                                    phase1 = False
                                subIndex += checkWin("-2",trueCount)
                                if subIndex != change:
                                    phase1 = True
                            elif subIndex ==1:
                                while phase1:
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    change = subIndex
                                    printText(bigfont,"Enter the running count. Then press enter to continue",275,50)
                                    ######   R U N N I N G  C O U N T   2  #####
                                    pygame.draw.line(win,(0,0,0),(25,415),(975,415))
                                    drawcard("2s",425,250)
                                    drawcard("5h",450,270)
                                    drawcard("3d",425,450)
                                    drawcard("2c",450,470)
                                    phase1 = False
                                subIndex += checkWin("4",trueCount)
                                if subIndex!=change:
                                    phase1 = True
                            elif subIndex ==2:
                                while phase1:
                                    change = pageIndex
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    printText(bigfont,"Enter the running count. Then press enter to continue",275,50)
                                    ######    R U N N I N G  C O U N T   3  ####
                                    pygame.draw.line(win,(0,0,0),(25,415),(975,415))
                                    drawcard("2s",425,250)
                                    drawcard("5h",450,270)
                                    drawcard("Kd",425,450)
                                    drawcard("0c",450,470)
                                    phase1 = False
                                pageIndex += checkWin("0",trueCount)
                                if pageIndex!=change:
                                    phase1 = True
                        elif pageIndex ==9:
                            if subIndex == 0:
                                ####  A C T I V I T Y    1  ####
                                while phase1:
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    change = subIndex
                                    formula()
                                    printText(cardfont,"Calculate the wager. Running count is 12. ",150,310)
                                    printText(cardfont,"There are 3 decks. A betting unit of 100",150,360)
                                    phase1 = False
                                subIndex += checkWin("300",trueCount1)
                                if subIndex!=change:
                                    phase1 = True
                                print(subIndex)
                            elif subIndex ==1:
                                ####  A C T I V I T Y    2  ####
                                while phase1:
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    change = subIndex
                                    formula()
                                    printText(cardfont,"Calculate the wager. Running count is 24.",150,310)
                                    printText(cardfont,"There are 8 decks. A betting unit of 100",150, 360)
                                    phase1 = False
                                subIndex += checkWin("200",trueCount1)
                                if subIndex!=change:
                                    phase1 = True
                                print(subIndex)
                            elif subIndex ==2:
                                ####  A C T I V I T Y    3  ####
                                while phase1:
                                    change = pageIndex
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    formula()
                                    printText(cardfont,"Calculate the wager. Running count is -12",150,310)
                                    printText(cardfont,"There are 6 decks. A betting unit of 100",150,335)
                                    printText(cardfont,"The minimum bet is 10",200,360)
                                    phase1 = False
                                pageIndex += checkWin("10",trueCount1)
                                if pageIndex!=change:
                                    phase1 = True
                                print(subIndex)
                        elif pageIndex == 10:
                            #####   M E A N I N G F U L   P A I R    #####
                            while phase1:
                                win.blit(tutorialPages[pageIndex], (0,0))
                                pygame.display.update()
                                drawButtons()
                                pygame.draw.rect(win,(255,0,0),(100,365,200,250))
                                drawcard("3c",150,450)
                                time.sleep(.5)
                                drawcard("7h",175,470)
                                time.sleep(.5)
                                printText(bigfont,"Not a meaningful pair",125,385)
                                pygame.draw.rect(win,(0,255,0),(390,365,200,250))
                                drawcard("3c",440,450)
                                time.sleep(.5)
                                drawcard("0h",465,470)
                                time.sleep(.5)
                                printText(bigfont,"Meaningful pair",440,385)
                                pygame.draw.rect(win,(255,0,0),(675,365,200,250))
                                drawcard("Jc",725,450)
                                time.sleep(.5)
                                drawcard("Qh",750,470)
                                time.sleep(.5)
                                printText(bigfont,"Not a meaningful pair",700,385)
                                phase1 = False
    except IndexError:
        inTutorial = False
print("DONE")
