#import pygame library

#Imprt random module

#Call the pygame.init() 

# Colors to choose from
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
#Set screen size

#Create user paddle at (370,200) with dimensions (10,80)

#Create player paddle at (370,200) with dimensions (10,80)

#Choose a random interger between 1 and 5 to set the speed in y direction of the computer's paddle "player"
playery=random.randint(1,5)
#Create a ball at (200,200) with dimensions (10,10)

#Creata "ballx" and "bally" and set values to 1.


#Create two variables "player_score" ,"user_score" and set them to zero

#Create Screen variable

#Set a caption as you wish

#Create "carryOn" and set it to True

#Begin the game loop

  #Iterate through all events using a for loop
  
    #Check if user quit
     
      #Set "carryOn" to False
       
  #Fill screen with a color of your choice            
 
  #Select a font to display the text

  #Display computer score
  
  
  #Display user score

  
  #Forward ball position by chnaging its x and y coordinates.
  
  
  #Ensure ball is within boundaries in y-direction
 

  #Check for computer paddle and ball collision
 

  #Check for user paddle and ball collision
  
  
 
  #If computer is unable to hit add user score
 


  #If user is unable to hit add computer score
  
  
  
  #Draw the ball
 
  #Increment computer paddle movement

  #Ensure computer paddle is within boundaries

  
  #Take user input to move the user paddle

  
  #Draw the paddles on the screen        
  
 
  #Some delay added for better visualizations
  pygame.time.wait(10)
  #Display is updated
  pygame.display.flip()

#Quit game whenever the game loop ends
pygame.quit()
