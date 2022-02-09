

import pygame, sys
import os
import random
import time

from pygame.locals import *

validCharM = ["1","2","3","4","5","6","7","8","9","0","-"]
validChars = "1234567890"
pygame.init()
pygame.display.set_mode()
pygame.font.get_init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,50)
win = pygame.display.set_mode((1000,675)) #creates a surface

#Images for the suits
heart = pygame.image.load(r'C:\Users\Zoltan\Downloads\heart.png').convert_alpha()
spade = pygame.image.load(r'C:\Users\Zoltan\Downloads\spade.png').convert_alpha()
club = pygame.image.load(r'C:\Users\Zoltan\Downloads\club.png').convert_alpha()
diamond = pygame.image.load(r'C:\Users\Zoltan\Downloads\diamond.png').convert_alpha()

pygame.display.set_caption("Black Jack Tutorial")#sets the name of the window

suits = ['s','c','h','d']
cardValues = ['A','2','3','4','5','6','7','8','9','0','J','Q','K']
###### T U T O R I A L    F U N C T I O N S   #######
class TextBoxM(pygame.sprite.Sprite):# object for running count text box
  def __init__(self):#constructor for Text Box elements 
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = bigfont
    self.image = bigfont.render("Enter running count:", False, [0, 0, 0])
    self.rect = self.image.get_rect()
  def add_chr(self, char): #accepting a proper number and add char
    if char in validCharM:
        self.text += str(char)
    self.update()

  def update(self): #updating the text box display
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos

def trueCount(): #textBox interface for true count activity
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
      for e in pygame.event.get(): 
        if e.type == pygame.QUIT:
            killgame()
        if e.type == pygame.KEYDOWN:#Get keypress if less than 10 char
            if len(textBox.text)<10:
                textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_BACKSPACE:#Remove one char
                textBox.text = textBox.text[:-1]
                textBox.update()
            if e.key == pygame.K_RETURN: #when enter is hit the string is returned
                if len(textBox.text) > 0:
                    print (textBox.text)
                    return str(textBox.text)
               
