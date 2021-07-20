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
orders=[245,280,279,290,213]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C7")
carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(ASH)
  #Choose a font
  font = pygame.font.Font(None, 34)
  #Display "PIZZA DELIVERY" in red color at (100,10)
  text = font.render("PIZZA DELIVERY ", 1, RED)
  screen.blit(text, (100,10))
  #Display "Orders left to be served:" in red color at (100,10)
  text = font.render("Orders left to be served: ", 1, ORANGE)
  screen.blit(text, (20,50))
  y=94
  #Create a for loop to ensure the value i in line 34 iterates through each value of the order
  for i in orders:
    text=font.render("Order Number: "+ str(i), 1, ORANGE)
    screen.blit(text, (20,y))
    y+=34
  #Choose a random order using random.choice function
  order_served=random.choice(orders)
  #Remove the order_served from the orders list 
  orders.remove(order_served)
  text=font.render("Order Served: "+ str(order_served), 1, DARKBLUE)
  screen.blit(text,(100,300))
  pygame.time.wait(1500)
  pygame.display.flip()
pygame.quit()
