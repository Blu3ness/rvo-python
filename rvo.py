import time
import random

charName = 'Ryan'
charHP_Max = 15
charHP_Current = 15	

charDodge = 9
charBlock = .9
charIsAlive = True

npcName = 'Orc'
npcHP_Max = 15
npcHP_Current = 15

npcDodge = 7
npcBlock = .9
npcIsAlive = True

def randomATK():
	temp = random.randrange(2,9)
	return temp
	
def powerATK():

	temp = random.randrange(10,18)
	return temp

def dodgeCheck():
	temp = random.randrange(1,100)
	print "%%%%%%%%%%%%%%%DODGE CHECK ", temp
	return temp
def combat():

	charCombatHP = charHP_Max
	npcCombatHP = npcHP_Max

	charPower = 0
	npcPower = 0
	charATK = randomATK()
	npcATK = randomATK()

	
	print "Player ATK: ", charATK
	print "NPC ATK: ", npcATK
	#time.sleep(1)
	
	charWin = 0
	npcWin = 0
	
	while charCombatHP and npcCombatHP > 0:
		
		print "Player Attacks NPC"
		charPower = charPower + .02
		#time.sleep(.5)
		print ">>>>>>>>>>>>>>>>>>>>>>>>>>>CHAR POWER: ", charPower
		#if 
		if charPower >= 10:
			charPower = charPower - 10
			charPowerATK = powerATK()
			npcCombatHP = npcCombatHP - (charPowerATK * npcBlock)			
			print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", npcCombatHP
			
		if npcPower < 10:	
			npcCombatHP = npcCombatHP - (charATK * npcBlock)
			print "@@@@@@@@@@@@@@@@@@@@"
		#time.sleep(.02)
		print npcCombatHP
		if npcCombatHP <= 0:
			print "Orc dead as fuck ", npcCombatHP
			npcCombatHP = npcHP_Max
			charWin = (charWin + 1)
			print "Ryan Win: ", charWin
		print "NPC Attacks Player"
		charPower = charPower + 1
		charCombatHP = charCombatHP - (npcATK * charBlock)
		
		#time.sleep(.02)
		print charCombatHP
		if charCombatHP <= 0:
			print "Ryan dead as fuck ", charCombatHP
			charCombatHP = charHP_Max
			npcWin = (npcWin + 1)
			print "Orc Win: ", npcWin
			
		charATK = randomATK()
		print "New Attack: ", charATK
		#time.sleep(.01)
		npcATK = randomATK()
		print "New Attach: ", npcATK
		#time.sleep(.01)

combat()


