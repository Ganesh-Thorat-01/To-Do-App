'''
env python3
Created on Wed Nov 04 2020
@author: Ganesh Thorat
-*-coding: utf-8 -*-
'''

import tkinter as tk
from tkinter import messagebox

def main():

    tolab = tk.Label(window, text="Boss,You Have To Complete Given Task.....",font=('aerial bold',11),bg='yellow')
    tolab.grid(row=0, sticky=('n', 'e'))

    global labframe
    labframe = tk.Frame(window,bg="light yellow")
    labframe.grid(row=1)

    global butframe
    butframe = tk.Frame(window,bg="light yellow")
    butframe.grid(row=len(todolist)+3)

    global length
    length = len(todolist)

    global addbut
    addbut = tk.Button(butframe, text='Add', relief='solid',bg="light blue",
                       command=lambda: Add())
    addbut.grid(row=1, ipadx=13, pady=7)

    global delbutton
    delbutton = tk.Button(butframe, text='Delete',bg="light blue",
                          relief='solid', command=lambda: Delete())
    delbutton.grid(row=2, ipadx=13, pady=7)

    window.mainloop()


def Add():
    global e
    e = tk.Entry(labframe,borderwidth=2)
    e.grid(row=len(todolist), ipadx=5, pady=5, column=1)

    global subbut
    subbut = tk.Button(labframe, text='Submit',bg="light blue",
                       relief='solid', command=lambda: addsubmit())
    subbut.grid(row=len(todolist), ipadx=5, pady=5, column=3)


def addsubmit():
    string = e.get()

    if len(string.strip()) > 0:
        todolist.append(string)
        display()
    e.destroy()
    subbut.destroy()


def Delete():

    global e1
    global dellabel
    global subbut1
    dellabel = tk.Label(labframe, text="Enter serial number",bg='light yellow')
    dellabel.grid(row=len(todolist), ipadx=2, pady=5, column=0)
    e1 = tk.Entry(labframe)
    e1.grid(row=len(todolist), ipadx=7, pady=5, column=1)
    subbut1 = tk.Button(labframe, text='Submit',bg="light blue",
                        relief='solid', command=lambda: delsubmit())
    subbut1.grid(row=len(todolist)+1, ipadx=3, pady=5, column=0, columnspan=2)


def delsubmit():
    num = e1.get()

    if num.isdigit and int(num) <= len(todolist):
        num = int(num)
        del todolist[num-1]
        e1.destroy()
        dellabel.destroy()
        subbut1.destroy()
        butframe.grid(row=len(todolist)+1)

        
        for widget in labframe.winfo_children():
            widget.destroy()
        labframe.pack_forget()
        display()

    else:
        tk.messagebox.showerror("Error", 'Invalid Serial Number')

def display():
    global lab
    labframe.pack_forget()
    for i in range(len(todolist)):
        lab=tk.Label(labframe,text="["+ str(i+1)+"] "+todolist[i],font=('aerial bold',12),bg='light yellow')
        lab.grid(row=len(todolist)+3,padx=4)
    
if __name__ == '__main__':
    global todolist
    todolist = []
    global window
    window = tk.Tk()
    window.title("To Do App")
    window.configure(bg='light yellow')
    window.geometry('300x350')
    main()
