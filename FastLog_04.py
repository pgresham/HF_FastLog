from Tkinter import *
import time
import datetime

#following are the file functions usable for this:
  
def file_accessible(filepath, mode):
    ''' Check if a file exists and is accessible.
        Many Thanx to pythoncentral.io for this
        code block. '''
    try:
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False
 
    return True

#following main code opens log file, checks if day log already exists.
    
filename = ''
t = datetime.date.today()
t = str(t)
if file_accessible(t + '.txt','a'):
    f = open(t + '.txt','a')
    f.write('\n')
else:
    f = open((t + '.txt','w'))    
#The filetype could very well be anything here.
#I elected to use *.txt for ease of opening in
#Notepad to make print-outs. Consiering changing
#subsequent versions to .log filetype. 



#following are the Button Functions:

def callback():

    log_test  = e1.get()
    if log_test != 'call sign':
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
        e1.insert(0,'call sign')
        #c1 checkbutton to lock frequency
        if f1.get():
            pass
        else:
            e2.delete(0,END)
            e2.insert(0,'frequency')
        #c2 checkbutton to lock mode
        if f2.get():
            pass
        else:
            e3.delete(0,END)
            e3.insert(0,'mode')
        #c3 checkbutton to lock r/s/t (this is a nod to robo-DX'ers)
        if f3.get():
            pass
        else:
            e4.delete(0,END)
            e4.insert(0,'rst')
    else:
        print 'blank entry'
        e1.delete(0,END)
        e1.insert(0,'call sign')
        #c1 checkbutton to lock frequency
        if f1.get():
            pass
        else:
            e2.delete(0,END)
            e2.insert(0,'frequency')
        #c2 checkbutton to lock mode
        if f2.get():
            pass
        else:
            e3.delete(0,END)
            e3.insert(0,'mode')
        #c3 checkbutton to lock r/s/t (this is a nod to robo-DX'ers)
        if f3.get():
            pass
        else:
            e4.delete(0,END)
            e4.insert(0,'rst')
def clearall():
#note: checkbuttons enabled will not be cleared.
    try:
        e1.delete(0,END)
        e1.insert(0,'call sign')
        
        if f1.get():
            pass
        else:
            e2.delete(0,END)
            e2.insert(0,'frequency')
       
        if f2.get():
            pass
        else:
            e3.delete(0,END)
            e3.insert(0,'mode')
        
        if f3.get():
            pass
        else:
            e4.delete(0,END)
            e4.insert(0,'rst')
    except:
        print 'error clearall'

master = Tk()
#Update the number as this evolves.
master.wm_title('Fast Log 0.4 Beta') 

e1 = Entry(master)
e1.grid(row = 1, column = 0)
e1.delete(0, END)
e1.insert(0, 'call sign')
e1.focus_set()

e2 = Entry(master)
e2.grid(row = 1, column = 1)
e2.delete(0, END)
e2.insert(0, 'frequency')
e2.focus_set()

e3 = Entry(master)
e3.grid(row = 1, column = 2)
e3.delete(0, END)
e3.insert(0, 'mode')
e3.focus_set()

e4 = Entry(master)
e4.grid(row = 1, column = 3)
e4.delete(0, END)
e4.insert(0, 'rst')
e4.focus_set()


f1 = IntVar()
f2 = IntVar()
f3 = IntVar()


c1 = Checkbutton(master, text = 'lock frequency ',variable = f1).grid(row = 2, column = 1)
c2 = Checkbutton(master, text = 'lock mode ',variable = f2).grid(row = 2, column = 2)
c3 = Checkbutton(master, text = 'lock rst ',variable = f3).grid(row = 2, column = 3)


enter = Button(master, text = 'log', width = 10, command = callback).grid(row = 1, column = 4)
clear = Button(master, text = 'clear', width = 10, command = clearall).grid(row = 2, column = 4)

#clock module

clock = Label(master)
clock.grid(row = 2, column = 0)
time1 =''

def tick():
    global time1 
    time2 = time.strftime('%a, %d %b %Y  %H:%M:%S ',gmtime())
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick) #200 ms accuracy to the clock. This does not generate the timestamp in the files, however.


tick()
master.mainloop()
f.close()


