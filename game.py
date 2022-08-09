import random
import os
import sys
from playsound import playsound
import threading

def playsoundbackr():
    while True:
        playsound("background.mp3")

thread = threading.Thread(target=playsoundbackr)

thread.start()


lt = 999

try:
    if  "/reset" in sys.argv[0] or "/reset" in  sys.argv[1]:
        if input("Are you sure you want to reset the score?") == "yes":
            os.remove("highscore.txt")
            print("Game high score reset completed...")
            exit(0)
except:
    pass

print("================================================")
print("Welcome to guessing mania....!!!")
try:
    print("Your Best:"+open("highscore.txt","r").read()+" Attempts...")    
except:
    print("Welcome for first time.....")
print("================================================")
print("")

print("""
1)Very Easy \n
2)Easy \n
3)Medium \n
4)Hard \n
5)Very Hard
""")
level = int(input("Select a level(Enter th level no. shown above):"))
playsound("click.wav")
if level == 1:
    lt = 10
elif level == 2:
    lt = 100
elif level == 3:
    lt = 500
elif level == 4:
    lt == 999
elif level == 5:
    lt = 1500
#print(n)

n = random.randint(0,lt)

gussed = 0
attepmts = 0
while gussed != n:
    a = input("Guess the no:")
    playsound("click.wav")
    gussed = int(a)
    if gussed > n:
        print("Your guess is more than the real no.")
    elif gussed < n:
        print("Your guess is less than the real no.")
    elif gussed > (lt+1):
        print("Your guess is more than no. limit the limit is "+str(lt+1))

    print("")
    attepmts += 1

print("")
print("Yayy you got it!!")
print("It took {} attempts to finish the game.".format(attepmts))
playsound("success.mp3")

if os.path.exists("highscore.txt"):
    hs = int(open("highscore.txt","r").read())
    if attepmts <= hs:
        open("highscore.txt","w").write(str(attepmts))
        print("Your new high score: {}".format(attepmts))
else:
     open("highscore.txt","w").write(str(attepmts))
     print("Your new high score: {}".format(attepmts))
input()
exit()
