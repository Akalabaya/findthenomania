import socket
import time
import random
from pyngrok import ngrok
import sys
try:
	from game_client_module import load_play
except:
	from socketmodes.game_client_module import load_play
import os
import sys
from playsound import playsound
import threading
import colorama
from colorama import Back,Fore

def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP



def play(c):

	print("")

	print("================================================")
	print("Welcome to guessing mania....!!!")
	try:
		print("Your Best:"+open("highscore.txt","r").read()+" Attempts...") 
	except:
		print("Welcome for the first time!!!")   	
	print("================================================")
	lt = 1500
	
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
	c.send(str(attepmts).encode())
	playsound("success.mp3")
	print("[+]Now waiting for opponent to complete the game...")
	while True:
		r = c.recv(1024).decode()
		if r != "": 
			if attepmts < int(r):
				print("[+] You won...")
				print("Oppentent attempts:"+str(r))
				break
			else:
				print("[+] You lost...")
				print("Oppentent attempts:"+str(r))
				break
	




def playcreate(port):
    # next create a socket object
    s = socket.socket()        
    #print ("Socket successfully created")
	
    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))        
    print ("Url of game:http://"+get_ip()+":%s" %(port))
    print("Send your friend the above url of game..")
    # put the socket into listening mode
    s.listen(5)    
	     
 
    # a forever loop until we interrupt it or
    #    an error occurs
    while True:
 
    # Establish connection with client.
      c, addr = s.accept()    
      #print ('Got connection from', addr )
      
      c.send('[+]Connection successfully established...'.encode())
      sc = play(c)
      # Close the connection with the client
      c.close()
    
      # Breaking once connection closed
      break


print("")

print("================================================")
print("Welcome to guessing mania....!!!")
try:
	print("Your Best:"+open("../highscore.txt","r").read()+" Attempts...") 
except:
	print("Welcome for the first time!!!")   	
print("================================================")
lt = 2000

print("""
1.Create A Game 
2.Enter A Game
 """)

choice = input("Enter your choice: ")
if int(choice) == 1:
	port = random.randint(1000,5000)
	try:
		print("[+] Connecting to ngrokForward")
		ngrok.set_auth_token(sys.argv[1])
		ssh_tunnel = ngrok.connect(port, "tcp")
		print("Public Url:"+ssh_tunnel.public_url.replace("tcp://","https://"))
	except:
		pass
	playcreate(port)
	input("[+]Press Enter to exit...")
else:
	load_play()






 
