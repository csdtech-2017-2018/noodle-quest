import colors as c
import classes as cl
from time import sleep as s
import os as o

deathscreen = '''
                				            (
               					 .            )        )
                				         (  (|              .
                				     )   )\/ ( ( (
				             *  (   ((  /     ))\))  (  )    )
				           (     \   )\(          |  ))( )  (|
				           >)     ))/   |          )/  \((  ) \   
				           (     (      .        -.     V )/   )(    (
				            \   /     .   \            .       \))   ))
				              )(      (  | |   )            .    (  /
				             )(    ,'))     \ /          \( `.    )
				             (\>  ,'/__      ))            __`.  /
				            ( \   | /  ___   ( \/     ___   \ | ( (
				             \.)  |/  /   \__      __/   \   \|  ))
				            .  \. |>  \      | __ |      /   <|  /
				                 )/    \____/ :..: \____/     \ <
				          )   \ (|__  .      / ;: \          __| )  (
				         ((    )\)  ~--_     --  --      _--~    /  ))
				          \    (    |  ||               ||  |   (  /
				                \.  |  ||_             _||  |  /
				                  > :  |  ~V+-I_I_I-+V~  |  : (.
				                 (  \:  T\   _     _   /T  : ./
        				           \  :    T^T T-+-T T^T    ;<
        				           \..`_       -+-       _'  )
				         )            . `--=.._____..=--'. ./         (
		
					__   __  ___   _   _   ____   ___  _____  ____  
					\ \ / / / _ \ | | | | |  _ \ |_ _|| ____||  _ \ 
					 \ V / | | | || | | | | | | | | | |  _|  | | | |
					  | |  | |_| || |_| | | |_| | | | | |___ | |_| |
					  |_|   \___/  \___/  |____/ |___||_____||____/ 
	'''

def death():
	print(c.clear)
	print(c.r + deathscreen)
	s(5)
	continueq()

def continueq():
	continueorquit = input(c.y + "Do you want to continue or exit?   Continue (1)    Exit (2)\n >>> " + c.b)
	if continueorquit == '1':
		g.game()
		cl.Player = cl.Main
	elif continueorquit== '2':
		exit
		o.system('exit')
