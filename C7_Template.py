import pygame
import random
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
ASH=(178, 190, 181)
size = (400, 400)
# Create a list of random orer numbers


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C7")
carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(ASH)
  #Choose a font
  
  #Display "PIZZA DELIVERY" in red color at (100,10)
  
  
  #Display "Orders left to be served:" in orange color at (100,10)
  
 
  y=94
  #Create a for loop to ensure the value i in line 34 iterates through each value of the order
  
    text=font.render("Order Number: "+ str(i), 1, ORANGE)
    screen.blit(text, (20,y))
    y+=34
  #Choose a random order using random.choice function
  
  #Remove the order_served from the orders list 
  
  text=font.render("Order Served: "+ str(order_served), 1, DARKBLUE)
  screen.blit(text,(100,300))
  pygame.time.wait(1500)
  pygame.display.flip()
pygame.quit()