class TextBoxM1(pygame.sprite.Sprite):# object for entering calculated wager
  def __init__(self):#constructor for text box elements
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = bigfont
    self.image = bigfont.render("Enter the wager:", False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.sumOfWager = 0
    self.numDigit = 0
  def add_chr(self, char): #accepting a proper number and add char
    if char in validCharM:
        self.text += str(char)
    self.update()

  def update(self): #updating the text box display
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
        if e.type == pygame.KEYDOWN:#Get keypress if less than 10 char
            if len(textBox.text)<10:
                textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_BACKSPACE:#Remove one char
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

def tutorialButtons():#Check mouse clicks and determine if buttons are clicked
    checkquit()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    mousex=mouse[0]
    mousey=mouse[1]
    leftclick=click[0]
    backButtonHit = False
    forwardButtonHit = False
    
    #Check back button click
    if mousex>=50 and mousex<=150 and mousey>=30 and mousey<=85:#Check if back button hit
        pygame.draw.rect(win,(0,0,0),(50,30,100,55))
        pygame.draw.rect(win,(100,100,255),(55,35,90,45))
        
        if leftclick ==1:
          #while True:
          #  checkquit()
          #  click = pygame.mouse.get_pressed()
          #  leftclick=click[0]
          #  if leftclick == 0:
          #5    break            
          backButtonHit = True
    else:
        pygame.draw.rect(win,(0,0,0),(50,30,100,55))
        pygame.draw.rect(win,(0,0,255),(55,35,90,45))
            
    if mousex>=855 and mousex<=955 and mousey>=30 and mousey<=85:#Check if forward button hit
        pygame.draw.rect(win,(0,0,0),(850,30,100,55))
        pygame.draw.rect(win,(100,100,255),(855,35,90,45))
        
        if leftclick ==1:
          #while True:
          #  checkquit()
          #  click = pygame.mouse.get_pressed()
          #  leftclick=click[0]
          #  if leftclick == 0:
          #    break
          forwardButtonHit = True
    else:
        pygame.draw.rect(win,(0,0,0),(850,30,100,55))
        pygame.draw.rect(win,(0,0,255),(855,35,90,45))
        
    win.blit(backTM, (75,45))
    win.blit(forwardTM, (875,45))
    pygame.display.update()
    return(backButtonHit, forwardButtonHit)#Return status

def drawButtons():#Draw the FW and BW buttons 
    pygame.draw.rect(win,(0,0,0),(50,30,100,55))
    pygame.draw.rect(win,(0,0,255),(55,35,90,45))
   
    pygame.draw.rect(win,(0,0,0),(850,30,100,55))
    pygame.draw.rect(win,(0,0,255),(855,35,90,45))
    win.blit(backTM, (75,45))
    win.blit(forwardTM, (875,45))
    pygame.display.update()
    
def formula():#Draw the formula for the wager activity
    printText(menuFont,"Calculate the wager",400,50)
    pygame.draw.rect(win,(255,255,255),(600,125,350,400))
    pygame.draw.line(win,(0,0,0),(600,320),(950,320))
    printText(cardfont,"Betting Formula: W = B(T-1)",700,190)
    printText(cardfont,"For W = wager, B = betting unit and T = true count",625,250)
    printText(cardfont,"True Count: T = R / D",730,380)
    printText(cardfont,"For T = true count, R = running count and D = number of decks ",605,440)
    pygame.draw.rect(win,(255,255,255),(100,270,320,150))
   
def checkWin(condition,func):#Checkif user got question right
    if func()==condition:
        printText(menuFont,"That is correct",375,170)
        pygame.display.update()
        time.sleep(1.5)
        phase1 = False
        return 1
    return 0
def printText(font,text,x,y):#Condensed text rendering
    textT = font.render(text,True,(0,0,0))
    win.blit(textT,(x,y))
    pygame.display.update()
################################ B L A C K J A C K   T U T O R I A L    A S S E T S###################

#Tutorial Slides    

SlideM = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide.jpg').convert_alpha()
Slide0 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (1).jpg').convert_alpha()
Slide1 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (2).jpg').convert_alpha()
Slide2 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (3).jpg').convert_alpha()
Slide3 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (4).jpg').convert_alpha()
Slide5 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (5).jpg').convert_alpha()
Slide6 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (6).jpg').convert_alpha()
Slide7 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (7).jpg').convert_alpha()
Slide9 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (8).jpg').convert_alpha()
Slide10 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (9).jpg').convert_alpha()
Slide11 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (10).jpg').convert_alpha()
Slide12 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (11).jpg').convert_alpha()
Slide13 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (12).jpg').convert_alpha()
Slide14 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (13).jpg').convert_alpha()
Slide15 = pygame.image.load(r'C:\Users\Zoltan\Downloads\Card Counting Guide (14).jpg').convert_alpha()

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

pageIndex = 0
subIndex = 0
change = subIndex
tutorial = [1,2,4,5,7,8,11,12,13,14,15]
simulation = [3,6,9,10]
inTutorial = True

######      B  L  A  C  K  J  A  C  K      G A M E    A S S E T S       ######

pygame.init()
pygame.display.set_mode()
pygame.font.get_init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,50)
win = pygame.display.set_mode((1000,675)) #creates a surface

p1total = 0
dealertotal = 0
money = 10000
count = 0
truecount = 0
odds = 0
teachnique = 0
teachnique2 = 1
decks = 1

cardfont = pygame.font.SysFont("timesnewroman", 13) #fonts and sizes
bigfont = pygame.font.SysFont("timesnewroman", 18)
titlefont = pygame.font.SysFont("timesnewroman", 42)
massivefont = pygame.font.SysFont("timesnewroman", 48)

decktxt = bigfont.render("How may decks do you want to play with", True, (0, 0, 0))
choosetxt = bigfont.render("Choose a teachnique to start", True, (0, 0, 0))
addtxt = massivefont.render("+", True, (0, 0, 0))
subtxt = massivefont.render("-", True, (0, 0, 0))

cardcountingtxt=titlefont.render("Card Counting",True,(0,0,0))
companiontxt=titlefont.render("Companion",True,(0,0,0))
shuffletxt=bigfont.render("Shuffling the deck",True,(0,0,0))
hit_word = bigfont.render("Hit", True, (0, 0, 0)) #words
stand_word = bigfont.render("Stand", True, (0, 0, 0))
double_word = bigfont.render("Double", True, (0, 0, 0))
blackjack = bigfont.render("Blackjack", True, (0, 0, 0))
bust_word = bigfont.render("Bust", True, (0, 0, 0))
push_word = bigfont.render("Push", True, (0, 0, 0))

you_lose = bigfont.render("You Lose", True, (0, 0, 0))
you_win = bigfont.render("You win", True, (0, 0, 0))

YourAmount = bigfont.render("You have:", True, (0, 0, 0))

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

##heart = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\heart.png').convert_alpha()##immages for the suits
##spade = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\spade.png').convert_alpha()
##club = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\club.png').convert_alpha()
##diamond = pygame.image.load(r'C:\Users\royzh\Photos for School\Poker\diamond.png').convert_alpha()
##
heart = pygame.image.load(r'C:\Users\Zoltan\Downloads\heart.png').convert_alpha()##immages for the suits
spade = pygame.image.load(r'C:\Users\Zoltan\Downloads\spade.png').convert_alpha()
club = pygame.image.load(r'C:\Users\Zoltan\Downloads\club.png').convert_alpha()
diamond = pygame.image.load(r'C:\Users\Zoltan\Downloads\diamond.png').convert_alpha()

