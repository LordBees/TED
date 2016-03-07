##http://bit.do/list-of-url-shorteners.php
##http://www.hongkiat.com/blog/url-shortening-services-the-ultimate-list/
import random,webbrowser,os
from tkinter import *
from tkinter import messagebox
FILE_HISTORY = 'history.dat'
vchars = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
history = []
root = Tk()
linktype_Radio = IntVar()
gennedlink = StringVar()
def openrng():##button funct
    global gennedlink
    print('link = ',gennedlink.get())
    webbrowser.open(gennedlink.get())

    
def googlehome():##button funct
    webbrowser.open('google.co.uk')

    
def save_file(name,data,overwrite = False,array = False):#saving funct
    if overwrite:
        f = open(name,'r+')
    else:
        f = open(name,'w')
    if array:
        for x in data:
            f.write(x+'\n')
    else:
        for x in data:
            f.write(x)
    f.close()


def loadfile(name):##loading funct
    contents = []
    f = open(name,'r')
    for x in f.readlines():
        contents.append(x.strip('\n'))
    f.close()
    return contents


def load_history_ext():
    global history
    if askokcancel():
        history = loadfile(FILE_HISTORY)

def load_history():
    global history
    if FILE_HISTORY in os.listdir():
        history = loadfile(FILE_HISTORY)
    else:
        save_file(FILE_HISTORY,['the history file'])

    
def save_history():
    global history
    save_file(FILE_HISTORY,history,array = True)

def refresh_Hbox():
    history_Listbox.delete(0,history_Listbox.size())
    for x in history:
        history_Listbox.insert(END,x)
       
def genlink():##button funct
    if linktype_Radio.get() == 0:
        pass
    else:
        if linktype_Radio.get()   ==  1:
            gennedlink.set(get_tinyurl())##eg http://tinyurl.com/DlJzJ
        elif linktype_Radio.get() ==  2:
            gennedlink.set(get_BitLy())
        elif linktype_Radio.get() ==  3:
            gennedlink.set(get_googl())
        history.append(gennedlink.get())
        save_history()
        linkbox_Label.config(text = str(gennedlink.get()))
        refresh_Hbox()

        
def setlink():
    global history_listbox
    if history_Listbox.curselection() == None:##checks if valid
        pass
    else:
        gennedlink.set(history_Listbox.get(history_Listbox.curselection()))
        linkbox_Label.config(text = str(gennedlink.get()))


def get_tinyurl():   
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://tinyurl.com/'+link


def get_BitLy():
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://bit.ly/'+link


def get_googl():
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://goo.gl/'+link
    
def on_run():
    load_history()
    refresh_Hbox()

    
def on_close():
    #save_history()##better to save direct
    print('cleanup')
    
    
def asciidump_ext():
	chrs = []
	for x in range(0,255):
		chrs.append(str(chr(x)))
	return chrs






###
ol_LF = LabelFrame(root,text = 'open link')##openlink 
lr_LF = LabelFrame(root,text = 'pick a link type')##linkradio
historyscroller_Scrollbar = Scrollbar(root)
history_Listbox = Listbox(root,yscrollcommand = historyscroller_Scrollbar.set)
historyscroller_Scrollbar.config(command = history_Listbox.yview)

tinyurl_radio = Radiobutton(lr_LF,text = 'tinyurl',variable = linktype_Radio,value = 1)
bitly_radio = Radiobutton(lr_LF,text = 'Bit.ly',variable = linktype_Radio,value = 2)
c_radio = Radiobutton(lr_LF,text = 'goo.gl',variable = linktype_Radio,value = 3)
genlnk_Button = Button(ol_LF,command = genlink,text = 'generate\nlink')
openlnk_Button = Button(ol_LF,command = openrng,text = 'open link')
opengoogle_Button = Button(root,command = googlehome,text = 'google homepage')
selectlink_Button = Button(root,command = setlink,text = 'select link')
linkbox_Label = Label(root)


lr_LF.pack()
ol_LF.pack()

tinyurl_radio.pack()
bitly_radio.pack()
c_radio.pack()
genlnk_Button.pack()
openlnk_Button.pack()
opengoogle_Button.pack()
selectlink_Button.pack()
linkbox_Label.pack()
history_Listbox.pack()
historyscroller_Scrollbar.pack()


on_run()
root.geometry('300x300')
root.mainloop()
on_close()

