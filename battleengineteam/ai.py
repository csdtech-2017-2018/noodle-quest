import random as r
from time import sleep as s
import classes
import pmoves
import emoves
import colors as c

'''
Dmg Damage
Hp Health
Agi Agility
Deff Defence
Dpen Armor "Health"
Htp Healing amount
Spc Special
Spp Amount of times you can use your special
Lvl Level
Htp Amount of times you can heal
'''

Student = cl.Student
Enemy = cl.Enemy

enemychoose = r.randint(1, 3)

def ai():
	if enemychoose == 1:
		if Student.agi > 0 and Student.agi <= 9:
			dodge = r.randint(1, 30)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 10 and Student.agi <= 19:
			dodge = r.randint(1, 25)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 20 and Student.agi <= 29:
			dodge = r.randint(1, 20)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 30 and Student.agi <= 39:
			dodge = r.randint(1, 15)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 40 and Student.agi <= 49:
			dodge = r.randint(1, 10)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 50 and Student.agi <= 59:	
			dodge = r.randint(1, 8)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 60 and Student.agi <= 69:
			dodge = r.randint(1, 6)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 70 and Student.agi <= 79:
			dodge = r.randint(1, 4)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 80 and Student.agi <= 89:
			dodge = r.randint(1, 3)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 90 and Student.agi <= 199:
			dodge = r.randint(1, 2)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.attack()
		elif Student.agi >= 200:
			pmoves.dodge()
		else:
			emoves.attack()


	elif enemychoose == 2:
		if Enemy.htp >= 1:
			emoves.heal()
		else:
			ai()
	elif enemychoose == 3:
		if Enemy.spp >= 1:
			if Student.agi > 0 and Student.agi <= 9:
			dodge = r.randint(1, 30)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 10 and Student.agi <= 19:
			dodge = r.randint(1, 25)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 20 and Student.agi <= 29:
			dodge = r.randint(1, 20)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 30 and Student.agi <= 39:
			dodge = r.randint(1, 15)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 40 and Student.agi <= 49:
			dodge = r.randint(1, 10)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 50 and Student.agi <= 59:
			dodge = r.randint(1, 8)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 60 and Student.agi <= 69:
			dodge = r.randint(1, 6)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 70 and Student.agi <= 79:
			dodge = r.randint(1, 4)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 80 and Student.agi <= 89:
			dodge = r.randint(1, 3)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 90 and Student.agi <= 499:
			dodge = r.randint(1, 2)
			if dodge == 1:
				pmoves.dodge()
			else:
				emoves.special()
		elif Student.agi >= 500:
			pmoves.dodge()
		else:
			ai()

	elif enemychoose == 3:
		emovesheal()

	else:
		ai()
