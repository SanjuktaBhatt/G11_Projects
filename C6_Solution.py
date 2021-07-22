import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,140,10)
YELLOW = (255,255,0)
GREEN=(0,255,0)
BROWN=(165,102,42)
size = (400, 400)
#Use list comprehension to creat a list of bricks for the wall
Y=[pygame.Rect(i*30+15,230,20,20) for i in range(4,11)]
G=[pygame.Rect(i*30+15,170,20,20) for i in range(4,11)]
R=[pygame.Rect(i*30+15,200,20,20) for i in range(4,11)]
B=[pygame.Rect(i*30+15,140,20,20) for i in range(4,11)]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C6")
carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(BROWN)
  pygame.draw.line(screen, WHITE, [88,0], [88,400], 4)
  pygame.draw.line(screen, WHITE, [82,0], [82,400], 4)
  font = pygame.font.Font(None, 34)
  text = font.render("Sports Day", 1, DARKBLUE)

  bgd=pygame.Rect(150,10,130,20)
  pygame.draw.rect(screen,WHITE,bgd)
  screen.blit(text, (150,10))
  
  for i in range(5,80,20):
    for j in range(5,391,20):
      audience=pygame.Rect(i,j,10,10)
      pygame.draw.rect(screen,(0,0,0),audience)
  #Create a for loop to draw each brick
  for i in Y:
    pygame.draw.rect(screen,YELLOW,i)
  for i in G:
    pygame.draw.rect(screen,GREEN,i)
  for i in R:
    pygame.draw.rect(screen,RED,i)
  for i in B:
    pygame.draw.rect(screen,DARKBLUE,i)
  pygame.display.flip()
pygame.quit()
