# Import socket module
import socket    

import random
import os
import sys
from playsound import playsound
import threading        
import colorama
from colorama import Back,Fore
import pyperclip

def play(c,ato):

	print("")

	print("================================================")
	print("Welcome to guessing mania....!!!")
	try:
		print("Your Best:"+open("highscore.txt","r").read()+" Attempts...") 
	except:
		print("Welcome for the first time!!!")   	
	print("================================================")
	lt = 1500
	

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
	if attepmts < ato:
		print("You won the game!!!!")
		print("Oppentent attempts:"+str(ato))
	elif attepmts == int(ato):
			print("[+] Match Tied...")
	else:
		print("You lost the game!!!")
		print("Oppentent attempts:"+str(ato))
	print("")
	print(Back.WHITE)
	print(Fore.BLACK)
	c.send(str(attepmts).encode())
	playsound("success.mp3")
	


	

def load_play():
	# Create a socket object
	s = socket.socket()
	sn = pyperclip.paste()
	url = ""
	if str(sn).startswith("https://") or str(sn).startswith("http://"):
		url = str(sn)
	else:
		url = input("Enter a URL to connect:")
	# Define the port on which you want to connect
	att2 = 0
	host = url.replace("http://","").replace("https://","").split(":")[0]
	port = url.replace("http://","").replace("https://","").split(":")[1]              

	# connect to the server on local computer
	s.connect((host, int(port)))
 
	# receive data from the server and decoding to get the string.
	closed = False
	print("[+] Waiting for opponent to complete the game...")
	while closed == False:
		r = s.recv(1024).decode()
		if r != "":
			try:
				play(s,int(r))
				input("[+]Press Enter to exit...")
				break
			except:
				pass
	
# close the connection
	s.close()    