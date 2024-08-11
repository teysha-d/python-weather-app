import requests
from rich import print
from datetime import datetime

def display_temperature(day, temperature, unit='C'):
  """Displays a temperature with day"""
  print(f"[blue]{day}[/blue]: {round(temperature)}º{unit}")

def display_current_weather(city):
  """Displays the current weather"""
  api_key = "a43ab0c5t7640e69ab4693092fo45cea"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

  response = requests.get(api_url)
  current_weather_data = response.json()
  current_weather_city = current_weather_data['city']
  current_weather_temperature = current_weather_data['temperature']['current']
  
  display_temperature("Today", round(current_weather_temperature))

def display_forecast_weather(city_name):
  """Display the weather forecast of a city"""
  api_key = "a43ab0c5t7640e69ab4693092fo45cea"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

  response = requests.get(api_url)
  forecast_weather_data = response.json()
  print("\n[green bold]Forecast:[/green bold]")
  for day in forecast_weather_data['daily']:
    timestamp = day['time']  
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime("%A")
    temperature = day['temperature']['day']
    
    if date.date() != datetime.today().date():
      display_temperature(formatted_day, round(temperature))

def credit():
  """Display a credit message"""
  print("\n[yellow]This app was built by TD[/yellow]")

def welcome():
  """Display a welcome"""
  print("[blue bold]MY AWESOME WEATHER APP[/blue bold]")
  

welcome()
city_name = input("Enter a city: ")
city_name = city_name.strip()

if city_name:
  display_current_weather(city_name)
  display_forecast_weather(city_name)
  credit()
else:
  print("Please try again with a city")