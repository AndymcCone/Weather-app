from tkinter import *
import requests
from datetime import datetime

#Funktio jolla muokataan säädata JSON-muodosta helpommin luettavaksi
def format_response(weather):
	try:
		name = weather["name"]
		desc = weather["weather"][0]["description"]
		temp = round(weather["main"]["temp"],1)
		sunrise_timestamp = weather["sys"]["sunrise"]
		sunset_timestamp = weather["sys"]["sunset"]
		sunrise = datetime.fromtimestamp(sunrise_timestamp)
		sunset = datetime.fromtimestamp(sunset_timestamp)
		nousu = str(sunrise)
		nousuaika = nousu.split()[1]
		lasku = str(sunset)
		laskuaika = lasku.split()[1]
		
		final_str = "City: %s \nConditions: %s \nTemperature: %s°C \nSun rise: %s \nSun set: %s" % (name, desc, temp, nousuaika, laskuaika)
	except:
		final_str = "City not found"
	
	return final_str

#Funktio jolla haetaan säädata openweathermap-palvelusta saadun API-avaimen avulla.			

def get_weather(city):
	weather_key = "04258f9181beca1c4a57e93e956183f0"
	url = "https://api.openweathermap.org/data/2.5/weather"
	params = {"APPID" : weather_key, "q": city, "units": "metric"}
	response = requests.get(url, params=params)
	weather = response.json()
		
	label["text"] = format_response(weather)
	entry.delete("0","end")

def on_click(event):
    event.widget.delete(0, END)
	
root = Tk()
root.maxsize(950, 600)
root.minsize(450, 250)
root.title("Sääsovellus")
root.iconbitmap("sunico2.ico")

canvas = Canvas(root, height=400, width=600)
canvas.pack()

background_image = PhotoImage(file="bckgrnd.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

entry = Entry(root, bg="#e6f2ff", font=("Calibri", 15), bd=1)
entry.place(relx = 0.126,rely = 0.1, relheight=0.1, relwidth=0.45)
new_text = "Enter city"
entry.insert(0, new_text)
entry.bind("<Button-1>", on_click)

button = Button(root, text="Get weather", font=("Calibri", 15), bd=1, command=lambda: get_weather(entry.get()))
button.place(relx=0.626, rely=0.1, relheight=0.1, relwidth=0.25)

alaruutu = Frame(root, bg="#a6a6a6", bd=1)
alaruutu.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = Label(alaruutu, bg="#e6f2ff",  font=("Calibri", 16))
label.place(relwidth=1, relheight=1)

root.bind("<Return>", lambda event = None: button.invoke()) 
root.mainloop()
