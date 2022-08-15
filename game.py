import random
import os
import sys
from playsound import playsound
import threading
import colorama
from colorama import Back,Fore

colorama.init()
print(Back.YELLOW)
print(Fore.RED)
print(colorama.ansi.clear_screen())


playsound2 = True

if len(sys.argv) >= 2:
    if  "/reset" in sys.argv[0] or "/reset" in  sys.argv[1]:
        if input("Are you sure you want to reset the score?") == "yes":
            os.remove("highscore.txt")
            print("Game high score reset completed...")
            exit(0)
    if  "/nosound" in sys.argv[1] or "/nosound" in  sys.argv[2]:
        playsound2 = False


def playsoundbackr():
    if playsound2 == True:
         while True:
            playsound("background.mp3")

thread = threading.Thread(target=playsoundbackr)

thread.start()

def play():

	print("")

	print("================================================")
	print("Welcome to guessing mania....!!!")
	try:
		print("Your Best:"+open("highscore.txt","r").read()+" Attempts...") 
	except:
		print("Welcome for the first time!!!")   	
	print("================================================")
	lt = 999
	print(Fore.GREEN)
	print("""
1)Very Easy \n"""+Fore.CYAN+"""
2)Easy \n"""+Fore.BLACK+"""
3)Medium \n"""+Fore.LIGHTMAGENTA_EX+"""
4)Hard \n"""+Fore.LIGHTRED_EX+"""
5)Very Hard"""+Fore.RED+"""
	""")
	level = int(input("Select a level(Enter the level no. shown above):"))
	playsound("click.wav")
	if level == 1:
		lt = 10
	elif level == 2:
		lt = 100
	elif level == 3:lt = 500
	elif level == 4:
		lt == 999
	elif level == 5:lt = 1500
	#print(n)

	n = random.randint(0,lt)
	print(Fore.BLUE)
	guessed = 0
	attepmts = 0

	while guessed != n:
		a = input("Guess the no:")
		playsound("click.wav")
		guessed = int(a)
		if guessed > n:print("Your guess is more than the real no.")
		elif guessed < n:
			print("Your guess is less than the real no.")
		elif guessed > (lt+1):print("Your guess is more than no. limit the limit is "+str(lt+1))
		print("")
		attepmts += 1

	print("")
	print(Back.WHITE)
	print(Fore.BLACK)
	print("Yayy you got it!!")
	print("It took {} attempts to finish the game.".format(attepmts))
	playsound("success.mp3")

	if os.path.exists("highscore.txt"): 
		hs = int(open("highscore.txt","r").read())
		if attepmts <= hs:
			print("Your new high score: {}".format(attepmts))
			open("highscore.txt","w").write(str(attepmts))
	
	else:
		open("highscore.txt","w").write(str(attepmts))
	


	if input("Play another time?") == "yes":
		colorama.init()
		print(Back.YELLOW)
		print(Fore.RED)
		print(colorama.ansi.clear_screen())
		play()
	else:
		print("Bye Byye!!!")




play()