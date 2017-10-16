import random as c
import colors as c
from time import sleep as s
import animation as a
import classes as cl

'''
Dmg 
Hpo 
Agi 
Deffo 
Deff 
Dpeno 
Dpen 
Spp 
Lvl 
Htp 
'''
player = cl.Player
enemy = cl.Enemy

def attack():
	print(c.p + "You attack!")
	s(2)
	a.pattackanim()
	enemy.hp -= player.dmg
	if enemy.dpen > 0:
		enemy.deff *= enemy.hp
		enemy.dpen -= 1

def dodge():
	print(c.p + "You dodge your enemy's attack!")
	s(2)
	a.pdodgeanim()

def special():
	print(c.p + "You use your special ability!")
	s(2)
	a.pspecialanim()
	enemy.hp -= player.spc
	player.spp -= 1
	if enemy.dpen > 0:
		enemy.deff *= enemy.hp
		enemy.dpen -= 1


