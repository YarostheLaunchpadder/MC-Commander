# IMPORT LIBRARIES
from pynput.keyboard import Key, Controller
from tkinter import *
from tkinter.ttk import *
import time
import sys
import pyperclip
from PIL import ImageTk, Image
from pathlib import Path

#WINDOW SETUP
window = Tk()
window.title("MC Commander")
window.geometry('675x300')
window.resizable(width=False, height=False)
window.iconbitmap("minecraft_icon.ico")

# DISPLAY LOGO
logo = ImageTk.PhotoImage(Image.open("logo/minecraft_logo.png"))
logolabel = Label(window, image=logo).place(x=325, y=1)


# CHECK NICKNAME
nicknamefile=open("nickname.txt", "r")
filecontents = nicknamefile.read()
nickname = filecontents
currentnick = Label(window, text="Current nick: " + (filecontents) + "                                 ", font=("Calibri", 11))
currentnick.place(x=495, y=57)

# FUNCTIONS

# NICK MANAGEMENT
def usenick():
    global nickname
    nickname = str(nickentry.get())
    currentnick = Label(window, text="Current nick: " + (nickname) + "                                             ", font=("Calibri", 11))
    currentnick.place(x=495, y=57)

def remembernick():
    nickfile = open('nickname.txt', 'w')
    nickget = str(nickentry.get())
    nickfile.write(nickget)
    nickfile.close()
    global nickname
    nickname = str(nickentry.get())
    currentnick = Label(window, text="Current nick: " + (nickname) + "                                             ", font=("Calibri", 11))
    currentnick.place(x=495, y=57)

def deletenick():
    nickfile = open('nickname.txt', 'w')
    nickfile.write("")
    nickfile.close()
    global nickname
    nickname = ("")
    currentnick = Label(window, text="Current nick: NONE                                        ", font=("Calibri", 11))
    currentnick.place(x=495, y=57)

# ROW 1  
def killentity():
    killcommand = "/kill " + (nickname)
    pyperclip.copy(killcommand)
    
def kickentity():
    kickcommand = "/kick " + (nickname)
    pyperclip.copy(kickcommand)
    
def banentity():
    bancommand = "/ban " + (nickname)
    pyperclip.copy(bancommand)
    
def unbanentity():
    unbancommand = "/pardon " + (nickname)
    pyperclip.copy(unbancommand)

def opentity():
    opcommand = "/op " + (nickname)
    pyperclip.copy(opcommand)

def deopentity():
    deopcommand = "/deop " + (nickname)
    pyperclip.copy(deopcommand)

def starttp():
    global tptargetentry
    tpcoords = str(tptargetentry.get())
    tpcommand = "/tp " + (nickname) + " " + (tpcoords)
    pyperclip.copy(tpcommand)
    tpwindow.destroy()

# ROW 2
def cblockchosen():
    cblockcommand = "/give " + (nickname) + " minecraft:command_block"
    pyperclip.copy(cblockcommand)
    pblock.destroy()

def bblockchosen():
    bblockcommand = "/give " + (nickname) + " minecraft:barrier"
    pyperclip.copy(bblockcommand)
    pblock.destroy()

def invisibilitychosen():
    edurationstr = str(effectduration.get())
    invisibilitycommand = "/effect give " + (nickname) + " minecraft:invisibility " + (edurationstr) + " 1 true"
    pyperclip.copy(invisibilitycommand)
    peffect.destroy()

def nightvisionchosen():
    edurationstr = str(effectduration.get())
    nvcommand = "/effect give " + (nickname) + " minecraft:night_vision " + (edurationstr) + " 1 true"
    pyperclip.copy(nvcommand)
    peffect.destroy()

def slowfallingchosen():
    edurationstr = str(effectduration.get())
    sfcommand = "/effect give " + (nickname) + " minecraft:slow_falling " + (edurationstr) + " 2 true"
    pyperclip.copy(sfcommand)
    peffect.destroy()

def speedchosen():
    edurationstr = str(effectduration.get())
    speedcommand = "/effect give " + (nickname) + " minecraft:speed " + (edurationstr) + " 2 true"
    pyperclip.copy(speedcommand)
    peffect.destroy()

def jumpboostchosen():
    edurationstr = str(effectduration.get())
    jbcommand = "/effect give " + (nickname) + " minecraft:jump_boost " + (edurationstr) + " 5 true"
    pyperclip.copy(jbcommand)
    peffect.destroy()

# ROW 3
def gmsurvival():
    gmscommand = "/gamemode survival"
    pyperclip.copy(gmscommand)

def gmcreative():
    gmccommand = "/gamemode creative"
    pyperclip.copy(gmccommand)

def gmspectator():
    gmspcommand = "/gamemode spectator"
    pyperclip.copy(gmspcommand)

def gmadventure():
    gmacommand = "/gamemode adventure"
    pyperclip.copy(gmacommand)

# ROW 4
def daychosen():
    global timesetday
    timesetday = "/time set noon"
    pyperclip.copy(timesetday)
    timewin.destroy()

def nightchosen():
    global timesetnight
    timesetnight = "/time set midnight"
    pyperclip.copy(timesetnight)
    timewin.destroy()

