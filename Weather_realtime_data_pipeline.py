#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from datetime import datetime
import schedule
import time


# In[2]:


# Initialize a DataFrame to store weather data
weather_df = pd.DataFrame(columns=['timestamp', 'city', 'temperature', 'humidity', 'pressure', 'weather', 'wind_speed', 'season'])


# In[3]:


# Your OpenWeatherMap API key
api_key = '429e6570bf176b57734d33f03e17ea4a'
# List of cities you want to fetch weather data for
cities = ['Delhi', 'Mumbai', 'Bangalore']


# In[4]:


# Function to fetch weather data
def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

# Fetch weather data for each city and print results
for city in cities:
    weather_data = fetch_weather(city, api_key)
    if weather_data:
        print(f"Weather in {city}: {weather_data['main']['temp']}°C, {weather_data['weather'][0]['description']}")


# In[5]:


# Function to determine the current season based on Indian weather
def get_current_season():
    month = datetime.now().month
    if month in [12, 1, 2, 3]:  # Winter: December to early April
        return 'Winter'
    elif month in [4, 5, 6]:    # Summer or pre-monsoon: April to June (or July in NW India)
        return 'Summer'
    elif month in [7, 8, 9]:    # Monsoon or rainy: June to September
        return 'Monsoon'
    else:                       # Post-monsoon: October to December
        return 'Post-monsoon'


# In[6]:


# Function to update weather DataFrame and save to CSV
def job():
    global weather_df
    for city in cities:
        weather_data = fetch_weather(city, api_key)
        if weather_data is not None:
            new_data = pd.DataFrame([{
                "timestamp": datetime.now(),
                "city": city,
                "temperature": weather_data['main']['temp'],
                "humidity": weather_data['main']['humidity'],
                "pressure": weather_data['main']['pressure'],
                "weather": weather_data['weather'][0]['description'],
                "wind_speed": weather_data['wind']['speed'],
                "season": get_current_season()
            }])
            weather_df = pd.concat([weather_df, new_data], ignore_index=True)

    # Save the DataFrame to CSV
    weather_df.to_csv('weather_data.csv', index=False)
    print("Updated weather DataFrame:")
    print(weather_df)

# For testing purposes, run the job function
job()
print("Final DataFrame:")
print(weather_df)


# In[7]:


# Function to schedule the job
schedule.every().day.at("08:00").do(job)  # Set to run daily at 08:00 AM


# In[ ]:


# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)  # Wait for one second before checking again

