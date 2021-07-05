import pygame
import random
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (200, 400)

player=pygame.Rect(100,380,20,20)
end=pygame.Rect(0,0,200,10)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C3")
carryOn = True
while carryOn:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(YELLOW)
  pygame.draw.rect(screen,RED,end)

  #Check if event type is "KEYDOWN"
  if event.type == pygame.KEYDOWN:
    #Check if event key is "K_RIGHT"
    if event.key == pygame.K_RIGHT:
      #Check if x-coordinate of "player" is less than 170
      if player.x<=170:
        #Increment x-coordinate of "player" by 10
        player.x=player.x+10
    #Check if event key is "K_LEFT"
    if event.key == pygame.K_LEFT:
      #Check if x-coordinate of "player" is greater than 0
      if player.x>=0:
        #Decrement x-coordinate of "player" by 10
        player.x=player.x-10
    #Check if event key is "K_UP"
    if event.key == pygame.K_UP:
      #Check if y-coordinate of "player" is greater than 0
      if player.y>=0:
        #Decrement y-coordinate of "player" by 10
        player.y=player.y-10
    #Check if event key is "K_DOWN"
    if event.key == pygame.K_DOWN:
      #Check if y-coordinate of "player" is less than 370
      if player.y<=370:
        #Increment y-coordinate of "player" by 10
        player.y=player.y+10

  
  for i in range(1,9):
    obstacle=pygame.Rect(50+random.randint(-70,150),i*40,20,10)
    pygame.draw.rect(screen,(0,0,0),obstacle)
    if obstacle.collidepoint(player.x,player.y):
      screen.fill(YELLOW)
      font = pygame.font.Font(None, 34)
      text = font.render("GAME OVER", 1, RED)
      screen.blit(text, (50,150))
      pygame.display.flip()
      pygame.time.wait(2000)
      break

  pygame.draw.rect(screen,LIGHTBLUE,player)
  pygame.time.wait(200)
  pygame.display.flip()

  if end.collidepoint(player.x,player.y):
      screen.fill(YELLOW)
      font = pygame.font.Font(None, 34)
      text = font.render("YOU WON", 1, RED)
      screen.blit(text, (50,150))
      pygame.display.flip()
      pygame.time.wait(2000)
      break 
pygame.quit()
