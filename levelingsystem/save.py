import json
import classes

'''
dmg none
hpo none
agi none
deffo none
deff none
dpeno none
dpen none
spp none
lvl none
htp none
Hlp none
'''

def save_game():
	with open('Player.json', 'w') as saved:
		saved.write(json.dumps({
		"dmg":classes.Player.dmg, 
		"hp":classes.Player.hp, 
		"htp":classes.Player.htp, 
		"hlp":classes.Player.hlp,
		"deff":classes.Player.deff,
		"nsrd":classes.Player.nsrd,
		"dpen":classes.Player.dpen,
		"dpeno":classes.Player.dpeno,
		"spp":classes.Player.spp,
		"spc":classes.Player.spc,
		"lvl":classes.Player.lvl,
		}))	