pygame.display.set_caption("Black Jack")#sets the name of the window

splithand1 = []
splithand2 = []
user1cards = []#card lists for players
dealercards = []

player1locationsx=[300,320,340,380] #card locations
player1locationsy=[370,382,294,306]

dealerlocationsx=[300,320,340]
dealerlocationsy=[70,82,94]
suits = ['s','c','h','d']
cardValues = ['A','2','3','4','5','6','7','8','9','0','J','Q','K']
deck = [] #deck and discard pile
deaddeck = []
   
for card in range(0,13): #starts by creating a deck
    for suit in range(0,4):
        deck.append(cardValues[card]+suits[suit])
random.shuffle(deck)
print(deck)

class TextBox(pygame.sprite.Sprite):# class for inputing wager
  def __init__(self): #initialize starting text
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = bigfont
    self.image = bigfont.render("Wager an amount:", False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.sumOfWager = 0
    self.numDigit = 0
  def add_chr(self, char): #accepting a proper number
    if char in validChars:
       
        if self.text=='' and char =="0":
            pass
        else:
            self.numDigit +=1
            self.text += char
            self.sumOfWager += int(char)*10^(self.numDigit-1)
    elif char in validChars:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self): #update display 
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos
   
def checkdeck(deck,deaddeck):
    if deck ==[]: #if the deck is empty,
        win.blit(shuffletxt,(500,200))
        pygame.display.update()
        print("shufl")
        time.sleep(3)
        pygame.draw.rect(win,(255,255,255),(500,200,200,100))
        deck=deaddeck
        random.shuffle(deck)
        deaddeck=[]
        count=0#restes the count
        return deck,deaddeck
   
    else:
        return deck,deaddeck
   
def betamount(truecount,money): #calculates the amount the user should bet
    suggestion=money/1000*round((truecount-1),1)#amount formula
    if suggestion<=0:
        betamounttxt = bigfont.render("Suggested bet: Minimum bet ($2)", True, (0, 0, 0))
    else:        
        betamounttxt = bigfont.render("Suggested bet: "+ str(suggestion), True, (0, 0, 0))
    win.blit(betamounttxt,(720,500))
       
def companion(x,y,l,t): #displayes the count, true count and lets the user
    pygame.draw.rect(win,(255,255,255), (705,180,300,400))
   
    hilowtxt = bigfont.render("Hi-low", True, (0, 0, 0)) # definitions of teachnique text
    zencounttxt = bigfont.render("Zen-count", True, (0, 0, 0))
    halvestxt = bigfont.render("Halves", True, (0, 0, 0))  
    countIstxt = bigfont.render("The running count is:  " + str(count), True, (0, 0, 0))
    trueCountIstxt = bigfont.render("The true count is:  " + str(truecount), True, (0, 0, 0))
   
    win.blit(cardcountingtxt,(720 , 20))#displays the count true count and Title
    win.blit(companiontxt,(740 , 70))
    win.blit(countIstxt,(720 , 400))
    win.blit(trueCountIstxt,(720 , 450))
   
    pygame.draw.rect(win,(0,0,0), (715,200,80,40)) #black outline to the buttons
    pygame.draw.rect(win,(0,0,0), (715,260,80,40))
    pygame.draw.rect(win,(0,0,0), (715,320,80,40))
   
    if (x>=715 and x<=795 and y>=200 and y<=240): #highlight buttons if hovering over
        pygame.draw.rect(win,(200,255,200), (716,201,78,38))
    else:
        pygame.draw.rect(win,(255,255,255), (716,201,78,38))
    if (x>=715 and x<=795 and y>=260 and y<=300):
        pygame.draw.rect(win,(200,255,200), (716,261,78,38))
    else:
        pygame.draw.rect(win,(255,255,255), (716,261,78,38))
    if (x>=715 and x<=795 and y>=320 and y<=360):
        pygame.draw.rect(win,(200,255,200), (716,321,78,38))
    else:
        pygame.draw.rect(win,(255,255,255), (716,321,78,38))

    if (x>=715 and x<=795 and y>=200 and y<=240 and l==1):#if user clicks on the buttons
        t = 1
    elif (x>=715 and x<=795 and y>=260 and y<=300 and l==1):
        t = 2
    elif (x>=715 and x<=795 and y>=320 and y<=360 and l==1):
        t = 3

    if t ==1 :#draws the coloured button and word
        pygame.draw.rect(win,(0,255,0), (716,201,78,38))
    win.blit(hilowtxt,(716,201))
    if t ==2 :
        pygame.draw.rect(win,(0,255,0), (716,261,78,38))
    win.blit (zencounttxt, (716,261))
    if t == 3 :
        pygame.draw.rect(win,(0,255,0), (716,321,78,38))
    win.blit (halvestxt,(716,321))

    pygame.display.update()
    return t

