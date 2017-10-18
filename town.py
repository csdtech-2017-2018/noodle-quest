#Author: Abhi and Ahad


def hub():
	print("Welcome to Noodle Town!")
	hubquestions = input("Where would you like to go. The shop, battle arena, save area, or to the noodle microwave? (1) (2) (3) (4) ")
 if hubquestions=="1":
	print("All right. Let's go!")
	shop()
elif hubquestions=="2":
	print("Hope you don't die.")
	battle arena()
elif hubquestions=="3":
	print("Oke Doike.")
	save area()
elif hubquestion=="4":
	print("Wow! You are brave to go the mistical noodle microwave.")
	noodle microwave()
else:
	print("I do not understand.")
	sleep(1)
	hub()


