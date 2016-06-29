import pygame
import sys
import time
import random
try: 
	abc=sys.argv[1]
except:
	abc="Guest: "
pygame.init()
#pygame.mixer.init()
#pygame.mixer.pre_init(44100, -16, 2, 2048)
#pygame.mixer.music.load('midi.midi')
#pygame.mixer.music.play()

size = width,height = 1500,800
speed = [10,10]
speed2 = [0,0]
mycolor = (255, 255, 255)
screen = pygame.display.set_mode(size)
ball = pygame.image.load("communism.jpg");
ball2 = pygame.image.load("usa.jpg")
ballrect = ball.get_rect()
ballrect.x=900
ballrect.y=600
ballrect2 = ball2.get_rect()
ballrect2.x=200
ballrect2.y=100
lasttime = 0
lasttime2 = 0
lasttime3 = 0
lasttime4 = 0
horiz=3
win = True
timeleft=60
center=0
end=0
leaderboard="1"
score="Time remaining: 60"
myfont = pygame.font.SysFont(None, 30)
def enemy():
	enspeedx=random.randint(-20,20)
	enspeedy=random.randint(-20,20)
	return [enspeedx,enspeedy]
while True:
	label = myfont.render(score, 1, (0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				speed2 = [0,0]
			if event.key == pygame.K_UP:
				speed2 = [0,-5]
				horiz=0
			if event.key == pygame.K_DOWN:
				speed2 = [0,5]
				horiz=0
			if event.key == pygame.K_LEFT:
				speed2 = [-5,0]
				horiz=1
			if event.key == pygame.K_RIGHT:
				speed2 = [5,0]
				horiz=1

	if (pygame.time.get_ticks() - lasttime > 1000):
		if center==0:
			speed=enemy()
			lasttime = pygame.time.get_ticks()

	if (pygame.time.get_ticks() - lasttime4 > 10):
		if center==0:
			ballrect = ballrect.move(speed)
			lasttime4 = pygame.time.get_ticks()

	if (pygame.time.get_ticks() - lasttime2 > 10):
		ballrect2 = ballrect2.move(speed2)
		lasttime2 = pygame.time.get_ticks()

	if (pygame.time.get_ticks() - lasttime3 > 1000):
		if win==False:
			leaderboard=str(60-timeleft)
			center=2
		elif timeleft<=0:
			center=1
		else:
			timeleft-=1
			score="Time remaining: "+str(timeleft)
		lasttime3 = pygame.time.get_ticks()

	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1]=-speed[1]
	if ballrect2.left <= 0 or ballrect2.right >= width:
		speed2[0] = -speed2[0]
	if ballrect2.top <= 0 or ballrect2.bottom >= height:
		speed2[1]=-speed2[1]
	if win==True:
		if ballrect.colliderect(ballrect2):
			win=False
			leaderboard=str(60-timeleft)
			speed = [0,0]
			speed2 = [0,0]
			f = open("highscore.txt", 'a')
			f.write(abc +leaderboard + "\n")
			f.close()
			end=0
			break
	screen.fill(mycolor)
	screen.blit(ball,ballrect)
	screen.blit(ball2,ballrect2)	
	if center==0:
		screen.blit(label, (1250, 750))
	elif center==1:
		end=1
		speed=[0,0]
		speed2=[0,0]
		f = open("highscore.txt", 'a')
		f.write(abc +leaderboard + "\n")
		f.close()
		break
	else:
		end=0
		speed=[0,0]
		speed2=[0,0]
		f = open("highscore.txt", 'a')
		f.write(abc +leaderboard + "\n")
		f.close()
		break
	pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	if end==0:
		myfont = pygame.font.SysFont(None, 100)
		label = myfont.render("F*** THE COMMIES.", 1, (0,0,0))
		screen.blit(label, (430, 300))
		myfont2 = pygame.font.SysFont(None, 100)
		if int(leaderboard)==1:
			label2 = myfont2.render("YOU SURVIVED FOR "+leaderboard+" SECOND.", 1, (0,0,0))
		else:
			label2 = myfont2.render("YOU SURVIVED FOR "+leaderboard+" SECONDS.", 1, (0,0,0))
		screen.blit(label2, (185, 450))
	else:
		myfont = pygame.font.SysFont(None, 100)
		label = myfont.render("YOU WIN!!", 1, (0,0,0))
		screen.blit(label, (620, 350))
	pygame.display.flip()