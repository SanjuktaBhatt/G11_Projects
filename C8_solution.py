#import pygame library
import pygame
#Imprt random module
import random
#Call the pygame.init() 
pygame.init() 
# Colors to choose from
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
#Set screen size
size = (400, 400)
#Create user paddle at (370,200) with dimensions (10,80)
user=pygame.Rect(370,200,10,80)
#Create player paddle at (370,200) with dimensions (10,80)
player=pygame.Rect(20,200,10,80)
#Choose a random interger between 1 and 5 to set the speed in y direction of the computer's paddle "player"
playery=random.randint(1,5)
#Create a ball at (200,200) with dimensions (10,10)
ball= pygame.Rect(200,200,10,10)
#Creata "ballx" and "bally" and set values to 1.
ballx=1
bally=1

#Create two variables "player_score" ,"user_score" and set them to zero
player_score = 0
user_score=0
#Create Screen variable
screen = pygame.display.set_mode(size)
#Set a caption as you wish
pygame.display.set_caption("Project C8")
#Create "carryOn" and set it to True
carryOn = True
#Begin the game loop
while carryOn:
  #Iterate through all events using a for loop
  for event in pygame.event.get():
    #Check if user quit
    if event.type == pygame.QUIT: 
      #Set "carryOn" to False
      carryOn = False 
  #Fill screen with a color of your choice            
  screen.fill(YELLOW)
  #Select a font to display the text
  font = pygame.font.Font(None, 34)
  #Display computer score
  text = font.render("Comp: " + str(player_score), 1, (0,0,0))
  screen.blit(text, (20,5))
  #Display user score
  text2 = font.render("User: " + str(user_score), 1, (0,0,0))
  screen.blit(text2, (300,5))
  #Forward ball position by chnaging its x and y coordinates.
  ball.x+=ballx
  ball.y+=bally
  #Ensure ball is within boundaries
  if ball.y<=0:
    bally=-bally
  if ball.y>=390:
    bally=-bally
  #Check for computer paddle and ball collision
  if player.collidepoint(ball.x,ball.y):
    ballx=-ballx
  #Check for user paddle and ball collision
  if user.collidepoint(ball.x,ball.y):
    ballx=-ballx
  #If computer is unable to hit add user score
  if ball.x<=0:
    ballx=-ballx
    bally=-bally
    user_score+=1
  #If user is unable to hit add computer score
  if ball.x>=390:
    ballx=-ballx
    bally=-bally
    player_score+=1
  #Draw the ball
  pygame.draw.rect(screen,(0,0,0),ball)
  #Increment computer paddle movement
  player.y+=playery
  #Ensure computer paddle is within boundaries
  if player.y<=20 or player.y>=320:
    playery=-playery
  #Take user input to move the user paddle
  if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if user.y>20: 
                user.y-=5
        if event.key == pygame.K_DOWN:
            if user.y<320:
               user.y+=5   
  #Draw the paddles on the screen        
  pygame.draw.rect(screen,DARKBLUE,player)
  pygame.draw.rect(screen,RED,user)
  #Some delay added for better visualizations
  pygame.time.wait(10)
  #Display is updated
  pygame.display.flip()

#Quit game whenever the game loop ends
pygame.quit()