def bet(usable_money): #allows the player to wager an amount of money
    textBox = TextBox()
    textBox.rect.center = [340, 545]
    running = True
    while running:
      pygame.draw.rect(win,(255,255,255), (250,535,200,50))
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
                textBox.sumOfWager //= 10
                print("WAGER:",textBox.sumOfWager)
                textBox.update()
            if e.key == pygame.K_RETURN and textBox.text!="": #when enter is hit the string is returned
                if usable_money < int(textBox.text):
                    continue
                elif len(textBox.text) > 0:
                    print (textBox.text)
                    return textBox.text

def deal(user): #deals a card to the player using lists    
    deaddeck.append(deck[0])
    user.append(deck[0])
    deck.remove(deck[0])
    return (user[-1])

def killgame(): #exits the game
    pygame.display.quit()
    pygame.quit()
    exit()    
   
def checkquit(): #checks if the big X in the corrner is hit
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killgame()            

def buttons(x,y,l): #highlighs and displays buttons

    hit_button=0#defines button initial states
    stand_button=0
    double_button =0
   
    pygame.draw.line(win, (0,0,0), (700,0), (700,675))#draws divider line between companion
   
    if (x>=100 and x<= 200 and y>=600 and y<=650): #hit button and highlight
        pygame.draw.rect(win,(0,255,0), (100,600,100,50))
        if (l==1):
            hit_button=1      
    else:
        pygame.draw.rect(win,(5,200,5), (100,600,100,50))
        hit_button=0
    win.blit(hit_word,(135,615))

    if (x>=500 and x<= 600 and y>=600 and y<=650): #stand button and highlight
        pygame.draw.rect(win,(255,0,0), (500,600,100,50))
        if (l==1):
            stand_button=1      
    else:
        pygame.draw.rect(win,(200,5,5), (500,600,100,50))
        stand_button=0
    win.blit(stand_word,(525 , 615))
   
    if (x>=300 and x<= 400 and y>=600 and y<=650): #double button and highlight
        pygame.draw.rect(win,(100,100,255), (300,600,100,50))
        if (l==1):
            double_button = 1
    else:
        pygame.draw.rect(win,(50,50,200), (300,600,100,50))
        double_button=0
    win.blit(double_word,(320 , 615))

    pygame.draw.rect(win,(255,255,255), (0,250,100,50)) #covers the and re-displays the money  
    win.blit(YourAmount,(15, 250 ))
    win.blit(MoneyDisplay,(15, 280 ))
   
    pygame.display.update()
    return (hit_button, stand_button, double_button)#returns state of the hit,stand,double button    
   
def drawcard (card, placex, placey): #draws the correct card in the correct spot with the suit in the corner
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
       # win.blit(heart, (placex+40,placey+60))
    elif card[1] == 's':
        win.blit(spade, (placex+2,placey+17))
       # win.blit(heart, (placex+40,placey+60))

    elif card[1] == 'd':
        win.blit(diamond, (placex+2,placey+17))
       # win.blit(heart, (placex+40,placey+60))

    elif card[1] == 'c':
        win.blit(club, (placex+2,placey+17))
        #win.blit(heart, (placex+40,placey+60))

    pygame.display.update()
    return player  

    #dealertotal+= drawcard(dealercards[-1],dealerlocationsx[1],dealerlocationsy[1])
##    return (p1total, dealertotal)
def insurance(x,y,l,w):
    buyInsurancetxt = bigfont.render("Buy insurance", True, (0, 0, 0))
    insurancetxt= bigfont.render("Insurance", True, (0, 0, 0))
    insurancebet = cardfont.render(str(round(w/2,2)), True, (0, 0, 0))
    clickofftxt = bigfont.render("Click off to decline", True, (0, 0, 0))
    pygame.draw.rect(win,(0,0,0), (430,300,100,50))
    pygame.draw.rect(win,(255,255,255), (431,301,98,48))
    win.blit(buyInsurancetxt, (425,280))
    win.blit(insurancetxt, (440,310))
    win.blit(clickofftxt, (425,360))
   
    if x>=430 and x<=530 and y>=300 and y<=350:
        pygame.draw.rect(win,(200,255,200), (430,300,100,50))
        pygame.draw.rect(win,(255,255,255), (431,301,98,48))
        win.blit(insurancetxt, (440,310))
    if x>=430 and x<=530 and y>=300 and y<=350 and l==1:
        pygame.draw.rect(win,(255,255,255), (425,280,150,180))
        pygame.draw.rect(win,(0,255,0), (430,300,100,50))
        pygame.draw.rect(win,(255,255,255), (431,301,98,48))
        win.blit(insurancetxt, (440,310))
        win.blit(insurancebet, (440,330))
        return (1)
    elif l==1:
        insurance=0
        pygame.draw.rect(win,(255,255,255), (425,280,150,180))
        return(0)
   
