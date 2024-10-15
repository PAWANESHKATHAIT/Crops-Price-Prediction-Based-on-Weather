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


# In[4]:


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


# In[5]:


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


# In[6]:


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


# In[7]:


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