def clearchosen():
    global weatherclear
    weatherclear = "/weather clear"
    pyperclip.copy(weatherclear)
    weatherwin.destroy()

def rainchosen():
    global weatherrain
    weatherrain = "/weather rain"
    pyperclip.copy(weatherrain)
    weatherwin.destroy()

def thunderchosen():
    global weatherthunder
    weatherthunder = "/weather thunder"
    pyperclip.copy(weatherthunder)
    weatherwin.destroy()

def lightcycletruechosen():
    global daylightcycletrue
    daylightcycletrue = "/gamerule doDaylightCycle true"
    pyperclip.copy(daylightcycletrue)
    daylightcyclewin.destroy()

def lightcyclefalsechosen():
    global daylightcyclefalse
    daylightcyclefalse = "/gamerule doDaylightCycle false"
    pyperclip.copy(daylightcyclefalse)
    daylightcyclewin.destroy()

def weathercycletruechosen():
    global weathercycletrue
    weathercycletrue = "/gamerule doWeatherCycle true"
    pyperclip.copy(weathercycletrue)
    weatherwin.destroy()

def weathercyclefalsechosen():
    global weathercyclefalse
    weathercyclefalse = "/gamerule doWeatherCycle false"
    pyperclip.copy(weathercyclefalse)
    weatherwin.destroy()

# TELEPORT WINDOW
def opentpwindow():
    global tpwindow
    tpwindow = Toplevel()
    tpwindow.title('Teleport character')
    tpwindow.geometry('400x100')
    tpwindow.resizable(width=False, height=False)
    tpwindow.iconbitmap("minecraft_icon.ico")

    global tplogo
    tplogo = ImageTk.PhotoImage(Image.open("tp/teleport.png"))
    tplogolabel = Label(tpwindow, image=tplogo).place(x=1, y=1)
    
    tplabel = Label(tpwindow, text="Teleport player", font=("Arial Bold", 11))
    tplabel.place(x=55, y=15)

    tlocationlabel = Label(tpwindow, text="Target location:", font=("Arial", 11))
    tlocationlabel.place(x=1, y=60)

    global tptargetentry
    tptargetentry = Entry(tpwindow)
    tptargetentry.place(x=107, y=60)

    tpgo = Button(tpwindow, text="GO!", command=starttp)
    tpgo.place(x=238, y=58)

# PICK BLOCK WINDOW
def pickblock():
    global pblock
    pblock = Toplevel()
    pblock.title('Pick a block')
    pblock.geometry('145x70')
    pblock.resizable(width=False, height=False)
    pblock.iconbitmap("minecraft_icon.ico")
    
    global cblock
    cblock = ImageTk.PhotoImage(Image.open("block/cblock.png"))
    Button(pblock, image=cblock,command=cblockchosen).place(x=5, y=3)
    
    global bblock
    bblock = ImageTk.PhotoImage(Image.open("block/bblock.png"))
    Button(pblock, image=bblock,command=bblockchosen).place(x=75, y=3)

# PICK EFFECT WINDOW
def pickeffect():
    global peffect
    peffect = Toplevel()
    peffect.title("Pick an effect")
    peffect.geometry('500x70')
    peffect.resizable(width=False, height=False)
    peffect.iconbitmap("minecraft_icon.ico")

    edurationlabel = Label(peffect, text="Effect duration:", font=("Calibri", 11))
    edurationlabel.place(x=350, y=20)

    global effectduration
    effectduration = Spinbox(peffect, from_ = 10, to = 60, width = 4)
    effectduration.place(x=453, y=22)
    
    global invisibility
    invisibility = ImageTk.PhotoImage(Image.open("effect/invisibility.png"))
    Button(peffect, image=invisibility,command=invisibilitychosen).place(x=5, y=3)

    global nightvision
    nightvision = ImageTk.PhotoImage(Image.open("effect/night_vision.png"))
    Button(peffect, image=nightvision,command=nightvisionchosen).place(x=75, y=3)

    global slowfalling
    slowfalling = ImageTk.PhotoImage(Image.open("effect/slow_falling.png"))
    Button(peffect, image=slowfalling,command=slowfallingchosen).place(x=145, y=3)

    global speed
    speed = ImageTk.PhotoImage(Image.open("effect/speed.png"))
    Button(peffect, image=speed,command=speedchosen).place(x=215, y=3)

    global jumpboost
    jumpboost = ImageTk.PhotoImage(Image.open("effect/jump_boost.png"))
    Button(peffect, image=jumpboost,command=jumpboostchosen).place(x=285, y=3)

# PICK TIME WINDOW
def timewindow():
    global timewin
    timewin = Toplevel()
    timewin.title('Change time')
    timewin.geometry('135x70')
    timewin.resizable(width=False, height=False)
    timewin.iconbitmap("minecraft_icon.ico")

    global setday
    setday = ImageTk.PhotoImage(Image.open("daynight/day.png"))
    Button(timewin, image=setday,command=daychosen).place(x=5, y=3)

    global setnight
    setnight = ImageTk.PhotoImage(Image.open("daynight/night.png"))
    Button(timewin, image=setnight,command=nightchosen).place(x=70, y=3)
    