def countcard(card,t,count):
    if t==1 and (card[0]=="2" or card[0]=="3" or card[0]=="4" or card[0]=="5" or card[0]=="6"):
        count+=1
    elif t==1 and (card[0]=="0" or card[0]=="J" or card[0]=="Q" or card[0]=="K" or card[0]=="A"):
        count-=1

    if t==2 and (card[0]=="2" or card[0]=="3" or card[0]=="7"):
        count+=1
    elif t==2 and (card[0]=="4" or card[0]=="5" or card[0]=="6"):
        count+=2
    elif t==2 and (card[0]=="0" or card[0]=="J" or card[0]=="Q" or card[0]=="K"):
        count-=2    
    elif t==2 and (card[0]=="A"):
        count-=1

    if t==3 and (card[0]=="2" or card[0]=="7"):
        count+=0.5
    elif t==3 and (card[0]=="4" or card[0]=="3" or card[0]=="6"):
        count+=1
    elif t==3 and card[0]=="5":
        count+=1.5
    elif t==3 and (card[0]=="9"):
        count-=0.5
    elif t==3 and (card[0]=="0" or card[0]=="J" or card[0]=="Q" or card[0]=="K" or card[0]=="A"):
        count-=1    
    return count
###################  T U T O R I A L    L O O P   ######################
while inTutorial:#Tutorial loop
    phase1 = True
    try:#Exit if the user leaves the list
        win.blit(tutorialPages[pageIndex], (0,0))
        pygame.display.update()
        #Implement tap anywhere to start for menu page
        
        if pageIndex == 0:#Page one - Menu #click anywhere to start
            
            pygame.event.get()#mouse shenanigans
            click = pygame.mouse.get_pressed()
            leftclick=click[0]

            if leftclick == 1:
                while True:
                    pygame.event.get()
                    click = pygame.mouse.get_pressed()
                    leftclick=click[0]
                    if leftclick==0:
                        break
                pageIndex+=1  #goes to else                  

        else:#  not the title slide
            subIndex = 0 #resets the answer varriable

            while True:    
                checkquit()  #checks mouse position

                back, forward = tutorialButtons()
                pygame.display.update()

               
                if pageIndex in tutorial:
                    checkquit()
                    ##Print tutorial slides

                    back, forward = tutorialButtons()

                    #pygame.display.update()
                    time.sleep(.05)
                    
                    #Move back or forth depending on button click
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
                      
                    else:
                      win.blit(tutorialPages[pageIndex], (0,0))
                      
                elif pageIndex in simulation: #start of simulations
                    
                    checkquit()
                    ##Move back or forth depending on button click
                    if back:
                        if pageIndex-1>=0:
                            #Reset per page flags
                            pageIndex-=1
                            time.sleep(.5)
                            subIndex = 0
                            phase1 = True
                            break

                    elif forward:
                        #Reset per page flags
                        pageIndex+=1
                        time.sleep(.5)
                        subIndex = 0
                        phase1 = True
                        break
                      
                    else:
                        if pageIndex ==3:
                           
                            if subIndex ==0:
                                while phase1:
                                    #Draw the example of win once
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
                                    #Draw example of blackjack once
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
                                    #Draw example of bust once
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
                                    #Draw example of push once
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
                            #print("HI")
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_RETURN:
                                        #Switch examples if return is hit
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
                                    #Draw question 1 once
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
                                #Check answer
                                subIndex += checkWin("-2",trueCount)
                                if subIndex != change:
                                    phase1 = True
                            elif subIndex ==1:
                                while phase1:
                                    #Draw question 2 once
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
                                #Check answer
                                subIndex += checkWin("4",trueCount)
                                if subIndex!=change:
                                    phase1 = True
                            elif subIndex ==2:
                                while phase1:
                                    #Draw question 3 once
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
                                #Check answer
                                pageIndex += checkWin("0",trueCount)
                                if pageIndex!=change:
                                    phase1 = True
                        elif pageIndex ==9:
                            if subIndex == 0:
                                ####  A C T I V I T Y    1  ####
                                while phase1:
                                    #Draw question 1 for wager
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    change = subIndex
                                    formula()
                                    printText(cardfont,"Calculate the wager. Running count is 12. ",150,310)
                                    printText(cardfont,"There are 3 decks. A betting unit of 100",150,360)
                                    phase1 = False
                                    #Check
                                subIndex += checkWin("300",trueCount1)
                                if subIndex!=change:
                                    phase1 = True
                                print(subIndex)
                            elif subIndex ==1:
                                ####  A C T I V I T Y    2  ####
                                while phase1:
                                    #Draw question 2 for wager
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    change = subIndex
                                    formula()
                                    printText(cardfont,"Calculate the wager. Running count is 24.",150,310)
                                    printText(cardfont,"There are 8 decks. A betting unit of 100",150, 360)
                                    phase1 = False
                                #Check answer
                                subIndex += checkWin("200",trueCount1)
                                if subIndex!=change:
                                    phase1 = True
                                print(subIndex)
                            elif subIndex ==2:
                                ####  A C T I V I T Y    3  ####
                                while phase1:
                                    #Draw question 3 for wager
                                    change = pageIndex
                                    win.blit(tutorialPages[pageIndex], (0,0))
                                    pygame.display.update()
                                    drawButtons()
                                    formula()
                                    printText(cardfont,"Calculate the wager. Running count is -12",150,310)
                                    printText(cardfont,"There are 6 decks. A betting unit of 100",150,335)
                                    printText(cardfont,"The minimum bet is 10",200,360)
                                    phase1 = False
                                #Check answer
                                pageIndex += checkWin("10",trueCount1)
                                if pageIndex!=change:
                                    phase1 = True
                                print(subIndex)
                        elif pageIndex == 10:
                            #####   M E A N I N G F U L   P A I R    #####
                            while phase1:
                                #Draw simulation/example of meaningful pair
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
    except IndexError:#When playerleaves tutorial, stop running tutorial
        inTutorial = False
       
