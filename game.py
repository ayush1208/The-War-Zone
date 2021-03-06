import pygame
import time
import math
import random
pygame.init()
pygame.font.init()
win=pygame.display.set_mode((1000,500))
music=pygame.mixer.music.load('gameofthrones.mp3')	#Background Music
pygame.mixer.music.play(-1)	#Playing the background music
bg=pygame.image.load('bg.png')	#Background image
bg=pygame.transform.scale(bg,(1000,500))	#Scaling
run=1
while run==1:
	pygame.display.set_caption("The War Zone")
	win.blit(bg,(0,0))	#Displaying the background
	pygame.time.delay(50)
	pygame.draw.rect(win,(0,255,0),(400,100,250,45))	#Mode 1 on front screen
	pygame.draw.rect(win,(0,255,0),(400,200,250,45))	#Mode 2 on front screen 
	pygame.draw.rect(win,(0,255,0),(400,300,250,45))	#Help on front screen
	pygame.draw.rect(win,(0,255,0),(400,400,250,45))	#Quit on front screen
	font=pygame.font.SysFont("Comic Sans Ms",30)	#Font1 Assign
	font1=pygame.font.SysFont("Comic Sans Ms",50)	#Font2 Assign
	font2=pygame.font.SysFont("Comic Sans Ms",10)	#Font3 Assign
	text1=font.render("Mode 1",False,(255,0,0))
	text2=font.render("Mode 2",False,(255,0,0))
	text3=font.render("Help",False,(255,0,0))	#Text for blitting
	text4=font.render("Quit",False,(255,0,0))
	text5=font1.render("The War Game",False,(255,0,0))
	win.blit(text5,(350,10))
	win.blit(text1,(475,108))
	win.blit(text2,(475,208))	#Displaying the texts
	win.blit(text3,(480,303))
	win.blit(text4,(480,403))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=0
	pygame.mouse.get_pressed()
	if event.type==pygame.MOUSEBUTTONDOWN:
		if(pygame.mouse.get_pos()[0]>400 and pygame.mouse.get_pos()[0]<650 and pygame.mouse.get_pos()[1]>100 and pygame.mouse.get_pos()[1]<145):
			
					pygame.time.delay(100)
					x1=60    #Initial x coordinate of left tank
					y1=425   #Initial y coordinate of left tank
					width1=40
					height1=60                     #Mode 1
					x2=830  #Initial x coordinate of right tank 
					y2=425  #Initial y coordinate of right tank
					x3=400  #Initial x coordiante of power bar
					y3=50   #Initial y coordiante of power bar
					width3=10 #Height and width of power bar
					height3=10
					vel3=10  #Power bar's velocity
					x4=400
					y4=50
					bg1=pygame.image.load('war1.png')	#Background
					bg1=pygame.transform.scale(bg1,(1000,500))
					char1=pygame.image.load('2a.png')
					char2=pygame.image.load('2.png')
					char3=pygame.image.load('canonball.png')	#Images in the mode 1
					char4=pygame.image.load('dewaar1.png')
					char5=pygame.image.load('blast.png')
					sound1=pygame.mixer.Sound('Explosion1.wav')	#Blast sound
					run1=1
					k=0
					vy=30   #Initial y velocity
					xl=130  #Initial x coordinate of cannon ball of left tank
					yl=425  #Initial y coordinate of cannon ball of left tank
					xr=830  #Initial x coordinate of cannon ball of right tank
					yr=425  #Initial y coordinate of cannon ball of right tank
					c=0     
					health1=7
					health2=7
					while run1==1:
						pygame.display.set_caption("Mode 1")
						life1=font.render("Lives: "+str(health1),False,(255,0,0))#Health for left tank
						life2=font.render("Lives: "+str(health2),False,(255,0,0))#Health for right tank
        					pygame.time.delay(50)
        					for event in pygame.event.get():
                					if event.type==pygame.QUIT:
                        					run=0
								run1=0
        					keys=pygame.key.get_pressed()
        					if keys[pygame.K_s] and c%2==0:#Firing for left tank
							if x3<=520:
                        					x3+=vel3
                        					pygame.draw.rect(win,(255,0,0),(x3,y3,width3,height3))
						elif keys[pygame.K_DOWN] and c%2==1:#Firing for right tank
							if x4<=520:
                        					x4+=vel3
                        					pygame.draw.rect(win,(255,0,0),(x4,y4,width3,height3))
						elif keys[pygame.K_ESCAPE]:#To Menu
                                                        run1=0
        					else:
                					win.blit(bg1,(0,0))
							win.blit(life1,(30,50))
							win.blit(life2,(850,50))
                					win.blit(char4,(480,350))
                					if(x3>400 and k==0):
                        					vx=((x3-320)/random.randrange(32,38,1)*5.5)#velocity in x direction of cannon
                        					k=1	#For left tank
                					if(x4>400 and k==0):
                        					vx=((x4-320)/random.randrange(32,38,1)*5.5)
                        					k=2	#For right tank
                					if k==1:
                        					vy=vy-2
								yl-=vy         #Projectile physics
                        					xl+=vx
                        					win.blit(bg1,(0,0))
								win.blit(life1,(30,50))    #Left tank
                                                                win.blit(life2,(850,50))	
                        					win.blit(char3,(xl,yl))   #Displaying of all characters
                        					win.blit(char1,(x1,y1))
                        					win.blit(char4,(480,350))
                					if k==2:
                        					vy=vy-2
                        					yr-=vy
                        					xr-=vx                    
                        					win.blit(bg1,(0,0))        #Right tank
								win.blit(life1,(30,50))
                                                                win.blit(life2,(850,50))
                        					win.blit(char3,(xr,yr))
                        					win.blit(char2,(x1,y1))
                        					win.blit(char4,(480,350))

                					if yl>438:
                        					win.blit(char1,(x1,y1))
                        					win.blit(char2,(x2,y2))
                        					xl=x1+70
                        					yl=425          #Checking if the cannon ball has completed its projectie
                        					vy=30
                        					x3=400
                        					k=0
								c+=1
                					if yr>438:
                        					win.blit(char1,(x1,y1))
                        					win.blit(char2,(x2,y2))
                        					xr=x2+20
                        					yr=425
                        					vy=30
                        					x4=400
                        					k=0
								c+=1
							if xl>x2-28 and xl<x2+123 and yl>420 and yl<435: #Checking for collision
                        					for i in range(50):
                                					win.blit(char5,(x2-30,y2-100))
                                					sound1.play()
                               			 			pygame.time.delay(10)
                        					xl=x1+70     
                        					yl=425
                        					vy=30
                        					x3=400
                        					k=0
                        					c+=1
								health2-=1
                					if xr>x1-8 and xr<x1+125 and yr>420 and yr<435:	#Checking for collision
                        					for i in range(50):
                                					win.blit(char5,(x1-30,y1-100))
                                					sound1.play()
                                					pygame.time.delay(10)
                        					xr=x2+20
                        					yr=425
                        					vy=30
                        					x4=400
                        					k=0
                        					c+=1
								health1-=1
							if health1==0:           #Checking for End of game
								msg1=font1.render("Player 2 wins",False,(255,0,0))
								msg2=font.render("For menu press Escape",False,(255,0,0))
								win.blit(msg1,(300,100))
								win.blit(msg2,(300,250))
							if health2==0:            #Checking for End of Game
                                                                msg1=font1.render("Player 1 wins",False,(255,0,0))
                                                                msg2=font.render("For menu press Escape",False,(255,0,0))
                                                                win.blit(msg1,(300,100))
                                                                win.blit(msg2,(300,250))
							
                					if keys[pygame.K_a] and k==0 and x1>5:
                        					x1-=2                                     
                        					xl=x1+70
                					if keys[pygame.K_d] and k==0 and x1<350:         #Controls for movement of left tank
                        					x1+=2
                        					xl=x1+70
                					if keys[pygame.K_LEFT] and k==0 and x2>530:
                        					x2-=2
                        					xr=x2+20
                					if keys[pygame.K_RIGHT] and k==0 and x2<870:     #Controls for movement of right tank
								x2+=2
                        					xr=x2+20
                        					win.blit(char1,(x1,y1))
                        					win.blit(char2,(x2,y2))

                					else:
                        					win.blit(char1,(x1,y1))
                        					win.blit(char2,(x2,y2))
						pygame.display.update()
	if event.type==pygame.MOUSEBUTTONDOWN:
                if(pygame.mouse.get_pos()[0]>400 and pygame.mouse.get_pos()[0]<650 and pygame.mouse.get_pos()[1]>200 and pygame.mouse.get_pos()[1]<245):
					SHeight = 1000
					SWidth = 500
					k=0
					pygame.display.set_caption("Mode 2")                 #Mode 2
					bg = pygame.image.load('bg.png')                     #Background 
					bg= pygame.transform.scale(bg,(SHeight,SWidth))    
					sound1=pygame.mixer.Sound('Explosion1.wav')

					clock = pygame.time.Clock()	

					class plane():                      #Plane class and its characteristics
        					def __init__(self):
                					self.pwidth = 125
                					self.pheight = 75
               						self.plane = pygame.image.load('plane.png')
                					self.plane = pygame.transform.scale(self.plane,(self.pwidth,self.pheight))
                					self.plane2 = pygame.transform.flip(self.plane, True, False)
                					self.px = 0
                					self.py = 30
                					self.pvel = 10

        					def draw(self, win):
                					if self.pvel > 0:
                    						if self.px <  SHeight -self.pwidth - self.pvel:
                        						self.px += self.pvel                    
                    						else:                                          
                        						self.pvel *= -1
									self.px += self.pvel
                					else:                                             #Checking for boundary conditions
                    						if self.px >  - self.pvel:
                        						self.px += self.pvel
                    						else:
                        						self.pvel = self.pvel * -1
                        						self.px += self.pvel
                					if self.pvel<0:
                        					win.blit(self.plane,(self.px,self.py))
                					else:
                        					win.blit(self.plane2,(self.px,self.py))

					P = plane()

					def blast(a):                         #Blast function during collision
        					blastimg = pygame.image.load('blast.png')
        					blastimg = pygame.transform.scale(blastimg,(200,100))
        					win.blit(blastimg,a)
						sound1.play()
						pygame.time.delay(50)
							

					class boy:                                 #Boy class with its characteristics
        					def __init__(self):
                					self.boyimg = pygame.image.load('soldier.png')
                					self.bx =450
                					self.by = 380
                					self.bvel = 4
        					def draw(self,win):
                        				win.blit(self.boyimg,(self.bx,self.by))

        					def right(self):
                					if self.bx < SHeight - self.bvel-60:
                       						self.bx+=self.bvel
                        					self.draw(win)
        					def left(self):                                        #Movement of boy
							if self.bx > self.bvel:
                        					self.bx-=self.bvel
                        					self.draw(win)
       
					class ball():                              #Cannon ball and its characteristics
        					def __init__(self):
                					self.bwidth = 10
                					self.bheight = 10
                					self.ballimg = pygame.image.load('ball.png')
                					self.ballimg = pygame.transform.scale(self.ballimg,(self.bwidth,self.bheight))
                					self.blastimg = pygame.image.load('blast.png')
                					self.blastimg = pygame.transform.scale(self.blastimg,(300,300))
                					self.bx = P.px + P.pwidth/2
                					self.by = P.py + P.pwidth/2
                					self.bvel = 6
                					self.BD  = True
        					def draw(self,win):
                					if self.by < SHeight-self.bwidth:
                        					self.by+=self.bvel
                        					win.blit(self.ballimg,(self.bx,self.by))
                					else:
                        					win.blit(self.ballimg,(self.bx,self.by))
					B = []
					MB = boy()
					def display():
        					global k
						win.blit(bg,(0,0))
        					font=pygame.font.SysFont("Comic Sans Ms",20)
        					font1=pygame.font.SysFont("Comic Sans Ms",50)
        					P.draw(win)
        					MB.draw(win)
        					text1=font.render("Bombs left: "+str(12-len(B)),False,(255,0,0)) #Number of balls left 
        					win.blit(text1,(400,20))
						keys=pygame.key.get_pressed()
        					if keys[pygame.K_LEFT]:      #Movement of boy to left
                					MB.left()
        					if keys[pygame.K_RIGHT]:     #Movement of boy to right
                					MB.right()

        					for i in B:
                					if i.BD:
                        					i.draw(win)
                        					if i.bx>MB.bx+10 and i.bx<MB.bx+50 and i.by>375 and i.by<460:
                                        				k=1                      #Checking for collision
                                        				blast((MB.bx-70,400))
                       						elif(len(B)==12):#Checking for player 2 winning
                                        				text2=font1.render("Player 2 Wins",False,(255,0,0))
                                        				text3=font1.render("For menu press Escape",False,(255,0,0))
                                        				win.blit(text2,(300,100))
									win.blit(text3,(300,200))
                        					if k==1:#Checking for player 1 winning
                                					text2=font1.render("Player 1 Wins",False,(255,0,0))
                                					text3=font1.render("For menu press Escape",False,(255,0,0))
									win.blit(bg,(0,0))
                                					win.blit(text2,(300,100))
									win.blit(text3,(300,200))
									
        					pygame.display.update()

					run2 = True
					a=0
					time=0
					while run2:
        					clock.tick(50)
        					time+=1
        					for event in pygame.event.get():
                					if event.type == pygame.QUIT:
                    						run=0
								run2 = False
								
        					keys = pygame.key.get_pressed()
						if keys[pygame.K_ESCAPE]:  #To Menu
							run2=False
							
        					if keys[pygame.K_SPACE]:#Dropping of bomb
							if a==0:
                        					if len(B)<12 :
                                					B.append(ball())
                                					a+=1
        					else:
                					a=0
						
        					display()
						pygame.display.update()	






	
	if event.type==pygame.MOUSEBUTTONDOWN:
                if(pygame.mouse.get_pos()[0]>400 and pygame.mouse.get_pos()[0]<650 and pygame.mouse.get_pos()[1]>300 and pygame.mouse.get_pos()[1]<345):
					run2=1       
					while run2==1:
						for event in pygame.event.get():                #Help Menu
                                                        if event.type==pygame.QUIT:
                                                                run=0
                                                                run2=0
						
						win.blit(bg,(0,0))
						help1=font.render("Mode 1:",False,(255,0,0))
						help2=font.render("For the 1st player on the left,the tank moves left and right with keys a",False,(255,0,0))
						help3=font.render("and d respectively and fires with the s switch",False,(255,0,0)) 
						help4=font.render("The 2nd player uses the right and left arrow for movement of the tank",False,(255,0,0))
						help5=font.render("and the down arrow for firing, in alternate chances",False,(255,0,0))
						help6=font.render("Mode 2:",False,(255,0,0))
						help7=font.render("For the 1st player the aeroplane drops the bomb with the spacebar and the",False,(255,0,0))
						help8=font.render("second player uses arrow keys for movement of man",False,(255,0,0))
						help9=font.render("For menu press Escape",False,(255,0,0))
						win.blit(help1,(5,20))
						win.blit(help2,(5,50))
						win.blit(help3,(5,80))
						win.blit(help4,(5,110))
						win.blit(help5,(5,140))
						win.blit(help6,(5,250))
						win.blit(help7,(5,280))
						win.blit(help8,(5,310))
						win.blit(help9,(5,360))
						keys=pygame.key.get_pressed()
						if keys[pygame.K_ESCAPE]:
							run2=0
						pygame.display.update()										            
	if event.type==pygame.MOUSEBUTTONDOWN:
                if(pygame.mouse.get_pos()[0]>400 and pygame.mouse.get_pos()[0]<650 and pygame.mouse.get_pos()[1]>400 and pygame.mouse.get_pos()[1]<445):
					run=0			#Quit Option
	pygame.display.update()
pygame.quit()




	
				
				
					
