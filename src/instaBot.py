#!/usr/bin/env python3

import sys
import os
from tkinter import *
from tkinter import messagebox

class instaBot:
    def __init__(self, win):
        
        def run():
            check = 0
            if self.t1.get() != '':
                print(self.t1.get())
                print('account OK')
                check=check+1
            if self.t2.get() != '':
                print(self.t2.get())
                print('password OK')
                check=check+1
            if self.t3.get() != '':
                print(self.t3.get())
                print('keyword OK')
                check=check+1
            if self.t4.get() != '':
                print(self.t4.get())
                print('DM OK')
                check=check+1
            if check == 4:
                print("OK WE CAN CONTINUE")
            elif check != 4:
                messagebox.showinfo("Error", "One or several fields are not filled.")

        def overview():
            txt = self.t4.get()
            self.lbl6=Label(win, text=txt)
            self.lbl6.pack(pady=125)
        
        self.count=int()
        #Instagram account & password
        self.lbl1=Label(win, text='Account : @')
        self.lbl1.place(x=10, y=5)
        self.t1=Entry()
        self.t1.place(x=85, y=5)
        self.lbl2=Label(win, text='Password :')
        self.lbl2.place(x=10, y=35)
        self.t2=Entry(show="*")
        self.t2.place(x=85, y=35)

        #DM counter
        self.lbl3=Label(win, text='Nb account DMed :')
        self.lbl3.place(x=10, y=125)
        self.countDM=Label(win, text=str(self.count))
        self.countDM.place(x=135, y=125)

        #Key word research
        self.lbl4=Label(win, text='Key Word research :')
        self.lbl4.place(x=300, y=5)
        self.t3=Entry()
        self.t3.place(x=430,y=5)
        
        #DM message
        self.lbl5=Label(win, text='DM (past here):')
        self.lbl5.place(x=300, y=35)
        self.t4=Entry()
        self.t4.place(x=430, y=35)
        self.b1=Button(win, text='Overview', command=overview, bg="green")
        self.b1.place(x=600, y=35)

        #Run button
        self.runButton=Button(win, text='Run', command=run, bg="green")
        self.runButton.place(x=350, y=250)

def instaBotDM():
    """ Return nothing

    First function wich is the main function that call every module.
    """
    window=Tk()
    mywin=instaBot(window)
    window.title('Insta Bot DM')
    window.geometry("700x300")
    window.mainloop()