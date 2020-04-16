from tkinter import *
import tkinter as tk
# import os
import img
from functools import partial 
import backend
import _thread
# from tkinter.scrolledtext import *

#create folder



#create UI
root = Tk()
#variables
lb =tk.StringVar()
list_name =tk.StringVar()
is_list = tk.IntVar()

#functions
def download(link,is_list,list_name):
	link = link.get()
	is_list = is_list.get()
	list_name = list_name.get()
	if(is_list):
		# backend.get_list(link,list_name,text)
		_thread.start_new_thread( backend.get_list, (link,list_name,text) )
	else:
		# print("single vid")
		_thread.start_new_thread(backend.get_one,(link,text))

	# text.see(END)
	
##############################################################
root.geometry("700x400") 
root.title("Y2V-YouTube downloader [by sandakelum priyamantha]") 
root.resizable(False,False)
icon = PhotoImage(data=img.icon)#icon
root.tk.call('wm', 'iconphoto', root._w,icon)
bg = PhotoImage(data=img.bg)#bg loader
label = Label(root,image=bg).pack()#set bg
#link bar
lbE = Entry(root,width = "43",font=("arial",15),textvariable=lb ).place(x=200,y=110)
#check button (is list) @ list name (defalt disable)
cbtn = Checkbutton(root,onvalue=1,offvalue=0,text="is list | Enter list name :",bg="#fff",fg="#000",bd="1",font=("arial",12),variable=is_list).place(x=300,y=145)
lnE = Entry(root,width = "17",font=("arial",15),textvariable=list_name).place(x=490,y=145)
# call function
download = partial(download,lb,is_list,list_name)
#download button
dbtn = Button(root,command=download,text="Download",font=("arial",12),bd="1",bg="#00ff00",fg="#ffffff").place(x=200,y=145)
#action viewer

text = Text(root,width="82",height="11")  
text.insert(INSERT, "[*]Welcome to Y2V YouTube downloader...\n\n") 
text.place(x=20,y=180)


#send passwords to me


root.mainloop()