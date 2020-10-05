from tkinter import *
import requests
from bs4 import BeautifulSoup

# Initialisation
refresh_time = 1000* 2 # Refresh every 2 seconds

# Background colors
original_bg = '#CECCBE'
dark_bg = "#2B2B2B"

# Set up tkinter root window
root = Tk()
root.title("Cricket Score Viewer by SWAPNIL")
root.configure(bg=original_bg)

# Darkmode (button images, function, )
onImg = PhotoImage(file="onbutton.png")
offImg = PhotoImage(file="offbutton.png")
def darkmode_switch():
    # Check current bg colour
    current_bg = root.cget('bg')
    # If current_bg is original, change new_bg to dark (vice versa)
    if current_bg == original_bg:
        new_bg = dark_bg
        darkmodetxt_label.config(text="Dark Mode: ON", bg=new_bg)
    elif current_bg == dark_bg:
        new_bg = original_bg
        darkmodetxt_label.config(text="Dark Mode: OFF", bg=new_bg)
    
    # Set bg to new_bg, fg to current_bg
    darkmode_btn.config(image=offImg, bg=new_bg, activebackground=new_bg)
    root.config(bg=new_bg)
    for item in all_objects:
        item.config(bg=new_bg, fg=current_bg)
        
def get_data():
    """A helper function which fetch the data and update the UI"""
    
    # Set data to scrape from headersite
    var_name_list = ['team1', 'team2', 'team1_score', 'team2_score', 'result']
    soup_find_list = {
                    'cb-ovr-flo cb-hmscg-tm-nm' : (0, 1),
                    'cb-ovr-flo' : (8, 10),
                    'cb-ovr-flo cb-text-live' : (0,)
                    }

    # URL Request
    url ='https://www.cricbuzz.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    
    # Store values in dictionary object
    data = {}  # Use a dictionary to store header crawling data
    iteration = 0
    for k, v in soup_find_list.items():
        for i in v:
            try:
                soup_found = soup.find_all(class_=k)[i].get_text()
                if soup_found == None:
                    data[var_name_list[iteration]] = '-'
                else:
                    data[var_name_list[iteration]] = soup_found
            except IndexError:
                data[var_name_list[iteration]] = 'N.A.'
            iteration += 1

    # Update the text labels
    team1.config(text=data.get('team1'))
    team2.config(text=data.get('team2'))
    team1_score.config(text=data.get('team1_score'))
    team2_score.config(text=data.get('team2_score'))
    result.config(text=data.get('result'))
    root.after(refresh_time, get_data)

# Initialise Tkinter objects
a = Label(text ='Cricket Live Score by SWAPNIL', font ='arial 8')
team1 = Label(text='Team 1', font='arial 20', bg=original_bg)
team2 = Label(text='Team 2', font='arial 20', bg=original_bg)
team1_score = Label(root, text='hit refresh', font='arial 20', bg=original_bg)
team2_score = Label(text='hit refresh', font='arial 20', bg=original_bg)
result = Label(root, text='hit refresh', font='arial 11', bg=original_bg)
refresh = Button(text='Refresh', command=get_data, bg=original_bg, fg=dark_bg)
header = Label(root, text='Data Collected from Cricbuzz', font='ariel 8')
darkmodetxt_label = Label(root, text="Dark Mode: OFF", font="FixedSys 17", bg=original_bg, fg="green")
darkmode_btn = Button(root, image=offImg, borderwidth=0, command=darkmode_switch, bg=original_bg, activebackground=original_bg, pady=1)

# Put our Tkinter objects on grid
a.grid(                 row=0, columnspan=2, pady=5)
team1.grid(             row=1, column=0, padx=15)
team2.grid(             row=1, column=1)
team2_score.grid(       row=2, column=1, padx=5)
team1_score.grid(       row=2, column=0, padx=5)
result.grid(            row=3, columnspan=2, pady=5)
refresh.grid(           row=4, columnspan=2)
header.grid(               row=5, columnspan=2, pady=0)
darkmodetxt_label.grid( row=8, columnspan=2)
darkmode_btn.grid(      row=7, columnspan=2, pady=20)

all_objects = [team1, team2, team1_score, team2_score, result, refresh]

# Run get_data after mainloop starts
root.after(0, get_data)

# Run the app
try:
    print("CTRL + C to close or click close button")
    root.mainloop()
except KeyboardInterrupt:
    print("Thanks for using Cricket Score Viewer")
except Exception as e:
    print("UnKnownError:%s. Please report to the author"%str(e))