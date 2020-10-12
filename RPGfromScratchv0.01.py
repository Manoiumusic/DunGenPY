#RPGfromScratch by Daniel Manoiu
#v.0.02
#Copyright 2020

######################################
#IMPORT ALL MODULES
#####################################

import os
import random
#import console #this module and all its function calls should be commented out if not running in Pythonista

######################################
#SET ALL CONSTANTS
#####################################

#set game screen size
screenX = 28
screenY = 12

dungeonX = 28
dungeonY = 12

#set player starting position 
playerStartX = 3
playerStartY = 10


##############################################
#START OF GAME - DECLARE AND SET ALL VARIABLES 
##############################################

#populate game screen and place player in starting position
gameScreen = [["•" for i in range(screenX)] for j in range(screenY)] 
gameScreen[playerStartY][playerStartX] = "@"

#set player's current position to starting defaults
playerCurrentX = playerStartX
playerCurrentY = playerStartY

#declaring the variable used for player input
playerMoveDirection = ""

playerName = "TestDummy" #TODO: this will be custom
playerClass = "Pawn" #TODO: player will select class
playerLevel = 1 


######################################
#DEFINING ALL FUNCTIONS
#####################################


def generateDungeon():
		choice = 0
		for i in range(screenY):
			for j in range(screenX):
				choice = random.randint(0,4)
				if choice == 3:
					gameScreen[i][j]= "▓"
				else:
					gameScreen[i][j]= "•"

#this draws the title and version number
def drawTopInfo():
	print("_________________________________")
	print("RPG From Scratch by Daniel Manoiu")
	print("v0.01.00002")
	print("_________________________________")

#this draws the bottom part with the stats
def drawPlayerStats():
	print("_________________________________")
	print (playerName)
	print ("Level " + str(playerLevel) + " " + playerClass)
	print ()

#update function that will be called in tge main game loop 
def Update():
	#this does nothing on iOS but should clear console in Windows
	os.system('cls' if os.name == 'nt' else "printf '\033c'") 

	#clear console in Pythonista 
	#console.clear() #this needs to be commented out if not tunning in Pythonista 
	
	global playerMoveDirection
	global playerCurrentX
	global playerCurrentY
	global gameScreen
	
	
	drawTopInfo()
	for ScreenX in gameScreen:
		print (''.join(map(str, ScreenX)))
	
	drawPlayerStats()
	
	directionInput = input("[G]enerate Dungeon\n[W]up [S]down [A]left [D]right\n[Q]uit\nyour input: ")
	playerMoveDirection = directionInput.upper()
	
	if (playerMoveDirection == "W"):
		if gameScreen[playerCurrentY-1][playerCurrentX] != "▓":
			gameScreen[playerCurrentY][playerCurrentX] = "•"
			playerCurrentY -= 1
		
	elif (playerMoveDirection == "S"):
		if gameScreen[playerCurrentY+1][playerCurrentX] != "▓":
			gameScreen[playerCurrentY][playerCurrentX] = "•"
			playerCurrentY += 1	
		
	elif (playerMoveDirection == "A"):
		if gameScreen[playerCurrentY][playerCurrentX-1] != "▓":
			gameScreen[playerCurrentY][playerCurrentX] = "•"
			playerCurrentX -= 1
	
	elif (playerMoveDirection == "D"):
		if gameScreen[playerCurrentY][playerCurrentX+1] != "▓":
			gameScreen[playerCurrentY][playerCurrentX] = "•"
			playerCurrentX += 1
		
	elif (playerMoveDirection == "G"):
		generateDungeon()
	
	#gameScreen = [["•" for i in range(screenX)] for j in range(screenY)] 
	gameScreen[playerCurrentY][playerCurrentX] = "@"
	

######################################
#MAIN GAME LOOP
#####################################

while True:
	Update()