########      E  N  D      O  F     T  U  T  O  R  I  A  L       ########
       
deckstxt = massivefont.render(str(decks), True, (0, 0, 0))#redifines
win.fill((255,255,255)) #refreshed the sceen (white)
win.blit(deckstxt,(350,410))
win.blit(choosetxt, (710,150))
win.blit(decktxt,(200,300))

   
while True: #############   S E T     U P     B L A C K J A C K   ############
   
    checkquit()#gets input from the mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    mousex=mouse[0]
    mousey=mouse[1]
    leftclick=click[0]
    rightclick=click[2]

    deckstxt = massivefont.render(str(decks), True, (0, 0, 0))#redifines

    if (mousex>=200 and mousex<=300 and mousey>=380 and mousey<=480):#highlights - button
        pygame.draw.rect(win,(150,255,150), (200,380,100,100))
    else:
        pygame.draw.rect(win,(0,0,0), (200,380,100,100))
    pygame.draw.rect(win,(255,255,255), (201,381,98,98))
    win.blit(subtxt,(240,400))

    if (mousex>=450 and mousex<=550 and mousey>=380 and mousey<=480):#highlights + button
        pygame.draw.rect(win,(150,255,150), (450,380,100,100))
    else:
       pygame.draw.rect(win,(0,0,0), (450,380,100,100))
    pygame.draw.rect(win,(255,255,255), (451,381,98,98))
    win.blit(addtxt,(490,405))

    if (mousex>=200 and mousex<=300 and mousey>=380 and mousey<=480 and leftclick==1 and decks>1): #will subtract 1 from decks if there is 1 to subtract from
       
        pygame.draw.rect(win,(50,155,50), (200,380,100,100))#redraw buttons
        pygame.draw.rect(win,(255,255,255), (201,381,98,98))
        win.blit(subtxt,(240,400))
       
        decks-=1
        pygame.draw.rect(win,(255,255,255), (350,410,100,100))
        deckstxt = massivefont.render(str(decks), True, (0, 0, 0))#redifines
        win.blit(deckstxt,(350,410))
        while True: #only subtract on realease of mouse
            checkquit()
            mouse = pygame.mouse.get_pos() #gets input from the mouse
            click = pygame.mouse.get_pressed()
            mousex=mouse[0]
            mousey=mouse[1]
            leftclick=click[0]
            rightclick=click[2]
            if leftclick==0:
                break

    if (mousex>=450 and mousex<=550 and mousey>=380 and mousey<=480 and leftclick==1): #will add a deck to the decks
       
        pygame.draw.rect(win,(50,155,50), (450,380,100,100)) #redraws button
        pygame.draw.rect(win,(255,255,255), (451,381,98,98))
        win.blit(addtxt,(490,405))
       
        decks+=1
        pygame.draw.rect(win,(255,255,255), (350,410,100,100))
        deckstxt = massivefont.render(str(decks), True, (0, 0, 0))#redifines
        win.blit(deckstxt,(350,410))        
        while True: #only adds on realeaase of button
            checkquit()
            mouse = pygame.mouse.get_pos() #gets input from the mouse
            click = pygame.mouse.get_pressed()
            mousex=mouse[0]
            mousey=mouse[1]
            leftclick=click[0]
            rightclick=click[2]
            if leftclick==0:
                break

    teachnique = companion(mousex,mousey,leftclick,teachnique)
    if teachnique!=0:
        for i in range(decks-1):
            deck=deck+deck
        random.shuffle(deck)
        print ("deck is",deck)
        break
    pygame.draw.line(win, (0,0,0), (700,0), (700,675))#draws divider line between companion
    pygame.display.update()

