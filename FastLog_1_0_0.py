from Tkinter import *
import time
from time import strftime, gmtime
from datetime import datetime
from datetime import date
import datetime

import os.path

def file_accessible(filepath, mode):
    ''' Check if a file exists and is accessible.
        Many Thanx to pythoncentral.io for this
        code block. '''
    try:
        fileWrite = open(filepath, mode)
        fileWrite.close()
    except IOError as e:
        return False
 
    return True
    
if not os.path.exists('logs'):
    os.makedirs('logs')         
t = str(datetime.date.today())
t = os.path.abspath('logs/%s.log'%t)
if file_accessible(t,'a'):
    fileWrite = open(t,'a')
else:
    fileWrite = open(t,'w')   

#updated as of ver 1.0.0 to write to logs directory!
#filetype changed from .txt to .log


def callback():
    log_test  = txtboxCallSign.get()
    freq_test = txtboxFrequency.get()
    if (log_test != 'call sign') and  (len(freq_test) != 0):
        callsign = txtboxCallSign.get()
        while len(callsign) < 8:
            callsign += ' '

        #To make sure that the user has inputted some form of number
        try:
            frequency = float(txtboxFrequency.get())
        except:
            print "Frequency not valid"
            return        
        while len(str(frequency)) < 8:
            frequency += ' '
        mode = txtboxMode.get()
        while len(mode) < 8:
            mode += ' '
        rst = txtboxRst.get()
        while len(rst) < 4:
            rst += ' '
            
        #The following puts the UTC Timestamp in a 'usable' format onto each log entry
        now = str( datetime.datetime.utcfromtimestamp(time.time()))
        full_entry = callsign + '  ' + frequency + '  ' + mode + '  ' + rst + '  ' + now + "\n"
        fileWrite.write(full_entry)
        txtboxCallSign.delete(0,END)
        txtboxCallSign.insert(0,'call sign')
        #checkFreqLock checkbutton to lock frequency
        if varFreqLock.get():
            pass
        else:
            txtboxFrequency.delete(0,END)
            txtboxFrequency.insert(0,'frequency')
        #checkModeLock checkbutton to lock mode
        if varModeLock.get():
            pass
        else:
            txtboxMode.delete(0,END)
            txtboxMode.insert(0,'mode')
        #checkRstLock checkbutton to lock r/s/t (this is a nod to robo-DX'ers)
        if varRstLock.get():
            pass
        else:
            txtboxRst.delete(0,END)
            txtboxRst.insert(0,'rst')
    else:
        print 'blank entry'

def clearall():
#note: checkbuttons enabled will not be cleared.
    try:
        txtboxCallSign.delete(0,END)
        txtboxFrequency.delete(0,END)
        txtboxMode.delete(0,END)
        txtboxRst.delete(0,END)
    except:
        print 'error clearall'

#UI initialisation start
master = Tk()
#Update the number as this evolves.
master.wm_title('Fast Log 1.1.1') 

txtboxCallSign = Entry(master)
txtboxCallSign.grid(row = 1, column = 0)
txtboxCallSign.delete(0, END)
txtboxCallSign.focus_set()

txtboxFrequency = Entry(master)
txtboxFrequency.grid(row = 1, column = 1)
txtboxFrequency.delete(0, END)
txtboxFrequency.focus_set()

txtboxMode = Entry(master)
txtboxMode.grid(row = 1, column = 2)
txtboxMode.delete(0, END)
txtboxMode.focus_set()

txtboxRst = Entry(master)
txtboxRst.grid(row = 1, column = 3)
txtboxRst.delete(0, END)

txtboxRst.focus_set()


varFreqLock = IntVar()
varModeLock = IntVar()
varRstLock = IntVar()


checkFreqLock = Checkbutton(master, text = 'lock frequency ',variable = varFreqLock).grid(row = 2, column = 1)
checkModeLock = Checkbutton(master, text = 'lock mode ',variable = varModeLock).grid(row = 2, column = 2)
checkRstLock = Checkbutton(master, text = 'lock rst ',variable = varRstLock).grid(row = 2, column = 3)


enter = Button(master, text = 'log', width = 10, command = callback).grid(row = 1, column = 4)
clear = Button(master, text = 'clear', width = 10, command = clearall).grid(row = 2, column = 4)

#clock module

clock = Label(master)
clock.grid(row = 2, column = 0)
timtxtboxCallSign =''


lblCall = Label(master)
lblCall.grid(row = 0, column = 0)
txtCall = "Call sign"
lblCall.config(text=txtCall)

lblFreq = Label(master)
lblFreq.grid(row = 0, column = 1)
txtFreq = "Frequency"
lblFreq.config(text=txtFreq)

lblMode =  Label(master)
lblMode.grid(row = 0, column = 2)
txtMode = "mode"
lblMode.config(text=txtMode)

lblRst = Label(master)
lblRst.grid(row = 0, column = 3)
txtRst = "rst"
lblRst.config(text=txtRst)

#UI initialization end

def tick():
    global timtxtboxCallSign 
    timtxtboxFrequency = time.strftime('%a, %d %b %Y  %H:%M:%S ',gmtime())
    if timtxtboxFrequency != timtxtboxCallSign:
        timtxtboxCallSign = timtxtboxFrequency
        clock.config(text=timtxtboxFrequency)
    clock.after(200, tick) #200 ms accuracy to the clock. This does not generate the timestamp in the files, however.


tick()
master.mainloop()
fileWrite.close()
