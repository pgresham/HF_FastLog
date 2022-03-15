#!/usr/bin/python3

#This is version 2.0.1 updated for Python 3.x.x
#Fastlog is a simple GUI to log Amateur Radio 
#contacts in a text-based log. 

#Updates in 2.0.1 from 1.0.0 include syntax fixes
#for Python 2 to 3 (Mostly print statements) as 
#well as some cleaning up of the UI and coding
#style as well as the addition of an exit button.

#73's and good DX


from tkinter import *
import time
from time import strftime, gmtime
from datetime import datetime
from datetime import date
import datetime
import os.path

def file_accessible(filepath, mode):
    try:
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False
 
    return True
    

def callback():

    log_test  = e1.get()
    if log_test != '':
        callsign = e1.get()
        while len(callsign) < 8:
            callsign += ' '
        frequency = e2.get()
        while len(frequency) < 8:
            frequency += ' '
        mode = e3.get()
        while len(mode) < 8:
            mode += ' '
        rst = e4.get()
        while len(rst) < 4:
            rst += ' '
            
        #The following puts the UTC Timestamp in a 'usable' format onto each log entry
        now = str( datetime.datetime.utcfromtimestamp(time.time()))
        full_entry = callsign + '  ' + frequency + '  ' + mode + '  ' + rst + '  ' + now + '\n'
        f.write(full_entry)
        e1.delete(0,END)
        #c1 checkbutton to lock frequency
        if f1.get():
            pass
        else:
            e2.delete(0,END)
        #c2 checkbutton to lock mode
        if f2.get():
            pass
        else:
            e3.delete(0,END)
        #c3 checkbutton to lock rst (robo-DX style)
        if f3.get():
            pass
        else:
            e4.delete(0,END)
    else:
        print( 'blank entry')
        e1.delete(0,END)
        
        if f1.get():
            pass
        else:
            e2.delete(0,END)
        
        if f2.get():
            pass
        else:
            e3.delete(0,END)
        
        if f3.get():
            pass
        else:
            e4.delete(0,END)

def clearall():
#note: checkbuttons enabled will not be cleared.
    try:
        e1.delete(0,END)

        if f1.get():
            pass
        else:
            e2.delete(0,END)
       
        if f2.get():
            pass
        else:
            e3.delete(0,END)
        
        if f3.get():
            pass
        else:
            e4.delete(0,END)

    except Exception as e:
        print(e)


master = Tk()
#Update the number as this evolves.
master.wm_title('Fast Log 2.0.1') 

e1 = Entry(master)
e1.grid(row = 1, column = 0)
e1.delete(0, END)
e1.focus_set()


e2 = Entry(master)
e2.grid(row = 1, column = 1)
e2.delete(0, END)
e2.focus_set()

e3 = Entry(master)
e3.grid(row = 1, column = 2)
e3.delete(0, END)
e3.focus_set()

e4 = Entry(master)
e4.grid(row = 1, column = 3)
e4.delete(0, END)
e4.focus_set()

l1 = Label(master, text='Callsign')
l1.grid(row=2,column=0)

l2 = Label(master, text='Frequency')
l2.grid(row=2,column=1)

l3 = Label(master, text='Mode')
l3.grid(row=2,column=2)

l4 = Label(master, text='RST')
l4.grid(row=2,column=3)


f1 = IntVar()
f2 = IntVar()
f3 = IntVar()


c1 = Checkbutton(master, text = 'lock frequency ',variable = f1).grid(row = 4, column = 1)
c2 = Checkbutton(master, text = 'lock mode ',variable = f2).grid(row = 4, column = 2)
c3 = Checkbutton(master, text = 'lock rst ',variable = f3).grid(row = 4, column = 3)


enter = Button(master, text = 'log', width = 10, command = callback).grid(row = 1, column = 4)
clear = Button(master, text = 'clear', width = 10, command = clearall).grid(row = 2, column = 4)

#clock module

clock = Label(master)
clock.grid(row = 4, column = 0)
time1 =''

def tick():
    global time1 
    time2 = time.strftime('%a, %d %b %Y  %H:%M:%S ',gmtime())
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick) #200 ms accuracy to the clock. This does not generate the timestamp in the files, however.

if __name__ == '__main__':


    try:
        tick()
        if not os.path.exists('logs'):
            os.makedirs('logs')         
        else:
            pass
        t = str(datetime.date.today())
        t = os.path.abspath('logs/%s.log'%t)
        if file_accessible(t,'a'):
            f = open(t,'a')
            f.write('\n')
        else:
            f = open(t,'w')   
            
        master.mainloop()
    except Exception as e:
        print(e)
    finally:
        try:
            if f:
                f.close()
                exit(0)
            else:
                exit(0)
        except:
        	exit(0)
