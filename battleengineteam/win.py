import colors as c
import time as t
import classes as cl
import random as r

pos1 =  '''
	   _o
	  __|-
	     >
	'''

pos2 =  '''
		    o/
		    |__
		    |
	'''

pos3 = '''
			 \o_
		       __/
			 >
	'''

pos4 =  '''

			    \__/o
			    /  \ 
	'''

pos5 =  '''
				    \ /
				     |
				    /o\ 
	'''

pos6 =  '''
					      __
					     /
					   o|
	'''

pos7 =  '''
						    __o
						      |
						     <<
	'''

pos8 =  '''
							  |o
							  /
							 |
	'''

pos9 =  '''
							       \__/o
	'''

pos10 = '''
								       <<
									|
									o\  
	'''

pos11 = '''
									      o___
									      /   \  
	'''

pos12 = '''
										       _o
											|
										       <<
	'''

pos13 = '''
											     o/
											     |
											    < \ 
	'''

def animation():
	o.system("clear")
	print(pos1)
	t.sleep(.2)
	o.system("clear")
	print(pos2)
	t.sleep(.2)
	o.system("clear")
	print(pos3)
	t.sleep(.2)
	o.system("clear")
	print(pos4)
	t.sleep(.2)
	o.system("clear")
	print(pos5)
	t.sleep(.2)
	o.system("clear")
	print(pos6)
	t.sleep(.2)
	o.system("clear")
	print(pos7)
	t.sleep(.2)
	o.system("clear")
	print(pos8)
	t.sleep(.2)
	o.system("clear")
	print(pos9)
	t.sleep(.2)
	o.system("clear")
	print(pos10)
	t.sleep(.2)
	o.system("clear")
	print(pos11)
	t.sleep(.2)
	o.system("clear")
	print(pos12)
	t.sleep(.2)
	o.system("clear")
	print(pos13)

def win():
	print(c.r + "You won!")
	t.sleep(3)
	animation()
	lvladd = r.randint(1, 10)
	cl.Player.lvl += lvladd
	print(c.y + "You got " + str(lvladd) + " experience points!")
	s(2)

