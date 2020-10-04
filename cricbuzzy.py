from tkinter import *

import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Cricket Score Viewer by SWAPNIL")
root.config(bg="darkblue")
#SWITCH FUNCTION FOR DARK MODE
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg, bg="#2B2B2B", activebackground="#2B2B2B")
        root.config(bg="darkblue")
        Label(f4,font="Helvetica 20 bold",text="Dark Mode Off  ",fg='black',bg='red').grid(row=8, columnspan=2,pady=20)
        btnState = False
    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        root.config(bg="black")
        Label(f4,font="Helvetica 20 bold",text="   Dark Mode On",fg='black',bg='red').grid(row=8, columnspan=2,pady=20)
        btnState = True
onImg = PhotoImage(file="onbutton.png")
offImg = PhotoImage(file="offbutton.png")


#MAIN FRAME AND LABEL FOR SWAPNIL
frame1=Frame(root,bg="red",borderwidth=10)
frame1.pack(side=TOP,fill=X)
MAIN=Label(frame1,font="Helvetica 25 bold",fg="violet",relief="sunken",text="Cricket Score Viewer by SWAPNIL")
MAIN.pack(fill=X,side="top")


#REFRESH BUTTON FRAME
frame3=Frame(root,bg="red",borderwidth=10,relief=GROOVE)
frame3.pack(side=BOTTOM,fill=X)

#FRAME FOR RESULT OF WIN OR LOSS
frame4=Frame(root,bg="green",borderwidth=10,relief=GROOVE)
frame4.pack(side=BOTTOM,fill=X)

#DATA COLLECTED FROM CRICBUZZ
frame2=Frame(root,bg="dark blue",borderwidth=10)
frame2.pack(side=TOP,fill=X)
Label(frame2,font="comicsansms 15 bold",fg='black',relief="groove",bg='red',text='Data Collected From Cricbuzz').pack(fill=X,side="bottom")


global f2,f3
#FRAME FOR TEAM 1
f2=Frame(root,bg="red",borderwidth=15,relief=RAISED)
f2.pack(fill=BOTH,padx=30,side=LEFT,pady=10)
#FRAME FOR TEAM 2
f3=Frame(root,bg="red",borderwidth=15,relief=RAISED)
f3.pack(fill=BOTH,side=RIGHT,pady=10,padx=30)



def get_data():
    url ='https://www.cricbuzz.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    global t1,t2, t1score ,t2score
    team_1 = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()
    t1 = StringVar(root,value=team_1)
    team_2 = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[1].get_text()
    t2= StringVar(root,value=team_2)
    team_1_score = soup.find_all(class_='cb-ovr-flo')[8].get_text()
    t1score = StringVar(root,value=team_1_score)
    team_2_score = soup.find_all(class_='cb-ovr-flo')[10].get_text()
    t2score = StringVar(root,value=team_2_score)
    result_score = soup.find_all(class_='cb-ovr-flo cb-text-complete')[0].get_text()
    
    if result_score not  in (team_1 or team_2):
        result_score = soup.find_all(class_='cb-ovr-flo cb-text-live')[0].get_text()
        global rscore
        rscore = StringVar(root,value=result_score)
    else:
        rscore = StringVar(root,value=result_score)
        
    rscore = StringVar(root,value=result_score)
    #LABELS THAT CAN CHANGE VALUES
    team1 = Label(f2,font="Helvetica 20 bold",textvariable=t1,fg='white',bg='red').grid(row=3,column=1)
    team2 = Label(f3,font="Helvetica 20 bold",textvariable=t2,fg='white',bg='red').grid(row=3,column=1)
    team1_score = Label(f2,font="comicsansms 15 bold",fg='black',bg='red',textvariable=t1score).grid(row=10,column=0,sticky=E,pady=10)
    team2_score = Label(f3,font="comicsansms 15 bold",fg='black',bg='red',textvariable=t2score).grid(row=10,column=0,sticky=E,pady=10)
    r_score = Label(frame4,font="comicsansms 15 bold",fg='black',bg='green',textvariable=rscore).grid(row=15,column=0,sticky=E,pady=10)
    

get_data()
#LABELS THAT CAN NOT CHANGE VALUES
team1_Label = Label(f2,font="Helvetica 20 bold",text="Team 1 - ",fg='white',bg='red').grid(row=3,column=0)
Label(f2,font="comicsansms 15 bold",fg='black',bg='red', text="                      SCORE                   ").grid(row=8,column=0,sticky=E,pady=10)
team2_Label = Label(f3,font="Helvetica 20 bold",text="Team 2 - ",fg='white',bg='red').grid(row=3,column=0)
Label(f3,font="comicsansms 15 bold",fg='black',bg='red', text="                            SCORE                     ").grid(row=8,column=0,sticky=E,pady=10)




    


#DARK MODE BUTTON
global f4
f4=Frame(root,bg="red",borderwidth=10,relief=SUNKEN)
f4.pack(fill=Y,pady=50,anchor=CENTER)
btn = Button(f4, text="OFF", borderwidth=0, command=switch, bg="darkblue", activebackground="darkblue", pady=1)
btn.grid(row=7, columnspan=2,pady=20)
btn.config(image=offImg)
btnState = False
#REFRESH BUTTON
refresh = Button(frame3,bg="yellow",text="REFRESH",command=get_data,width=20).pack(fill=X,side=TOP)

