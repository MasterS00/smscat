import os
import time
import random
import colorama
import requests
import subprocess
from colorama import Fore
class Banners:
	ban_a = "figlet smscat"
	creator = "MS00"
	github = "https://github.com/MasterS00/"

class Colors:
	red = Fore.RED
	blue = Fore.BLUE
	yellow = Fore.YELLOW

os.system("clear")
col = random.choice([Colors.red, Colors.blue, Colors.yellow])
print(col+"")
os.system(Banners.ban_a)
print(Fore.GREEN+"Creator: "+Fore.RED+Banners.creator)
print(Fore.RED+"github: "+Fore.YELLOW+Banners.github)
phoner = input(Colors.red+"+phone: "+Fore.WHITE)
mess = input(Colors.red+"message: "+Fore.WHITE)

resp = requests.post('https://textbelt.com/text', {
  'phone': f'{phoner}',
  'message': f'{mess}',
  'key': 'textbelt',
})
print(resp.json())
print(Colors.yellow+"Finish")
time.sleep(1)