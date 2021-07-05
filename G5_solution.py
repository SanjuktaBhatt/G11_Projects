import pygame
import random
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
COLOR=[WHITE,DARKBLUE,LIGHTBLUE,RED,ORANGE,YELLOW]
size = (400, 400)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C5")
#Create "carryOn" variable and set to true
carryOn = True
#Begin the while loop
while carryOn:
  #Iterate through each event
  for event in pygame.event.get():
    #Identify is user has quit 
    if event.type == pygame.QUIT: 
      #change "carryOn" to False
      carryOn = False 
  discolight_color=random.choice(COLOR)            
  screen.fill(discolight_color)
  pygame.display.flip()
pygame.quit()
