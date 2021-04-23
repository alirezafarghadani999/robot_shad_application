
#!/usr/bin/env python

# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import sys
from colorama import init, AnsiToWin32, Fore, Back
import requests
from datetime import datetime

os.system("cls")

print(Fore.GREEN +"""
_____________________________________

-. http://t.me/protag_programming .-
_____________________________________
<<<<<<<< ALIREZA FARGHADANI >>>>>>>>>

""")
driver = webdriver.Firefox()
driver.set_window_position(-10000,0)
driver.get("https://web.shad.ir")


def login():
    global numbers
    os.system("cls")
    numbers = input(Fore.RED +"shomare telefon : ")
    number = driver.find_element_by_xpath("/html//app-root/tab-login/div[@class='login_page_wrap']//form[@name='mySendCodeForm']//input[@name='phone_number']")
    number.clear();
    number.send_keys(numbers)
    trunum()

def trunum():
    driver.find_element_by_xpath("/html/body//app-root/tab-login/div[@class='login_page_wrap']//span[.='بعدی']").click()
    os.system("cls")
    inputnumtru = input(Fore.RED +"  in shomare -> "+ numbers + " aya dorost ? (y/n) : ")
    if (inputnumtru == "y"):
        driver.find_element_by_xpath("/html//app-root/app-modal-container//app-modal-view/div//div[@class='modal-content modal-content-animated']/app-confirm-custom//span[.='بله']").click()
        codlog()
    if (inputnumtru == "n"):
        driver.find_element_by_xpath("/html//app-root/app-modal-container//app-modal-view/div//div[@class='modal-content modal-content-animated']/app-confirm-custom//span[.='لغو']").click()
        login()

def codlog():
    os.system("cls")
    numcod =input(Fore.RED +"cod ersal shode be shomare shoma , code khod ra vared konid : ")
    codlo = driver.find_element_by_xpath("/html//app-root/tab-login/div[@class='login_page_wrap']//form[@name='myLoginForm']//input[@name='phone_code']")
    codlo.clear()
    codlo.send_keys(numcod)
    logchat()

def logchat():
    os.system("cls")
    print(Fore.GREEN +'''
    rahnama >>>>

    baraye mesal shoma ek groh ro sanjagh mikonid tori ke on groh ya chat hamishe balaye bala mimone
    masalan man groh riyazi ro sanjagh kardam ke balatar az hame chat ha gharar grefte va baraye hamin shomarash mishe 1
    bad chat ya groh badish mishe shomare 2 ta akhar in edame darad vali pishnahad ma in ke chat ro ba narm afzar android sanjagh konid
    ke jaye groh ya chat taghir nakone ....

    <<< ALIREZA FARGHADANI >>>
    
    -------------------------------------------------------------------------->>>

    ''')
    chatid = input(Fore.RED + "shomare chat ya groh mored nazar ro az bala be payin vared konid : ")
    xpathchat = "/html//app-root//rb-chats/div[@class='im_dialogs_col_wrap noselect']/div[@class='im_dialogs_col']/div/div[@class='im_dialogs_scrollable_wrap nano-content']/ul[2]/li["+chatid+"]//div[@class='im_dialog_peer']"
    driver.find_element_by_xpath(xpathchat).click()
    menutocon()


def menutocon():
    os.system("cls")
    print(Fore.YELLOW +'''
    tabrik maigam ta alan hmechi khob bode va khob pish rafte ....
    inja chand ta gozine darim ke mitoni entekhab koni va ba zaman banidi va dadan 
    zaman ersall ya anjameshon ka sorat begire 
    !------------------------------------------------------!

    [ 1 ] .- ersall matn hazeri 
    [ 2 ] .- sherkat dar nazarsanji ya hamon hazeri hoshmand
    [ 3 ] .- araye fake baraye nazarsanji 

    !------------------------------------------------------!

    |    agar ba moshkeli robro shodid mi tavanid va gmail va id telegram zir 
    |    dar ertebat bashid
    |
    |   gmail : alirezaf999.iran@gmail.com
    |   id tel : @alirezaff999

        =======================================''')

    menusel = input(Fore.RED +"       gozine shoma : ")

    if (menusel == "1"):
        sendmsgs()  
    if (menusel == "2"):
        notool()
    if (menusel == "3"):
        notool()
def sendmsgs():
    tiemseth = input(Fore.YELLOW + "zaman ersal ra benevisei be sa at (baraye mesal sa at 09) : ")
    tiemsetm = input(Fore.YELLOW + "zaman ersal ra benevisei be daghighe (baraye mesal daghighe 07) : ")
    msgtext = input("payami ke bayad ersal shavad ra benevisid : ")
    while True:
        now = datetime.now()
        current_timeh = now.strftime("%H")
        current_timem = now.strftime("%M")
        time.sleep(0.5)
        print(Fore.GREEN + "sa at alan >> " + current_timeh+":"+current_timem)
        if (str(current_timeh) == tiemseth):
            if (str(current_timem) == tiemsetm):
                msg = driver.find_element_by_xpath("/html//app-root//app-tab-container/app-tab-view//tab-conversation/div[@class='im_history_col']//div[@class='im_send_panel_wrap noselect']/div/div/form//div[@class='composer_rich_textarea']")
                msg.clear();
                msg.send_keys(msgtext)
                driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()
                print("payam ersal shod ba movafaghiat :) ")
                time.sleep(4)
                os.system("cls")
                back = input(Fore.YELLOW + "baraye bargasht be menu adad 99 ra ersall konid : ")
                if (back == "99"):
                    logchat()

def notool():
    os.system('cls')
    print(Fore.RED +" in abzar darhal sakht ast ... ")
    input(Fore.YELLOW + "enter bezan ta bargardi :)")
    menutocon()

login()