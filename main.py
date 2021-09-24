# Basic Pygame Structure

import pygame                               # Imports pygame and other libraries
import random

# Define Classes (sprites) here
class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.timecreated = pygame.time.get_ticks()  # note the time the object is created
        self.image = pygame.Surface([30,30])        # Create a surface on which to display the graphics
        self.image.set_colorkey(black)              # Set a colour to be transparent

        self.rect = self.image.get_rect()           # these lines create the rectangular sprite,
        self.rect.x = random.randint(0,670)         # the same size as the image surface and then
        self.rect.y = 0                             # assigns it coordinates

    def setImage(self,graphicSelected):
        fallingObjectsImage = pygame.image.load(graphicSelected)  # load in the passed image file
        self.image.blit(fallingObjectsImage,(0,0))                # draw the graphic on the surface

    def moveFallingObjects(self,distance):
        if self.rect.y <= 470:
          self.rect.y = self.rect.y + distance

    def deleteFallingObjects(self):
       if self.rect.y > 470:                         # check if sprite at bottom of window
             self.kill()                             # kill (delete) object if it is at bottom


class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,68])         # note the change in the surface size of the larger sprite
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = 420

        self.image.blit(pygame.image.load("Superhero.png"), (0,0))

    def moveCharacter(self,movement):
        if self.rect.x >= and self.rect.x <= 645
            self.rect.x = self.rect.x + movement

pygame.init()                               # Pygame is initialised (starts running)

screen = pygame.display.set_mode([700,500])  # Set the width and height of the screen [width,height]
pygame.display.set_caption("Dylan's Game")       # Name your window
background_image = pygame.image.load("OrchardBackground.jpg").convert()
done = False                                # Loop until the user clicks the close button.
clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
black    = (   0,   0,   0)                 # Define some colors usi`ng rgb values.  These can be
white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

# Define additional Functions and Procedures here
allFallingObjects = pygame.sprite.Group()

nextApple = pygame.time.get_ticks() + 2500   # how long until first apple appears (milliseconds) equal to 2.5 seconds

charactersGroup = pygame.sprite.Group()
character = Character()
charactersGroup.add(character)

movement = 0

# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get():        # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:       # If user clicked close window
            done = True                     # Flag that we are done so we exit this loop

    # Update sprites here
    if pygame.time.get_ticks() > nextApple:
        nextObject = FallingObject()
        nextObject.setImage("Apple.png ")
        nextApple = pygame.time.get_ticks() + 1500

        allFallingObjects.add(nextObject)

    for eachObject in (allFallingObjects.sprites()):     # loops through each object in a group
        eachObject.moveFallingObjects(5)                 # 5 = 5pixels down in window


        eachObject.deleteFallingObjects()

    screen.blit(background_image, [0,0])
    allFallingObjects.draw(screen)
    charactersGroup.draw(screen)
    pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
    clock.tick(20)                          # Limit to 20 frames per second

pygame.quit()                               # Close the window and quit.

