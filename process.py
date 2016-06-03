#PROCESS
import pygame, sys, classes, random
#pygame.init()
def process(bug, FPS, totalFrames):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			SystemExit 
		if event.type ==  pygame.KEYDOWN:
			if event.key == pygame.K_e:
				classes.BugProjectile.fire = not classes.BugProjectile.fire

	keys = pygame.key.get_pressed() #returs list of all the keys cif they were pressed 	(list of 0,1)
#HorizontalMovement
	if keys[pygame.K_d]:
		classes.Bug.goingRight = True
		bug.image = pygame.image.load("bug.png")
		bug.velx = 5
	elif keys[pygame.K_a]:
		classes.Bug.goingRight = False
		bug.image = pygame.image.load("bugflipped.png")
		bug.velx = -5
	else: 
		bug.velx = 0 
		#verticalMovement. 
	if keys[pygame.K_w]:
		bug.jumping = True
	
	if keys[pygame.K_SPACE]:
 
 #on pressing the e key and then SPACEBAR, it will fire the frosts, and
 # again on pressing e key and SPACEBAR, will reset to Fire mode on.
		def direction():
			if classes.Bug.goingRight:
				p.velx = 8
			else:
				p.image = pygame.transform.flip(p.image, True, False)
				p.velx = -8	
		if (classes.BugProjectile.fire):
			p = classes.BugProjectile(bug.rect.x, bug.rect.y,True ,"fire.png")
			direction()
		else:
			p = classes.BugProjectile(bug.rect.x, bug.rect.y, False ,"frost.png")
			direction()

	spawn(FPS,totalFrames)
	collisions()

	#PROCESS
def spawn(FPS, totalFrames):
	fourSec = FPS*4
	if totalFrames % fourSec == 0:
		r = random.randint(1,2)
		x = 1
		if r == 2: 
			x = 640 - 40
		classes.Fly(x, 130,"fly.png")
		#flies can start from either way, R->L or L->R

def collisions():
	for fly in classes.Fly.List:
		projectiles = pygame.sprite.spritecollide(fly,classes.BugProjectile.List, True)
		for projectile in projectiles:
			fly.health = 0

			if projectile.if_this_variable_is_true_then_fire:
				fly.image = pygame.image.load("burnt_fly.png") #fire projectile
			else:

				if fly.velx > 0:
					fly.image = pygame.image.load("frozen_fly.png") #frost.
				elif fly.velx < 0:	
					fly.image = pygame.image.load("frozen_fly.png") #frost.
					fly.image = pygame.transform.flip(fly.image, True, False) #frost.
			
			projectile.rect.x = 2 * -projectile.rect.width
  			projectile.destroy()			
