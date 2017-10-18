import random as r
import classes as cl
import playerchoose as pc
import ai
import scanner as s
import death as d
import win as w

player = cl.Player
enemy = cl.Enemy

def battleloop():
	if player.hp > 0 and enemy.hp > 0:
		if player.agi > enemy.agi:
			pfirst()
		elif player.agi < enemy.agi:
			efirst()
		elif player.agi == enemy.agi:
			randord = r.randint(1, 2)
			if randord == 1:
				pfirst()
			elif randord == 2:
				efirst()
		else:
			battleloop()
	elif player.hp <=  0:
		d.death()
	elif enemy.hp <= 0:
		w.win()
	battleloop()


def pfirst():
	s.scanner()
	pc.playerchoice()	
	ai.ai()
	
def efirst():
	s.scanner()
	ai.ai()
	pc.playerchoice()

if __name__ =='__main__':
	battleloop()
