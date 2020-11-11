import tkinter as tk
import requests
import json as json

root = tk.Tk()
root.title('Codemy Weather App')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x50")

def zipLookup():
    zip.get()
    zipLabel = tk.Label(root, text=zip.get())
    zipLabel.grid(row=1, column=0, columnspan=2)

    #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=0C1ACC43-9292-44A9-AFBD-5CB59EBCE85C

    try:
        # api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=0C1ACC43-9292-44A9-AFBD-5CB59EBCE85C")
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=0C1ACC43-9292-44A9-AFBD-5CB59EBCE85C")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = "#0C0"
        elif category == 'Moderate':
            weather_color = "#FFFF00"
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = "#ff9900"
        elif category == 'Unhealthy':
            weather_color = "#FF0000"
        elif category == 'Very Unhealthy':
            weather_color = "#990066"
        elif category == 'Hazardous':
            weather_color = "#660000"

        root.configure(background=weather_color)

        myLabel = tk.Label(root, text=city + ' Air Quality ' + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

zip = tk.Entry(root)
zip.grid(row=0, column=0, stick=tk.W+tk.E+tk.S+tk.N)

zipButton = tk.Button(root, text="Look up ZipCode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=tk.W+tk.E+tk.S+tk.N)

root.mainloop()
