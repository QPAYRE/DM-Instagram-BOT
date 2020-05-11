#!/usr/bin/env python3

import sys
import os
import time
import string
import traceback

from random import randint
from tkinter import *
from tkinter import messagebox
from selenium import webdriver

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

bgColor ='#a17957'

class instaBot:
    def __init__(self, win):
        def sendDm(contactList, dm, nbdm):
            """ Return nothing
                loop that dm to every @
            """
            dmed = 1
            for contact in contactList:
                time.sleep(randint(1,10))
                try:
                    time.sleep(1)
                    self.driver.get("https://www.instagram.com/direct/inbox/")
                    try:
                        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
                    except:
                        pass
                    self.driver.find_element_by_xpath('//button[@type="button"]').click()
                    time.sleep(2)
                    self.instaSendAccount = self.driver.find_element_by_name("queryBox")
                    time.sleep(2)
                    self.instaSendAccount.send_keys(contact)
                    time.sleep(2)
                    list1 = self.driver.find_elements_by_css_selector('div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl')
                    self.driver.execute_script("arguments[0].click();", list1[0])
                    time.sleep(2)
                    self.driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF.cB_4K').click()
                    time.sleep(2)
                    self.textArea = self.driver.find_element_by_css_selector('textarea')
                    time.sleep(2)
                    self.textArea.send_keys(dm)
                    time.sleep(2)
                    self.driver.find_element_by_css_selector('div.Igw0E.IwRSH.eGOV_._4EzTm.JI_ht > button:nth-child(1)').click()
                    if dmed == nbdm:
                        self.done=Label(win, text='DMs DONE !', bg='#3E4149')
                        self.done.place(x=330, y=200)
                        break
                    dmed = dmed+1
                except:
                    pass

        def backend(account, password, keyword, dm, nbdm):
            """ Return nothing
                It get @ from account in terms of #
                Send @, nb of dm to send, and the dm to sendDm()
            """
            #Print info in console
            print("Insta Account: "+account)
            print('#'+keyword)
            print("----------")
            self.driver = webdriver.Firefox(executable_path='./geckodriver')
            self.driver.get("https://instagram.com/")
            # Try to login to instagram
            try:
                self.instaAccount = self.driver.find_element_by_name("username")
                self.instaPassword = self.driver.find_element_by_name("password")
                self.instaAccount.send_keys(account)
                self.instaPassword.send_keys(password)
                time.sleep(1)
                self.driver.find_element_by_xpath('//button[@type="submit"]').click()
            except:
                pass
            # Try to skip notification popup (fr only)
            try:
                ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
            except:
                pass
            # Try to search keyword
            try:
                self.driver.get("https://www.instagram.com/explore/tags/"+keyword)
            except:
                pass
            # loop
            for i in range(1,3):
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)
            #searshing for picture link
            hrefs = self.driver.find_elements_by_tag_name('a')
            images_links = []
            for item in hrefs:
                href = item.get_attribute('href')
                if "/p/" not in href:
                    continue
                images_links.append(href)
            # Get @
            contactList = list()
            for images_link in images_links:
                self.driver.get(images_link)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                try:
                    contact = self.driver.find_element_by_css_selector('a.sqdOP.yWX7d._8A5w5.ZIAjV ')
                    contactList.append(contact.text)
                    self.count = self.count + 1
                except:
                    pass
            contactList = list(set(contactList))
            self.countDM=Label(win, text=str(self.count))
            # Send DM
            sendDm(contactList, dm, int(nbdm))

        def run():
            """ Return nothing
                Check if every fields are filled and call run function.
            """
            check = 0
            if self.t1.get() != '':
                check=check+1
            if self.t2.get() != '':
                check=check+1
            if self.t3.get() != '':
                check=check+1
            if self.t4.get() != '':
                check=check+1
            if self.nb.get() != '':
                check=check+1
            if check == 5:
                backend(self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get(), self.nb.get())
            elif check != 5:
                messagebox.showinfo("Error", "One or several fields are not filled.")
        
        self.count=int()
        #Instagram account & password
        self.lbl1=Label(win, text='Account : @', bg=bgColor)
        self.lbl1.place(x=10, y=5)
        self.t1=Entry()
        self.t1.place(x=90, y=5)
        self.lbl2=Label(win, text='Password :', bg=bgColor)
        self.lbl2.place(x=10, y=35)
        self.t2=Entry(show="*")
        self.t2.place(x=90, y=35)

        #DM counter
        self.lbl3=Label(win, text='Nb account to DM (20max /day or you might be banned) :', bg=bgColor)
        self.lbl3.place(x=10, y=125)
        self.nb=Entry()
        self.nb.place(x=365, y=125)

        #Key word research
        self.lbl4=Label(win, text='Key Word research : #', bg=bgColor)
        self.lbl4.place(x=300, y=5)
        self.t3=Entry()
        self.t3.place(x=445,y=5)
        
        #DM message
        self.lbl5=Label(win, text='DM (past here):', bg=bgColor)
        self.lbl5.place(x=300, y=35)
        self.t4=Entry()
        self.t4.place(x=445, y=35)

        #Run button
        self.runButton=Button(win, text='Run', command=run, highlightbackground=bgColor)
        self.runButton.place(x=350, y=250)

def instaBotDM():
    """ Return nothing

    First function wich is the main function that call every module.
    """
    window=Tk()
    mywin=instaBot(window)
    window.title('Insta Bot DM')
    window.geometry("700x300")
    window.configure(bg=bgColor)
    window.resizable(False, False)
    window.mainloop()
