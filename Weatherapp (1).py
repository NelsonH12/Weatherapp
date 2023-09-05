import tkinter as tk
import requests

class MyGUI:

  def __init__(self):
    self.window = tk.Tk()
    self.window.title("The Weather App")
    self.window.geometry("600x500")

    self.entered_city=tk.StringVar()

    self.label = tk.Label(self.window, text="Please enter a city to view the weather:", font=("arial", 12))
    self.label.pack()

    self.entered_city = tk.Text(self.window, height=5, font=("Arial", 18))
    self.entered_city.pack(padx=0, pady=0)

    self.button = tk.Button(self.window, text="Search", font=("Arial", 18), command=self.show_weather)
    self.button.pack(padx=10, pady=10)

    self.weather_label = tk.Label(self.window, text="", font=("Arial", 14))
    self.weather_label.pack()

    self.window.mainloop()

  def kelvin_to_c_f(self, kelvin):
    celsius = int(kelvin - 273.15)
    fahrenheit = int(celsius * (9/5) + 32)
    return celsius, fahrenheit

  def show_weather(self):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = open('api_key.txt', 'r').read()
    city = self.entered_city.get("1.0", tk.END)



    url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = self.kelvin_to_c_f(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = self.kelvin_to_c_f(feels_like_kelvin)
    description = response['weather'][0]['description']

    weather_text = f'Current weather conditions in {city}: {description}.\n'
    weather_text += f'Current temperature in {city}: {temp_celsius:.2f}*C or {temp_fahrenheit}*F'

    # Update the label text
    self.weather_label.config(text=weather_text)



if __name__ == "__main__":
  MyGUI()

tk.mainloop()