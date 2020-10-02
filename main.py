from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.configure(bg='sandybrown')
root.title("Cricket Score Viewer by SWAPNIL")
root.geometry("350x183")

# refresh time 
refresh_time = 2*1000 # refesh after 2 sec 

def get_data():
    """A helper function which fetch the data and update the UI"""
    team1, team2, team1_score, team2_score, result = data

    url          ='https://www.cricbuzz.com/'
    page         = requests.get(url)
    soup         = BeautifulSoup(page.text,'html.parser')
    team_1       = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()
    team_2       = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[1].get_text()
    team_1_score = soup.find_all(class_='cb-ovr-flo')[8].get_text()
    team_2_score = soup.find_all(class_='cb-ovr-flo')[10].get_text()
    try:
        # when there is not match, this will have no value. It may throw except IndexError.
        result_score = soup.find_all(class_='cb-ovr-flo cb-text-live')[0].get_text()
    except IndexError:
        result_score = 0

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

# Component defination
a           = Label(text ='Cricket Live Score by SWAPNIL', font ='arial 8')
team1       = Label(text='Team 1', font='arial 20', bg='light goldenrod')
team2       = Label(text='Team 2', font='arial 20', bg='light goldenrod')
team1_score = Label(root, text='hit refresh', font='arial 20', bg='light goldenrod')
team2_score = Label(text='hit refresh', font='arial 20', bg='light goldenrod')
result  = Label(root, text='hit refresh', font='arial 11', bg='light goldenrod')

# for force refresh button 
data    = [team1, team2, team1_score, team2_score, result]
ref     = get_data()
refresh = Button(text='Refresh', command=ref, bg='black', fg='white')

# Layout the components
a.grid(row=0, columnspan=2, pady=5)
team1.grid(row=1, column=0)
team2.grid(row=1, column=1)
team1_score.grid(row=2, column=0, padx=5)
team2_score.grid(row=2, column=1, padx=5)
result.grid(row=3, columnspan=2, pady=5)
refresh.grid(row=4, columnspan=2)
web = Label(root, text='Data Collected from Cricbuzz', font='ariel 8')
web.grid(row=5, columnspan=2, pady=0)

def get_data():
    """A loop callback funtion called every refresh_time sec"""
    # print("refreshing..")
    root.after(refresh_time, get_data)  

# initial scheduling
root.after(refresh_time, get_data)

# run the app
try:
    print("CTRL + C to close or click close button")
    root.mainloop()

except KeyboardInterrupt:
    print("Thanks for using Cricket Score Viewer")

except Exception as e:
    print("UnKnownError:%s. Please report to the author"%str(e))

