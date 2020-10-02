from tkinter import *

import requests
from bs4 import BeautifulSoup
import time

start = time.time()

root = Tk()
root.configure(bg='sandybrown')
root.title("Cricket Score Viewer by SWAPNIL")
root.geometry("350x183")

def get_data(data):
    team1, team2, team1_score, team2_score, result = data
    url ='https://www.cricbuzz.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    try:
        team_1 = soup.find_all(
                class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()
    except IndexError:
        team_1 = "Name Not Found"

    try:
        team_2 = soup.find_all(
                class_='cb-ovr-flo cb-hmscg-tm-nm')[1].get_text()
    except IndexError:
        team_2 = "Name Not Found"

    try:
        team_1_score = soup.find_all(class_='cb-ovr-flo')[8].get_text()
        if team_1_score == "":
            team_1_score = "0"

    except IndexError:
        team_1_score = "Score Not Found"

    try:
        team_2_score = soup.find_all(class_='cb-ovr-flo')[10].get_text()
        if team_2_score == "":
            team_2_score = "0"
    except IndexError:
        team_2_score = "Score Not Found"

    try:
        result_score = soup.find_all(
                class_='cb-ovr-flo cb-text-live')[0].get_text()
    except IndexError:
        try:
            result_score = soup.find_all(
                    class_='cb-ovr-flo cb-text-complete')[0].get_text()
        except IndexError:
            result_score = "Result Summary Not Found"

    team1.config(text=team_1)
    team2.config(text=team_2)
    team1_score.config(text=team_1_score)
    team2_score.config(text=team_2_score)
    result.config(text=result_score)
    team1.update()
    team2.update()
    team1_score.update()
    team2_score.update()
    result.update()

a = Label(text ='Cricket Live Score by SWAPNIL', font ='arial 8')
a.grid(row=0, columnspan=2, pady=5)
team1 = Label(text='Team 1', font='arial 20', bg='light goldenrod')
team1.grid(row=1, column=0)
team2 = Label(text='Team 2', font='arial 20', bg='light goldenrod')
team2.grid(row=1, column=1)

team1_score = Label(root, text='hit refresh', font='arial 20', bg='light goldenrod')
team1_score.grid(row=2, column=0, padx=5)
team2_score = Label(text='hit refresh', font='arial 20', bg='light goldenrod')
team2_score.grid(row=2, column=1, padx=5)

result = Label(root, text='hit refresh', font='arial 11', bg='light goldenrod')
result.grid(row=3, columnspan=2, pady=5)

data = [team1, team2, team1_score, team2_score, result]
ref = get_data(data)

refresh = Label(text='Scores are refreshed every 2 seconds.', font='arial 20', bg='sandybrown')
refresh.grid(row=4, columnspan=2)

web = Label(root, text='Data Collected from Cricbuzz', font='ariel 8')
web.grid(row=5, columnspan=2, pady=0)

stat = True
def update_stat():
    global stat
    stat = False

root.protocol("WM_DELETE_WINDOW", update_stat)

while(stat == True):
    end = time.time()
    if(abs(((end-start)%2)-0)<=0.2):
        data = [team1, team2, team1_score, team2_score, result]
        ref = get_data(data)
    root.update_idletasks()
    root.update()
    time.sleep(0.01)