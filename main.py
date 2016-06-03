
import pygame, sys
from pygame.locals import *
from classes import *
from process import *

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode( (SCREENWIDTH,SCREENHEIGHT) )
clock = pygame.time.Clock()
FPS = 24
totalFrames = 0 #keeps track of all the frames created.
background = pygame.image.load("forest.jpg")
bug = Bug(0,100,"bug.png")

#----MainProgramLoop---#

while True:  
	process(bug,FPS,totalFrames)	
	#LOGIC 
	bug.motion(SCREENWIDTH,SCREENHEIGHT)
	Fly.update_all(SCREENWIDTH,SCREENHEIGHT)
	BugProjectile.movement()
	totalFrames += 1
	#LOGIC
	#DRAW
	screen.blit(background, (0,0) )
	BaseClass.allsprites.draw(screen)  
	BugProjectile.List.draw(screen) 
	pygame.display.flip()
	#DRAW
	clock.tick(FPS)