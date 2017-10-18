import colors as c
from time import sleep as s
import random as r
import classes as cl
import emoves
import pmoves

Enemy = cl.Enemy
Enemy = cl.Enemy


def playerchoice():
	playerchoose = input(c.y + "Do you want to attack, heal, or use your special ability?   Attack-(1)   Heal-(2)   Special Ability-(3)\n>>> " + c.o)
	if playerchoose == '1':
		if Enemy.agi > 0 and Enemy.agi <= 9:
			dodge = r.randint(1, 30)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 10 and Enemy.agi <= 19:
			dodge = r.randint(1, 25)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 20 and Enemy.agi <= 29:
			dodge = r.randint(1, 20)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 30 and Enemy.agi <= 39:
			dodge = r.randint(1, 15)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 40 and Enemy.agi <= 49:
			dodge = r.randint(1, 10)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 50 and Enemy.agi <= 59:
			dodge = r.randint(1, 8)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 60 and Enemy.agi <= 69:
			dodge = r.randint(1, 6)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 70 and Enemy.agi <= 79:
			dodge = r.randint(1, 4)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 80 and Enemy.agi <= 89:
			dodge = r.randint(1, 3)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 90 and Enemy.agi <= 199:
			dodge = r.randint(1, 2)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.attack()
		elif Enemy.agi >= 200:
			emoves.dodge()
		else:
			pmoves.attack()


	elif playerchoose == '2':
		if Player.htp >= 1:
			pmoves.heal()
		else:
			playerchosen()

	elif playerchoose == '3':
		if Player.spp >= 1:
			if Enemy.agi > 0 and Enemy.agi <= 9:
				dodge = r.randint(1, 30)
				if dodge == 1:
					emoves.dodge()
				else:
					pmoves.special()
		elif Enemy.agi >= 10 and Enemy.agi <= 19:
			dodge = r.randint(1, 25)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 20 and Enemy.agi <= 29:
			dodge = r.randint(1, 20)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 30 and Enemy.agi <= 39:
			dodge = r.randint(1, 15)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 40 and Enemy.agi <= 49:
			dodge = r.randint(1, 10)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 50 and Enemy.agi <= 59:
			dodge = r.randint(1, 8)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 60 and Enemy.agi <= 69:
			dodge = r.randint(1, 6)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 70 and Enemy.agi <= 79:
			dodge = r.randint(1, 4)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 80 and Enemy.agi <= 89:
			dodge = r.randint(1, 3)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 90 and Enemy.agi <= 499:
			dodge = r.randint(1, 2)
			if dodge == 1:
				emoves.dodge()
			else:
				pmoves.special()
		elif Enemy.agi >= 500:
			emoves.dodge()
		else:
			playerchosen()
	else:
		playerchosen()




if __name__ == '__main__':
	try:
		playerchoose()
	except KeyboardInterrupt:
		exit
