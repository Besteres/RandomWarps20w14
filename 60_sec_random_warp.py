import os
import logging, sys
import time
import sched
from typing import Text
import win32gui
import win32api
import win32con
import win32console
import string
import random

from time import sleep
import win32gui, win32ui, win32con, win32api
#just import EVERYTHING DONT CARE

window_name = "C:\Windows\system32\cmd.exe" #name of the window in use
win32console.SetConsoleTitle("Random 20w14infinite warps By: Besteres") #title of the command prompt of this app
def main():
    print("Make sure that your SERVER command prompt is NAMED 'C:\Windows\system32\cmd.exe'! or else it will not work!")
    print("And remember to not minimize this application or the command prompt... Have fun!")
    print(" ") #reminder of the limitations...
    sleep(1.3)
    print("How much time between random warps?(integer numbers only)")
    input_interval = input()
    try: #verify if input_interval is an integer
        interval = int(input_interval)

    except ValueError: #this happens if theres an error (input was not an integer)
        print("That is not an integer... setting the time to the default value")
        interval = 60

    sleep(2.5)
    print("The time between random warps will be ", interval, "seconds")
    sleep(2.8)
    print("Prepare for chaos and PAIN")
    sleep(10)
    Send_Commands(interval)  


def definedimension(win_):
    eastereggs = ["ant","sponge","basic","blacklight","brand","bridges","busy","chess","colors","content","custom","darkness","decay","fleet","gallery","holes","isolation","library","missing","patterns","perfection","pillars","retro","rooms","shapes","skygrid","slime","spiral","sponge","terminal","tunnels","wall","zones"]
    #easter egg dimensions

    if random.randint(0, 100) < 30: #30% (before was 10) chance of this happening
        easter_egg = random.choice(eastereggs) #get random value from eastereggs list
        letter = 0
        for letter in range(len(easter_egg)): #print the easter_egg value with individual letters (because i cant just print a whole text FOR SOME REASON)
         win_.SendMessage(win32con.WM_CHAR, ord(easter_egg[letter]), 0) #printing the individual letter one BY ONE
        print("The code of this dimension is ", easter_egg, " and this dimension is an easter egg one!") #disclaimer that this is an easter egg!
        return
    else: #this happen when no easter egg :(
     maxlenght = random.randint(5, 9) #random lenght to prevent same dimension patterns
     code = [None] * maxlenght #this is to then show the code of the generated dimension (needs to be the same lenght as the dimension thats going to be generated or else InDeX oUt Of RaNgE!11!!)
     for x in range(maxlenght):
      random_crap = ''.join(random.choice(string.ascii_uppercase) for _ in range(1)) #there we go generating a dimension letter by letter again
      code[x] = random_crap #getting the letter into the list
      win_.SendMessage(win32con.WM_CHAR, ord(random_crap), 0) #sending the random_crap to the command prompt
     print("The code of this dimension is ", *code, sep='') #saying what code this dimension is without the brackets and the commas



def Send_Commands(inter_):
    
    timeleft = inter_
    print("Executing Command....")
    
    hwnd = win32gui.FindWindow(None, window_name) #finding the window with the name 'window_name'
    win = win32ui.CreateWindowFromHandle(hwnd) #i have no fucking clue about what this does BUT I NEED THIS FOR THE APP TO WORK!
    

    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('x'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('c'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('s'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('@'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('w'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('p'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0) #print initial command into the command prompt 'execute as @a run warp '

    definedimension(win) #generate dimension to be warped to

    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    
    print("Command has been made... waiting ", timeleft ,"seconds to send the command again")
    sleep(timeleft)
    Send_Commands(timeleft)# after this is done just loop yourself after the time that the user typed in has passed

main() 