# PICK WEATHER WINDOW
def weatherwindow():
    global weatherwin
    weatherwin = Toplevel()
    weatherwin.title('Change weather')
    weatherwin.geometry('200x70')
    weatherwin.resizable(width=False, height=False)
    weatherwin.iconbitmap("minecraft_icon.ico")

    global setclear
    setclear = ImageTk.PhotoImage(Image.open("weather/clear.png"))
    Button(weatherwin, image=setclear,command=clearchosen).place(x=1, y=3)

    global setrain
    setrain = ImageTk.PhotoImage(Image.open("weather/rain.png"))
    Button(weatherwin, image=setrain,command=rainchosen).place(x=65, y=3)

    global setthunder
    setthunder = ImageTk.PhotoImage(Image.open("weather/thunder.png"))
    Button(weatherwin, image=setthunder,command=thunderchosen).place(x=132, y=3)

# DAYLIGHT CYCLE WINDOW
def daylightwindow():
    global daylightcyclewin
    daylightcyclewin = Toplevel()
    daylightcyclewin.title('Do DayLight Cycle setting')
    daylightcyclewin.geometry('175x35')
    daylightcyclewin.resizable(width=False, height=False)
    daylightcyclewin.iconbitmap("minecraft_icon.ico")

    Button(daylightcyclewin,text="True",command=lightcycletruechosen).place(x=5, y=4)
    Button(daylightcyclewin,text="False",command=lightcyclefalsechosen).place(x=85, y=4)

# WEATHER CYCLE WINDOW
def weathercyclewindow():
    global weatherwin
    weatherwin = Toplevel()
    weatherwin.title('Do weather cycle setting')
    weatherwin.geometry('175x35')
    weatherwin.resizable(width=False, height=False)
    weatherwin.iconbitmap("minecraft_icon.ico")

    Button(weatherwin,text="True",command=weathercycletruechosen).place(x=5, y=4)
    Button(weatherwin,text="False",command=weathercyclefalsechosen).place(x=85, y=4)

# LABELS
welcome = Label(window, text="Welcome to", font=("Arial Bold", 15))
welcome.place(x=200, y=0)

appname = Label(window, text="MC Commander", font=("Minecraft", 14))
appname.place(x=195, y=24)

asknick = Label(window, text="Target nickname:", font=("Calibri", 11))
asknick.place(x=1, y=55)

pctext = Label(window, text="Player control:", font=("Calibri", 11))
pctext.place(x=1, y=90)

betext = Label(window, text="Blocks/Effects:", font=("Calibri", 11))
betext.place(x=1, y=135)

gsettings = Label(window, text="Game Settings:", font=("Calibri", 11))
gsettings.place(x=1, y=180)

wsettings = Label(window, text="World Control:", font=("Calibri", 11))
wsettings.place(x=1, y=225)

appbyyaros = Label(window, text="App made by YAROS", font=("Arial Bold", 15))
appbyyaros.place(x=467, y=272)

# ENTRY FIELDS
nickentry = Entry(window)
nickentry.place(x=115, y=58)

# BUTTONS
usecurrent = Button(text="Use", command=usenick)
usecurrent.place(x=245, y=56)

savenick = Button(text="Remember", command=remembernick)
savenick.place(x=325, y=56)

deletenick = Button(text="Clear memory", command=deletenick)
deletenick.place(x=405, y=56)

kill = Button(text="Kill", command=killentity)
kill.place(x=100, y=90)

kick = Button(text="Kick", command=kickentity)
kick.place(x=180, y=90)

ban = Button(text="Ban", command=banentity)
ban.place(x=260, y=90)

unban = Button(text="Unban", command=unbanentity)
unban.place(x=340, y=90)

unban = Button(text="OP", command=opentity)
unban.place(x=420, y=90)

unban = Button(text="Deop", command=deopentity)
unban.place(x=500, y=90)

tp = Button(text="Teleport", command=opentpwindow)
tp.place(x=580, y=90)

blocks = Button(text="Blocks", command=pickblock)
blocks.place(x=100, y=135)

effects = Button(text="Effects", command=pickeffect)
effects.place(x=180, y=135)

survival = Button(text="Survival",command=gmsurvival)
survival.place(x=100, y=180)

creative = Button(text="Creative",command=gmcreative)
creative.place(x=180, y=180)

spectator = Button(text="Spectator",command=gmspectator)
spectator.place(x=260, y=180)

adventure = Button(text="Adventure",command=gmadventure)
adventure.place(x=340, y=180)

settime = Button(text="Set time",command=timewindow)
settime.place(x=100, y=225)

setweather = Button(text="Set weather",command=weatherwindow)
setweather.place(x=180, y=225)

dodaylightcycle = Button(text="Do DayLight Cycle",command=daylightwindow)
dodaylightcycle.place(x=260, y=225)

dodayweathercycle = Button(text="Do Weather Cycle",command=weathercyclewindow)
dodayweathercycle.place(x=370, y=225)

window.mainloop()
