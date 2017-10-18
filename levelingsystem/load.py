import classes
import json

def load_game():
	with open('player.json', 'r') as pfile:
		j = json.load(pfile)
		classes.Player.dmg=j['dmg']
		classes.Player.hp=j['hp']
		classes.Player.agi=j['agi']
		classes.Player.deff=j['deff']
		classes.Player.dpen=j['dpen']
		classes.Player.dpeno=j['dpeno']
		classes.Player.spc=j['spc']
		classes.Player.spp=j['spp']
		classes.Player.lvl=j['lvl']
		classes.Player.hlp=j['hlp']
		classes.Player.nsrd=j['nsrd']

