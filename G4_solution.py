import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (135, 206, 235)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (300, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C4")
building=pygame.Rect(100,100,100,400)
door=pygame.Rect(130,440,40,60)
carryOn=True
while carryOn:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      carryOn = False             
  screen.fill(LIGHTBLUE)
  pygame.draw.rect(screen,(0,0,0),building)
  pygame.draw.rect(screen,WHITE,door)
  #Create a for loop to run from 1 to 3
  for i in range(1,4):
    #Create a rectangle object "window"
    window=pygame.Rect(130,100*i+50,40,40)
    #Draw the rectangle on the screen
    pygame.draw.rect(screen,YELLOW,window)
  pygame.display.flip()
pygame.quit()
