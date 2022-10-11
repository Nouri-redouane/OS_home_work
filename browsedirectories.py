import os
import random
import colorama
from colorama import Fore, Back, Style #just to color the results in the terminal
colorama.init() 

Files_Table = [] #a table contaning all writable files
Text_Files_Table = [] #a table contaning all writable TEXT files
theroot = "none"#just to check if we have a root file in a directory

for (root,dirs,files) in os.walk('/home/kali/Desktop/', topdown=True): #goes through the directory speciefied in the 1st parametere (we'll change it to '/' after testing) 
	print(files) #print all the files found in that directory
	print ('--------------------------------')
	
	for file in files: #goes through all the files
		path = os.path.join(root, file) #this part is to save a root file if found (just for testing, will be removed later)
		if os.path.isfile(path) == True:
			if os.stat(path).st_uid == 0:
				theroot = os.stat(path).st_uid
			
		if os.path.isfile(path) == False or os.stat(path).st_uid == 0 : continue #if we find a root file or a file that can't be opened, we ignore it
		else:
			if str(oct(os.stat(path).st_mode))[-3:-2] in {'7', '6', '3', '2'}: #check if we have permission to write in a file
				Files_Table.append(path) #put all writable files in the list
				if(pathlib.Path(path).suffix == ".txt"):
					Text_Files_Table.append(path) #put all writable TEXT files in the list	
				


print(Fore.BLUE+ "these are to modifiable files: ")				
print(Files_Table)
print(Fore.CYAN+ "these are to TEXT modifiable files: ")				
print(Files_Table)
print(Fore.GREEN + "the root is " + theroot)


randomFile = Files_Table[random.randint(0,len(Files_Table)) - 1]
while randomFile == '/home/kali/Desktop/attacker.py':
	randomFile = Files_Table[random.randint(0,len(Files_Table)) - 1]
	
#selma's code with randomeFile
#for example: os.remove(randomFile)
