import requests
from bs4 import BeautifulSoup



def get_weather(city):

  weather = requests.get(f"https://sinoptik.ua/погода-{city}")
  soup = BeautifulSoup(weather.content)
  temp = soup.find("p", class_="today-temp").text
  
  return temp 