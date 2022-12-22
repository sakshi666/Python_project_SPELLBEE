# importing the necessary modules
from tkinter import *
from tkinter import messagebox
import random
from tkinter.font import BOLD, ITALIC
import pyttsx3




win=Tk()
win.geometry("700x700")
win.title("SPELL BEE")



engine = pyttsx3.init() # object creation



# setting the text to speech
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate



"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1



"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female



# inititating variables required (list of words, score, etc)
le1=['architecture', 'dazzling', 'lush',   'resume',  'daffodills',
    'cliche',  'cuisine',  'billionaire',  'charcoal',  'boomerang']


le2=['adolescence',  'diaphragm',  'hierarchy',   'lenience',   'millennium',
     'sergeant',   'conscious',   'pisces',   'chihuahua',   'pretence']


le3=['questionnaire',  'omniscience',  'recapitulate',   'asceticism',   'sorbet',
     'rendezvous','    pnemonoultramicroscopicsilicovolcanoconiosis',   'apocalypse' ]



le=[le1,le2,le3]
c1=1; c=sc=0
for i in le:
    random.shuffle(i)



# function to destroy elements
def delel(*args):
    for arg in args:
        arg.destroy()



# function for speaking
def f5(item):
    engine.say(item)
    engine.runAndWait()




# function for changing states (normal,disabled) of widgets
def wstate(state,*widgets):
    for widget in widgets:
        widget['state']= state





# function for yes button
def f1():

    # function for enter button
    def f3():
        global c,w,sc,c1,le
        if (len(t1.get())!=0) and (not (t1.get()).isspace()):
            t1['state']='disabled'
            if ((t1.get()).strip()).lower()==w[c1-1][c]:
                messagebox.showinfo("Info","Correct")
                f5("Correct")
                sc=sc+1
            else:
                messagebox.showinfo("Info","Incorrect")
                f5("Incorrect")
            c=c+1
            wstate('normal',b4)
            wstate('disabled',b3,b6)
        else:
            messagebox.showinfo("Info","Please type word")
        if c==2:
            delel(l3,b3,b4,t1,b6,l10)
            global l7,l8,l9,b10
            st="Your score for level " + str(c1) + " is "+str(sc)
            if c1!=3:
                st1="You have reached the \n end of level "+str(c1)
            else:
                st1="You have reached the \n end of the game"
            l7=Label(canvas,text=st1,bg="#f2c941",fg="black",font=("Helvetica",48,BOLD))
            l7.place(x=10,y=25)
            l8=Label(canvas,text=st,bg="#f2c941",fg="black", font=("Helvetica",38,BOLD))
            l8.place(x=65,y=225)
            b10=Button(canvas,text="Level up", bg='black', fg='white',font=("Times",15),command=f10)
            b10.place(x=325,y=350)
                      
    


    # function for next button
    def f4():
        global w
        wstate('normal',b3,t1,b6)
        t1.delete(0, END)
        f5("Your word is: ")
        f5(w[c1-1][c])
        wstate('disabled',b4)

    



    # function for Repeat word button   
    def f6():
        global w
        f5(w[c1-1][c])

        



    # function to level up
    def f10():
        global c1,c,sc,w
        if c1<3 and sc>=1:
            c1=c1+1
            delel(canvas,frame,l6,l7,l8,b10)
            c=sc=0
            level()
            f5("Your word is: ")
            f5(w[c1-1][c])
        elif c1<3 and sc<1:
            messagebox.showinfo("Info","You have failed to clear level")
            win.destroy()
        else:
            wstate('disabled',b10)
        



    # function to set levels
    def level():
        global l6,l3,t1,b3,b4,b6,l10,canvas,frame,levels
        levels="Level "+str(c1)
        frame=Frame(win,bg="black",width=700)
        frame.pack(fill = "both", expand = True)
        l6=Label(frame,text="SPELL BEE",bg="black",fg="white",font=("Times",75,BOLD))
        l6.place(x=70,y=80)
        canvas=Canvas(win, bg="#f2c941",width = 700)
        canvas.pack(fill = "both", expand = True)
        l10=Label(canvas,text=levels,bg="black",fg="white",font=("Comic sans",45,BOLD))
        l10.place(x=250,y=60)
        l3=Label(canvas,text="Type down your word here: ",bg="#f2c941",fg="black",font=("Helvetica",25,BOLD))
        l3.place(x=140,y=175)
        t1=Entry(canvas)
        t1.place(x=290,y=255)
        b3=Button(canvas,text="Enter",bg='black', fg='white',font=("Times",15),command=f3)
        b3.place(x=90,y=350)
        b4=Button(canvas,text="Next",bg='black', fg='white',font=("Times",15),state=DISABLED, command=f4)
        b4.place(x=290,y=350)
        b6=Button(canvas,text="Repeat word",bg='black', fg='white',font=("Times",15),command=f6)
        b6.place(x=490,y=350)



    global w
    w=[[l[i]for i in range(2)] for l in le]
    delel(canvas1,l1,l2,b1,b2)  
    level()
    f5("Setting environment ...")
    f5("Please don't close the application")
    f5("Your word is: ")
    f5(w[c1-1][c])

    


    
#function for no button    
def f2():
    f5("Quiting ...")
    win.destroy()





#setting up environment
img = PhotoImage(file="backimg.png")
canvas1 = Canvas(win, width = 700,height = 700)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = img, anchor = "nw")
l1=Label(win,text="Welcome to Spellbee!",bg='#f2c941', fg='black',font=("Helvetica",48,BOLD))
l1.place(x=17.5,y=30)
l2=Label(win,text="Do you want to play?",bg='#f2c941', fg='black',font=("Helvetica",48,BOLD))
l2.place(x=36,y=130)
b1=Button(win,text="Yes",bg='black', fg='white',relief="raised",command=f1,height=2,width=15,font=("Times",15))
b1.place(x=400,y=350)
b2=Button(win,text="No",bg='black', fg='white',relief="raised",command=f2,height=2,width=15,font=("Times",15))
b2.place(x=400,y=450)




# closing application
engine.stop()
engine.save_to_file('Comp project', 'test.mp3')
win.mainloop()
