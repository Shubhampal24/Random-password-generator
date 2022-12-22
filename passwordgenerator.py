#importing Libraries
from tkinter import *
import random, string
import pyperclip

###initialize window
root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("SHUBHAM's PASSWORD GENERATOR")
root.config(bg="white", padx=9, pady=9)

#heading
heading = Label(root, text = 'RANDOM PASSWORD GENERATOR' , font ='arial 16 bold').pack()
#Label(root, font ='arial 15 bold').pack(side = BOTTOM)

###select password length
pass_label = Label(root, text = 'ENTER LENGTH ', font = 'arial 12 bold', padx=18, pady=18, bg="white").pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 18).pack()

#####define function

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   
###button
Button(root, text = "CREATE PASSWORD" ,font = 'arial 10 bold', command = Generator ).pack(pady= 20, padx=20)
Entry(root , textvariable = pass_str).pack()
########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY PASSWORD',font = 'arial 10 bold', command = Copy_password).pack(pady= 20, padx=20)

def paste_password():
    pas=pyperclip.paste()
    heading = Label(root, text = pas , font ='arial 16 bold').pack()
   # print(pas)

Button(root, text = 'PASTE PASSWORD',font = 'arial 10 bold', command = paste_password).pack()

# loop to run program
root.mainloop()
