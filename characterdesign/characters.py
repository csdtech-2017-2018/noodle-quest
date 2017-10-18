import colors as c
author="Matu and Patlu"

class Thing():
	dmg=None
	hpo=None
	hp=None
	agi=None
	deff=None
	dpeno=None
	dpen=None
	spp=None
	lvl=None
	hpp=None
	htp=None	
	
class Player(Thing):
	noodles=0
	name=None

class Foe(Thing):
	mname="Test mob name"


class Luke_potential_energy_user(Player):
	dmg=35
	hpo=100
	agl=25
	deff=15
	dpeno=4
	dpen=2
	spp=1
	lvl=1
	hpp=2
	hlp=40
class The_Goonslayer(Player):
	dmg=25
	hpo=70
	
