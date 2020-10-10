from tkinter import * 
import requests
from bs4 import BeautifulSoup

root = Tk()
root.configure(bg='blue')
root.title("Cricket Score Viewer")

root.geometry("500x500")

logo = PhotoImage(file="ipl.png")

def get_data(data):

    team1, team2, team1_score, team2_score, result = data

    url          ='https://www.cricbuzz.com/'
    page         = requests.get(url)
    soup         = BeautifulSoup(page.text,'html.parser')
   
    team_1       = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()
    team_2       = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[1].get_text()
    team_1_score = soup.find_all(class_='cb-ovr-flo')[8].get_text()
    team_2_score = soup.find_all(class_='cb-ovr-flo')[10].get_text()
    result_score = soup.find_all(class_='cb-ovr-flo cb-text-live')[0].get_text()

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

w1          = Label(root, compound = CENTER,image=logo)
a           = Label(text ='IPL Cricket Live Score by SWAPNIL', font ='arial 8')
team1       = Label(text='Team 1', font='arial 20', bg='light goldenrod')
team2       = Label(text='Team 2', font='arial 20', bg='light goldenrod')
team1_score = Label(root, text='hit refresh', font='arial 20', bg='light goldenrod')
team2_score = Label(text='hit refresh', font='arial 20', bg='light goldenrod')


result  = Label(root, text='hit refresh', font='arial 11', bg='light goldenrod')
data    = [team1, team2, team1_score, team2_score, result]
ref     = get_data(data)
refresh = Button(text='Refresh', command=ref, bg='black', fg='white')


# pack
w1.grid(row=0, columnspan=2 ,pady=5)
a.grid(row=1, columnspan=2, pady=5)
team1.grid(row=2, column=0)
team2.grid(row=2, column=1)
team1_score.grid(row=3, column=0, padx=5)
team2_score.grid(row=3, column=1, padx=5)
result.grid(row=4, columnspan=2, pady=5)
refresh.grid(row=5, columnspan=2)

web = Label(root, text='Data is Collected from Cricbuzz', font='ariel 8')
web.grid(row=6, columnspan=2, pady=0)


root.mainloop()
