#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
import pandas as pd
from datetime import datetime


# In[9]:


# Initialize a DataFrame to store weather data
weather_df = pd.DataFrame(columns=['timestamp', 'city', 'temperature', 'humidity', 'pressure', 'weather', 'wind_speed', 'season'])


# In[10]:


# Your OpenWeatherMap API key
api_key = '429e6570bf176b57734d33f03e17ea4a'


# In[11]:


# List of cities you want to fetch weather data 
cities = ['North and Middle Andaman ', 'Chittor', 'Guntur', 'Visakhapatnam',
       'Barpeta', 'Cachar', 'Goalpara', 'Jorhat', 'Kamrup',
       'Karbi Anglong', 'Kokrajhar', 'MORIGAON', 'Sonitpur', 'Araria',
       'Bhojpur', 'Madhubani', 'Rohtas', 'Chandigarh', 'Bilaspur',
       'Dhamtari', 'Durg', 'Kondagaon', 'Raipur', 'Rajnandgaon',
       'North Goa', 'South Goa', 'Ahmedabad', 'Amreli', 'Anand',
       'Banaskanth', 'Bharuch', 'Bhavnagar', 'Chhota Udaipur', 'Dahod',
       'Dang', 'Devbhumi Dwarka', 'Gandhinagar', 'Gir Somnath',
       'Jamnagar', 'Junagarh', 'Kachchh', 'Kheda', 'Mehsana', 'Morbi',
       'Navsari', 'Panchmahals', 'Patan', 'Porbandar', 'Rajkot',
       'Sabarkantha', 'Surat', 'Surendranagar', 'Vadodara(Baroda)',
       'Valsad', 'Ambala', 'Bhiwani', 'Fatehabad', 'Gurgaon', 'Hissar',
       'Jhajar', 'Jind', 'Kaithal', 'Kurukshetra', 'Mahendragarh-Narnaul',
       'Mewat', 'Panchkula', 'Panipat', 'Rewari', 'Rohtak', 'Sonipat',
       'Yamuna Nagar', 'Chamba', 'Hamirpur', 'Kangra', 'Kullu', 'Mandi',
       'Shimla', 'Una', 'Anantnag', 'Badgam', 'Baramulla', 'Jammu',
       'Kathua', 'Pulwama', 'Rajouri', 'Srinagar', 'Udhampur',
       'Bangalore', 'Chamrajnagar', 'Chikmagalur', 'Chitradurga',
       'Davangere', 'Kolar', 'Koppal', 'Mandya',
       'Mangalore(Dakshin Kannad)', 'Mysore', 'Raichur', 'Shimoga',
       'Udupi', 'Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasargod',
       'Kollam', 'Kottayam', 'Kozhikode(Calicut)', 'Malappuram',
       'Palakad', 'Pathanamthitta', 'Thirssur', 'Thiruvananthapuram',
       'Wayanad', 'Alirajpur', 'Anupur', 'Ashoknagar', 'Badwani',
       'Balaghat', 'Bhind', 'Bhopal', 'Chhatarpur', 'Chhindwara', 'Datia',
       'Dewas', 'Dhar', 'Dindori', 'Guna', 'Gwalior', 'Harda',
       'Hoshangabad', 'Indore', 'Khandwa', 'Khargone', 'Mandla',
       'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch', 'Rajgarh',
       'Ratlam', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shajapur',
       'Sheopur', 'Tikamgarh', 'Ujjain', 'Vidisha', 'Ahmednagar', 'Akola',
       'Buldhana', 'Kolhapur', 'Mumbai', 'Nagpur', 'Nashik', 'Pune',
       'Raigad', 'Ratnagiri', 'Sangli', 'Satara', 'Sholapur', 'Thane',
       'Yavatmal', 'East Khasi Hills', 'Kohima', 'Mokokchung', 'Delhi',
       'Balasore', 'Bargarh', 'Boudh', 'Dhenkanal', 'Kalahandi',
       'Kendrapara', 'Keonjhar', 'Nayagarh', 'Nuapada', 'Rayagada',
       'Sundergarh', 'Amritsar', 'Bhatinda', 'Faridkot', 'Fatehgarh',
       'Fazilka', 'Ferozpur', 'Gurdaspur', 'Hoshiarpur', 'Jalandhar',
       'Ludhiana', 'Mansa', 'Moga', 'Mohali', 'Nawanshahr', 'Pathankot',
       'Patiala', 'Ropar (Rupnagar)', 'Sangrur', 'Tarntaran', 'Ajmer',
       'Baran', 'Bikaner', 'Bundi', 'Churu', 'Ganganagar', 'Hanumangarh',
       'Jalore', 'Jodhpur', 'Jodhpur Rural', 'Pratapgarh', 'Sikar',
       'Tonk', 'Udaipur', 'Ariyalur', 'Chengalpattu', 'Coimbatore',
       'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode', 'Kallakuruchi',
       'Kancheepuram', 'Karur', 'Krishnagiri', 'Madurai', 'Nagapattinam',
       'Nagercoil (Kannyiakumari)', 'Namakkal', 'Perambalur',
       'Pudukkottai', 'Ramanathapuram', 'Ranipet', 'Salem', 'Sivaganga',
       'Tenkasi', 'Thanjavur', 'The Nilgiris', 'Theni',
       'Thiruchirappalli', 'Thirunelveli', 'Thirupathur', 'Thirupur',
       'Thiruvannamalai', 'Thiruvarur', 'Thiruvellore', 'Tuticorin',
       'Vellore', 'Villupuram', 'Virudhunagar', 'Hyderabad', 'Karimnagar',
       'Khammam', 'Mahbubnagar', 'Medak', 'Nalgonda', 'Nizamabad',
       'Ranga Reddy', 'Warangal', 'Gomati', 'North Tripura', 'Sepahijala',
       'Unokoti', 'Agra', 'Aligarh', 'Ambedkarnagar', 'Amethi', 'Amroha',
       'Auraiya', 'Ayodhya', 'Azamgarh', 'Badaun', 'Baghpat', 'Bahraich',
       'Ballia', 'Balrampur', 'Banda', 'Barabanki', 'Basti',
       'Bhadohi(Sant Ravi Nagar)', 'Bijnor', 'Bulandshahar', 'Chandauli',
       'Etah', 'Etawah', 'Farukhabad', 'Fatehpur', 'Firozabad',
       'Gautam Budh Nagar', 'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur',
       'Hardoi', 'Jalaun (Orai)', 'Jaunpur', 'Jhansi', 'Kannuj', 'Kanpur',
       'Kasganj', 'Kaushambi', 'Khiri (Lakhimpur)', 'Lakhimpur',
       'Lucknow', 'Maharajganj', 'Mahoba', 'Mainpuri', 'Mathura',
       'Mau(Maunathbhanjan)', 'Meerut', 'Mirzapur', 'Muzaffarnagar',
       'Pillibhit', 'Prayagraj', 'Raebarelli', 'Rampur', 'Saharanpur',
       'Sambhal', 'Sant Kabir Nagar', 'Shahjahanpur', 'Shamli',
       'Siddharth Nagar', 'Sitapur', 'Unnao', 'Varanasi', 'Champawat',
       'Dehradoon', 'Haridwar', 'Nanital', 'UdhamSinghNagar',
       'Alipurduar', 'Bankura', 'Birbhum', 'Darjeeling', 'Howrah',
       'Jalpaiguri', 'Kolkata', 'Medinipur(E)', 'Medinipur(W)',
       'Murshidabad', 'Nadia', 'North 24 Parganas', 'Paschim Bardhaman',
       'Purba Bardhaman', 'Puruliya', 'Sounth 24 Parganas',
       'East Godavari', 'Sibsagar', 'Vaishali', 'Surguja', 'Dharwad',
       'Kalburgi', 'Yadgiri', 'Damoh', 'Jabalpur', 'Katni', 'Panna',
       'Raisen', 'Shehdol', 'Umariya', 'Chandrapur', 'Hingoli', 'Latur',
       'Nanded', 'West Garo Hills', 'Dimapur', 'Bhadrak', 'Balotra',
       'Barmer', 'Dausa', 'Dungarpur', 'Nagaur', 'Neem Ka Thana',
       'Bareilly', 'Hathras', 'Lalitpur', 'Uttar Dinajpur', 'Nellore',
       'Darbhanga', 'Jamui', 'Samastipur', 'Janjgir', 'Kanker', 'Korba',
       'Koria', 'Narmada', 'Sirsa', 'Karwar(Uttar Kannad)',
       'Madikeri(Kodagu)', 'Rewa', 'Shivpuri', 'Sidhi', 'Parbhani',
       ' Jhunjhunu', 'Dudu', 'Jhalawar', 'Sanchore', 'Adilabad',
       'West Godavari', 'Kaithar', 'Kishanganj', 'Balodabazar', 'Bastar',
       'Jashpur', 'Kabirdham', 'Raigarh', 'Tumkur', 'Jhabua', 'Jalgaon',
       'Kalimpong', 'Krishna', 'Mungeli', 'Sukma', 'Surajpur', 'Bellary']


# In[12]:


def fetch_weather_data():
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            timestamp = datetime.now()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            weather = data['weather'][0]['description']
            wind_speed = data['wind']['speed']

            # Determine the season based on the month
            month = timestamp.month
            if month in [12, 1, 2]:
                season = 'Winter'
            elif month in [3, 4, 5]:
                season = 'Spring'
            elif month in [6, 7, 8]:
                season = 'Summer'
            else:
                season = 'Autumn'

            # Add data to the DataFrame
            weather_df.loc[len(weather_df)] = [timestamp, city, temperature, humidity, pressure, weather, wind_speed, season]

            # Print the data to check if it's fetching correctly
            print(f"Fetched data for {city}: Temperature={temperature}°C, Humidity={humidity}%, Weather={weather}, Wind Speed={wind_speed} m/s")
        else:
            print(f"Failed to fetch data for {city}. Status code: {response.status_code}")

    # Save the data to a CSV file
    weather_df.to_csv('weather_data.csv', index=False)
    print("Weather data has been updated and saved to weather_data.csv")


# In[13]:


# Fetch the weather data
fetch_weather_data()


# In[14]:


# Display the first few rows of the DataFrame to verify
weather_df.head()

