import os
import random
import pathlib
import colorama
from colorama import Fore, Back, Style
colorama.init()

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)
        self.files = []
        self.writefiles = []
        self.directories = []
        self.extra = []
        		
    def __exit__(self):
        os.chdir(self.savedPath)
        print(Fore.RED + "Current working directory : {0}".format(os.getcwd()) + '\033[39m')
        
    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
        print(Fore.RED + "Current working directory: {0}".format(os.getcwd()))
        print(Fore.GREEN + "element of the directory: ")
        os.system('ls')
        print('\033[39m')
        for file in os.listdir():
        	if os.path.isfile(file):
        		self.files.append(file)
        		if str(oct(os.stat(file).st_mode))[-1] in {7, 6, 3, 2}:
        			self.writefiles.append(file)
        	elif os.path.isdir(file):
        		self.directories.append(file)
        	else:
        		self.extra.append(file)
        		
        print(Fore.BLUE + "Files: " + str(self.files))
        print("writable files are : " + str(self.writefiles))
        print("directories: " + str(self.directories))
        print("extra: " + str(self.extra) + '\033[39m')
