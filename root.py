from tkinter import *
from PIL import ImageTk, Image
import subprocess
import signal

#global variables
root_user = False
window = incorrect_password_lbl = password_entry = None
passwrd = None

#call this function if returned true then root privilege gained
#else : the root privilege failed
def get_root():
    open_window()
    return root_user


def keep_alive(signum, frame):
    global passwrd
    echo_command = subprocess.Popen(['echo',passwrd], stdout=subprocess.PIPE)
    subprocess.Popen(['sudo', '-S', 'whoami'], stdin=echo_command.stdout, stdout=subprocess.PIPE)
    signal.signal(signal.SIGALRM, keep_alive)
    signal.alarm(600)

#this function deletese incorrect password message
def delete_incorrect_password_lbl(signum, frame):
    global incorrect_password_lbl
    incorrect_password_lbl.place_forget()

#this function checks if the given password is true or no
def password_checking(password):
    global passwrd
    echo_command = subprocess.Popen(['echo',password], stdout=subprocess.PIPE)
    root_command = subprocess.Popen(['sudo', '-S', 'whoami'], stdin=echo_command.stdout, stdout=subprocess.PIPE)
    
    
    if root_command.stdout.read()==b'root\n':
        passwrd = password
        signal.signal(signal.SIGALRM, keep_alive)
        signal.alarm(600)
        return True
    else:
        return False

#this function is called when the "OK" button clicked
def ok_click_handler():
    global password_entry, incorrect_password_lbl, root_user, window
    #getting the password from input field
    password=password_entry.get()
    #check if root password is true
    if password_checking(password)==True:
        root_user = True
        window.destroy()
    else:
        incorrect_password_lbl.place(x=100, y=200)
        password_entry.delete(0, END)
        signal.signal(signal.SIGALRM, delete_incorrect_password_lbl)
        signal.alarm(3)

#this function is called when the "Cancel" button clicked
def cancel_click_handler():
    #closing the window
    global window
    window.destroy()


def open_window():
    global window, password_entry, incorrect_password_lbl, root_user

    #creating new window
    window = Tk()

    #window title
    window.title("Authenticate")
    window.configure(width=600, height=250)

    #_____ cooming soon in the next window version inchaallah _____
    

    # window_width = 600
    # window_height = 250

    # window.configure(width=window_width, height=window_height)

    # screen_width = window.winfo_screenwidth()
    # screen_heigh = window.winfo_screenheight()

    # window_placement_x = (screen_width/2) - (window_width/2)
    # window_placement_y = (screen_heigh/2) - (window_height/2)

    # window.geometry("%dx%d+%d+%d"%(window_width, window_height, window_placement_x, window_placement_y))


    #______                                                   _______


    #----- initialisation -----

    #image
    key_img=ImageTk.PhotoImage(Image.open("images/key.png"))
    #labels
    admin_tasks_lbl=Label(window)
    description_lbl=Label(window)
    password_lbl=Label(window)
    incorrect_password_lbl=Label(window)
    key_image_lbl=Label(window, image=key_img)
    #inputs
    password_entry=Entry(window, show='.')
    #buttons
    ok_button=Button(window)
    cancel_button=Button(window)

    #----- configuration -----

    #labels
    admin_tasks_lbl.configure(text="Enter your password to perform \nadministrative tasks", font=('Helvetica', 20, 'bold'), foreground="#444643", justify="left")
    description_lbl.configure(text="Authentication required", font=('Helvetica', 14, 'normal'), foreground="#444643")
    password_lbl.configure(text="Password: ", font=('Helvetica', 15, 'normal'), foreground="#444643")
    incorrect_password_lbl.configure(text="Sorry, try again.", font=('Helvetica', 15, 'normal'), foreground="red")
    #input
    password_entry.configure(font=('Helvetica', 20, 'bold'), highlightcolor="#f4906c")
    #buttons
    ok_button.configure(text="OK", font=('Helvetica', 14, 'normal'), activebackground="#f4906c", command=ok_click_handler)
    cancel_button.configure(text="Cancel", font=('Helvetica', 14, 'normal'), activebackground="#f4906c", command=cancel_click_handler)


    #----- placements -----

    #labels
    key_image_lbl.place(x=5, y=5)
    admin_tasks_lbl.place(x=100, y=20)
    description_lbl.place(x=100, y=100)
    password_lbl.place(x=100, y=150)
    #input
    password_entry.place(x=200, y=145, width=320, height=30)
    #buttons
    ok_button.place(x=490, y=200, width=100)
    cancel_button.place(x=380, y=200, width=100)

    #window icon
    icon = PhotoImage(file="images/key_64.png")
    window.iconphoto(False, icon)


    window.mainloop()
