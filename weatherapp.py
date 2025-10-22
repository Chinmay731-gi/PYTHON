import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter City: \n")
url = f"https://api.weatherapi.com/v1/current.json?key=0fadfe10156046bf834161328252605&q={city}"
r = requests.get(url)

wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
print(f"The current temperature in {city} is {w}c")
engine.say(f"The current temperature in {city} is {w}Celsius")
engine.setProperty('rate', 150)
engine.runAndWait()