while True: ###############  S T A R T     B L A C K J A C K    G A M E  #######################3

    if money==0: #if the user has run out of money, they lose the game
        break
   
    user1cards=[]#resets the user cards and dealer cards
    dealercards=[]
    win.fill((255,255,255)) #refreshed the sceen (white)
    teachnique = companion(0,0,0,teachnique)#diaplays companion car
   
   
    mouse = pygame.mouse.get_pos() #gets input from the mouse
    click = pygame.mouse.get_pressed()
    mousex=mouse[0]
    mousey=mouse[1]
    leftclick=click[0]
    rightclick=click[2]
   

    MoneyDisplay = bigfont.render("$"+str(money), True, (0, 0, 0))

    hit,stand,double = buttons(mousex,mousey,leftclick)
    betamount(truecount,money)
    wager = int(bet(money))
    money = round(money - wager)
    pygame.draw.rect(win,(255,255,255), (0,250,100,50))
    MoneyDisplay = bigfont.render("$"+str(money), True, (0, 0, 0))
    hit,stand,double = buttons(mousex,mousey,leftclick)
    print (money)


    deck,deaddeck=checkdeck(deck,deaddeck)
    deal(user1cards) #deals the user 2 face up cards
    count = countcard(user1cards[-1],teachnique,count)
    truecount= round(count/decks,1)
    print ("true count is", truecount)
    p1total= drawcard(user1cards[-1],player1locationsx[0],player1locationsy[0])
    teachnique = companion(0,0,0,teachnique)
    time.sleep(.5)
    deck,deaddeck=checkdeck(deck,deaddeck)
    deal (user1cards)
    count = countcard(user1cards[-1],teachnique,count)
    truecount=round(count/decks,1)
    print ("countis",count)
    p1total += drawcard(user1cards[-1],player1locationsx[1],player1locationsy[1])
    teachnique = companion(0,0,0,teachnique)
    time.sleep(1)
   
    deck,deaddeck=checkdeck(deck,deaddeck)
    deal(dealercards)#Deals the dealer a face down card
    pygame.draw.rect(win,(0,0,0), (dealerlocationsx[0],dealerlocationsy[0],80,120))
    pygame.display.update()
    teachnique = companion(0,0,0,teachnique)
    time.sleep(.5)

    deck,deaddeck=checkdeck(deck,deaddeck)
    deal(dealercards)#Deas the dealer a Face up card
    count = countcard(dealercards[-1],teachnique,count)
    truecount=round(count/decks,1)
    print ("countis",count)
    dealertotal= drawcard(dealercards[-1],dealerlocationsx[1],dealerlocationsy[1])  

    p1num_of_cards=0 #resets varriables
    dealer_num_of_cards=0
    hitted=0
    insure=2    
   
    while True:#########################User clicks buttons

        p1bust=0
        checkquit()
       
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mousex=mouse[0]
        mousey=mouse[1]
        leftclick=click[0]
        rightclick=click[2]
        hit,stand,double = buttons(mousex,mousey,leftclick)
        #teachnique = companion(mousex,mousey,leftclick,teachnique)

        if insure==2: #checks if
            if dealercards[1][0] == "A" :
                if insurance(mousex,mousey,leftclick,wager) == 1:
                    insure = 1
                    money-= round(wager/2)
                    MoneyDisplay = bigfont.render("$"+ str(money), True, (0, 0, 0))
                    buttons(0,0,0)
                elif insurance(mousex,mousey,leftclick,wager) == 0:
                    insure = 0
            else:
                insure=0
            continue      

       
        if double == 1 and hitted == 0 and money-wager>=0: #if double button is hit
            money-=wager
            wager+=wager
            hit=1
            MoneyDisplay = bigfont.render("$"+str(money), True, (0, 0, 0))
            buttons(0,0,0)

            wagureDisplay = bigfont.render(str(wager), True, (0, 0, 0))
            win.blit(wagureDisplay,(340,550))
            pygame.display.update()
   
        if hit == 1: #if hit button is hit
            hitted=1
            p1num_of_cards+=1
            deck,deaddeck=checkdeck(deck,deaddeck)
            deal (user1cards)
            count = countcard(user1cards[-1],teachnique2,count)
            truecount=round(count/decks,1)
            print ("countis",count)
            p1total += drawcard(user1cards[-1],320+20*p1num_of_cards,382+12*p1num_of_cards)
            print(user1cards)
            print("--------------------------")
            print(dealercards)
            time.sleep(1)
            if p1total>21 and "As" in user1cards:
                    user1cards.remove("As")
                    p1total-=10
            if p1total>21 and "Ac" in user1cards:
                    user1cards.remove("Ac")
                    p1total-=10
            if p1total>21 and "Ad" in user1cards:
                    user1cards.remove("Ad")
                    p1total-=10
            if p1total>21 and "Ah" in user1cards:
                    user1cards.remove("Ah")
                    p1total-=10
                   
            if p1total >21:              
                p1bust = 1
                break
            if double ==1:
                break
            companion(mousex,mousey,leftclick,teachnique)

        if stand == 1 or p1total==21:
            break

    if p1bust ==1:
        win.blit(bust_word,(290 , 340 ))
        pygame.display.update()
        time.sleep(1)
        continue
    else: #### dealer procedure##################################################################
        time.sleep(1)
        print (dealercards)
        dealertotal+= drawcard(dealercards[0],dealerlocationsx[0],dealerlocationsy[0])
        count = countcard(dealercards[0],teachnique2,count)
        truecount=round(count/decks,1)
        print ("countis",count)
        drawcard(dealercards[-1],dealerlocationsx[1],dealerlocationsy[1])
        companion(mousex,mousey,leftclick,teachnique)
        time.sleep(1)
       
        if insure==1 and dealertotal==21: ####dealing with the the insurance
            money+= round(wager +wager/2)
            MoneyDisplay = bigfont.render("$"+ str(money), True, (0, 0, 0))
            buttons(0,0,0)
            time.sleep(2)
        else:
            pygame.draw.rect(win,(255,255,255), (425,280,150,120))
       
        if (dealertotal==21 and len(dealercards)==2) and (p1total ==21 and len(user1cards)==2): #checks if the dealer has a black jack
            win.blit(push_word,(290,340 ))
            money+=wager
            pygame.display.update()
            time.sleep(3)
            continue            

        if p1total == 21 and len(user1cards)==2:
            win.blit(blackjack,(290 , 340 ))
            money += round(wager+wager*3/2)
            pygame.display.update()
            time.sleep(3)
            continue
        while True: ###checking if ace is treated as 10 or 1
            if dealertotal>21 and "As" in dealercards:
                    dealercards.remove("As")
                    dealertotal-=10
            if dealertotal>21 and "Ac" in dealercards:
                    dealercards.remove("Ac")
                    dealertotal-=10
            if dealertotal>21 and "Ad" in dealercards:
                    dealercards.remove("Ad")
                    dealertotal-=10
            if dealertotal>21 and "Ah" in dealercards:
                    dealercards.remove("Ah")
                    dealertotal-=10
                           
            if dealertotal >21:
                break
            elif dealertotal >16:
                break
            dealer_num_of_cards+=1
            deck,deaddeck=checkdeck(deck,deaddeck)
            deal(dealercards)
            count = countcard(dealercards[-1],teachnique2,count)
            truecount=round(count/decks,1)
            print ("countis",count)
            companion(0,0,0,teachnique2)
            dealertotal += drawcard(dealercards[-1],320+20*dealer_num_of_cards,82+12*dealer_num_of_cards)
            time.sleep(1)          

        if (dealertotal>p1total and dealertotal<22):#player loses, dealer has higher total  
            win.blit(you_lose,(290,340 ))
            pygame.display.update()
            time.sleep(3)
            continue
        elif (dealertotal==p1total) or (len(user1cards)==2 and p1total==21 and dealertotal ==21and len(dealercards) ==2): #push, dealer and player ties
            win.blit(push_word,(290,340 ))
            money+=wager
            pygame.display.update()
            time.sleep(3)
            continue
           
        else:#player wins if the dealer doesn't lose
            money +=wager*2
            win.blit(you_win,(290,340))
            pygame.display.update()
            time.sleep(3)
            continue
       

quitgame()
